
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

    Sınıf/dönem sütunlarına yerleştirme yapar ve aynı öğretim üyesi veya
    dersliğin aynı zaman diliminde tekrar kullanılmamasına çalışır.
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
            key=lambda ders: (ders.sinif, ders.donem, ders.bolum_kodu != "ORT", ders.ders_kodu),
        )

        for ders in sorted_courses:
            sinif = min(max(ders.sinif, 1), 4)
            placed = 0
            total_slots = len(self.days) * len(self.hours)
            start_index = next_index_by_class[sinif]

            for offset in range(total_slots * 2):
                if placed >= ders.haftalik_saat:
                    break

                slot_index = (start_index + offset) % total_slots
                gun = self.days[slot_index // len(self.hours)]
                saat = self.hours[slot_index % len(self.hours)]

                instructor_key = (gun, saat, ders.ogretim_uyesi)
                classroom_key = (gun, saat, ders.derslik_id)

                if instructor_key in used_instructor or classroom_key in used_classroom:
                    continue

                schedule.get_cell(gun, saat, sinif).dersler.append(ders)
                used_instructor.add(instructor_key)
                used_classroom.add(classroom_key)
                placed += 1
                next_index_by_class[sinif] = (slot_index + 1) % total_slots

            if placed < ders.haftalik_saat:
                raise RuntimeError(
                    f"{ders.ders_kodu} dersi için yeterli çakışmasız zaman dilimi bulunamadı."
                )

        return schedule

    def generate_for_department(self, dersler: Iterable[ProgramDersi], bolum_kodu: str, baslik: str) -> Schedule:
        return self.generate(self.filter_by_department(dersler, bolum_kodu), baslik=baslik)
