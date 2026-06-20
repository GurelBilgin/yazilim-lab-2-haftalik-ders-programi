from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from .models import ProgramDersi


DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
HOURS = [
    "09:00-10:00",
    "10:00-11:00",
    "11:00-12:00",
    "12:00-13:00",
    "13:00-14:00",
    "14:00-15:00",
    "15:00-16:00",
    "16:00-17:00",
]
SINIFLAR = [1, 2, 3, 4]
Slot = tuple[int, int, str, str]


@dataclass
class ScheduleCell:
    """Bir zaman diliminde yer alan dersleri tutar."""

    dersler: list[ProgramDersi] = field(default_factory=list)

    @property
    def metin(self) -> str:
        if not self.dersler:
            return ""
        return "\n\n".join(ders.hucre_metni for ders in self.dersler)


@dataclass
class Schedule:
    """Haftalık ders programı tablosunu temsil eder."""

    baslik: str
    tablo: dict[tuple[str, str, int], ScheduleCell] = field(default_factory=dict)

    def get_cell(self, gun: str, saat: str, sinif: int) -> ScheduleCell:
        return self.tablo.setdefault((gun, saat, sinif), ScheduleCell())


class ScheduleGenerator:
    """Ders kayıtlarından haftalık program üretir.

    Yerleştirme mantığı kural tabanlıdır. Aynı sınıf, öğretim üyesi veya
    derslik için saat çakışması oluşturulmaz. Ders saatleri mümkün olduğunca
    aynı gün içinde arka arkaya blok olarak yerleştirilir. Örneğin 3 saatlik
    bir ders için önce 3 saatlik blok aranır; bulunamazsa 2+1 şeklinde daha
    düzenli bir bölme denenir.
    """

    def __init__(self, days: list[str] | None = None, hours: list[str] | None = None):
        self.days = days or DAYS
        self.hours = hours or HOURS

    def filter_by_department(self, dersler: Iterable[ProgramDersi], bolum_kodu: str) -> list[ProgramDersi]:
        bolum_kodu = bolum_kodu.upper()
        allowed_codes = {bolum_kodu, "ORT"}
        return [ders for ders in dersler if ders.bolum_kodu.upper() in allowed_codes]

    def generate(self, dersler: Iterable[ProgramDersi], baslik: str) -> Schedule:
        schedule = Schedule(baslik=baslik)
        used_instructor: set[tuple[str, str, str]] = set()
        used_classroom: set[tuple[str, str, str]] = set()
        next_index_by_class: dict[int, int] = defaultdict(int)

        sorted_courses = sorted(
            dersler,
            key=lambda ders: (
                ders.sinif,
                ders.donem,
                -ders.haftalik_saat,
                ders.bolum_kodu != "ORT",
                ders.ders_kodu,
            ),
        )

        for ders in sorted_courses:
            sinif = min(max(ders.sinif, 1), 4)
            start_index = next_index_by_class[sinif]
            slots = self._find_slots_for_course(
                ders=ders,
                sinif=sinif,
                start_index=start_index,
                used_instructor=used_instructor,
                used_classroom=used_classroom,
            )
            if not slots:
                raise RuntimeError(
                    f"{ders.ders_kodu} dersi için yeterli çakışmasız zaman dilimi bulunamadı."
                )

            self._place_slots(
                schedule=schedule,
                ders=ders,
                sinif=sinif,
                slots=slots,
                used_instructor=used_instructor,
                used_classroom=used_classroom,
            )
            last_slot = slots[-1]
            next_index_by_class[sinif] = self._flat_index(last_slot[0], last_slot[1]) + 1

        return schedule

    def generate_for_department(self, dersler: Iterable[ProgramDersi], bolum_kodu: str, baslik: str) -> Schedule:
        return self.generate(self.filter_by_department(dersler, bolum_kodu), baslik=baslik)

    def _find_slots_for_course(
        self,
        ders: ProgramDersi,
        sinif: int,
        start_index: int,
        used_instructor: set[tuple[str, str, str]],
        used_classroom: set[tuple[str, str, str]],
    ) -> list[Slot] | None:
        hours_needed = max(1, ders.haftalik_saat)

        # 1) Önce dersin tüm saatlerini aynı gün içinde arka arkaya blok olarak yerleştir.
        for plan in self._candidate_full_block_plans(hours_needed, start_index):
            if self._can_place_plan(ders, sinif, plan, used_instructor, used_classroom):
                return plan

        # 2) Tam blok bulunamazsa daha az parçalı ve düzenli bölünmüş planları dene.
        for plan in self._candidate_split_plans(hours_needed, start_index):
            if self._can_place_plan(ders, sinif, plan, used_instructor, used_classroom):
                return plan

        return None

    def _candidate_full_block_plans(self, block_size: int, start_index: int) -> list[list[Slot]]:
        if block_size > len(self.hours):
            return []
        blocks: list[list[Slot]] = []
        for day_idx, gun in enumerate(self.days):
            for hour_idx in range(0, len(self.hours) - block_size + 1):
                blocks.append([
                    (day_idx, hour_idx + offset, gun, self.hours[hour_idx + offset])
                    for offset in range(block_size)
                ])
        return self._sort_plans_by_start(blocks, start_index)

    def _candidate_split_plans(self, hours_needed: int, start_index: int) -> list[list[Slot]]:
        if hours_needed <= 1:
            return []

        block_sizes = self._split_block_sizes(hours_needed)
        if not block_sizes:
            return []

        candidate_groups = [self._candidate_full_block_plans(size, start_index) for size in block_sizes]
        plans: list[list[Slot]] = []

        def backtrack(group_index: int, selected: list[Slot]) -> None:
            if group_index == len(candidate_groups):
                plans.append(selected.copy())
                return
            for block in candidate_groups[group_index]:
                combined = selected + block
                if len({(slot[0], slot[1]) for slot in combined}) != len(combined):
                    continue
                backtrack(group_index + 1, combined)

        backtrack(0, [])
        return sorted(plans, key=self._split_plan_score)

    @staticmethod
    def _split_block_sizes(hours_needed: int) -> list[int]:
        if hours_needed == 2:
            return []
        if hours_needed == 3:
            return [2, 1]
        if hours_needed == 4:
            return [2, 2]
        if hours_needed == 5:
            return [3, 2]
        return [3, hours_needed - 3]

    def _can_place_plan(
        self,
        ders: ProgramDersi,
        sinif: int,
        slots: list[Slot],
        used_instructor: set[tuple[str, str, str]],
        used_classroom: set[tuple[str, str, str]],
    ) -> bool:
        if len({(slot[0], slot[1]) for slot in slots}) != len(slots):
            return False

        instructor = ders.ogretim_uyesi.strip()
        classroom = ders.derslik_id.strip()

        for _day_idx, _hour_idx, gun, saat in slots:
            if instructor and (gun, saat, instructor) in used_instructor:
                return False
            if classroom and (gun, saat, classroom) in used_classroom:
                return False
        return True

    @staticmethod
    def _place_slots(
        schedule: Schedule,
        ders: ProgramDersi,
        sinif: int,
        slots: list[Slot],
        used_instructor: set[tuple[str, str, str]],
        used_classroom: set[tuple[str, str, str]],
    ) -> None:
        instructor = ders.ogretim_uyesi.strip()
        classroom = ders.derslik_id.strip()

        for _day_idx, _hour_idx, gun, saat in slots:
            schedule.get_cell(gun, saat, sinif).dersler.append(ders)
            if instructor:
                used_instructor.add((gun, saat, instructor))
            if classroom:
                used_classroom.add((gun, saat, classroom))

    def _sort_plans_by_start(self, plans: list[list[Slot]], start_index: int) -> list[list[Slot]]:
        total_slots = len(self.days) * len(self.hours)
        return sorted(
            plans,
            key=lambda plan: (
                (self._flat_index(plan[0][0], plan[0][1]) - start_index) % total_slots,
                plan[0][0],
                plan[0][1],
            ),
        )

    def _split_plan_score(self, plan: list[Slot]) -> tuple[int, int, int, int]:
        days_used = {slot[0] for slot in plan}
        first_hour_single_penalty = 0
        if len(plan) >= 3:
            hour_counts: dict[tuple[int, int], int] = defaultdict(int)
            for day_idx, hour_idx, *_ in plan:
                hour_counts[(day_idx, hour_idx)] += 1
            first_hour_single_penalty = sum(1 for day_idx, hour_idx, *_ in plan if hour_idx == 0)

        # Planı insan eliyle hazırlanmış gibi göstermek için önce az gün, sonra
        # 09:00 tek saat parçalarını daha az tercih eden sıralama kullanılır.
        earliest = min(self._flat_index(slot[0], slot[1]) for slot in plan)
        latest = max(self._flat_index(slot[0], slot[1]) for slot in plan)
        span = latest - earliest
        return (len(days_used), first_hour_single_penalty, span, earliest)

    def _flat_index(self, day_idx: int, hour_idx: int) -> int:
        return day_idx * len(self.hours) + hour_idx
