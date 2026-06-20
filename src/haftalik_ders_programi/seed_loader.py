
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Iterable

from .models import Bolum, Ders, Derslik, Kullanici, ProgramDersi


INSERT_PATTERN = re.compile(r"INSERT INTO `(?P<table>\w+)` VALUES (?P<values>.*?);", re.DOTALL)


def _read_values(sql_path: Path) -> tuple:
    """MySQL dump dosyasındaki INSERT değerlerini tuple olarak okur."""
    text = sql_path.read_text(encoding="utf-8", errors="replace")
    match = INSERT_PATTERN.search(text)
    if not match:
        return tuple()
    return ast.literal_eval("(" + match.group("values") + ")")


def load_bolumler(sql_dir: str | Path) -> list[Bolum]:
    rows = _read_values(Path(sql_dir) / "app_bolum.sql")
    return [Bolum(*row) for row in rows]


def load_derslikler(sql_dir: str | Path) -> list[Derslik]:
    rows = _read_values(Path(sql_dir) / "app_derslik.sql")
    return [Derslik(row[0], int(row[1]), row[2]) for row in rows]


def load_kullanicilar(sql_dir: str | Path) -> list[Kullanici]:
    rows = _read_values(Path(sql_dir) / "app_kullanici.sql")
    return [Kullanici(int(row[0]), row[1], row[2], row[3], row[4]) for row in rows]


def load_dersler(sql_dir: str | Path) -> list[Ders]:
    rows = _read_values(Path(sql_dir) / "app_dersler.sql")
    return [
        Ders(
            ders_kodu=row[0],
            ders_adi=row[1],
            haftalik_saat=int(row[2]),
            ogretim_uyesi_id=int(row[3]),
            bolum_kodu=row[4],
            derslik_id=row[5],
            donem=int(row[6]),
            akts=int(row[7]),
            ders_turu=row[8],
        )
        for row in rows
    ]


def donemden_sinif_bul(donem: int) -> int:
    """Dönem bilgisinden sınıf seviyesini üretir."""
    if donem <= 0:
        raise ValueError("Dönem değeri pozitif olmalıdır.")
    return (donem + 1) // 2


def build_program_dersleri(
    dersler: Iterable[Ders],
    bolumler: Iterable[Bolum],
    kullanicilar: Iterable[Kullanici],
) -> list[ProgramDersi]:
    """Ders, bölüm ve öğretim üyesi kayıtlarını birleştirir."""
    bolum_map = {bolum.bolum_kodu: bolum for bolum in bolumler}
    kullanici_map = {kullanici.id: kullanici for kullanici in kullanicilar}

    program_dersleri: list[ProgramDersi] = []
    for ders in dersler:
        bolum = bolum_map.get(ders.bolum_kodu)
        ogretim_uyesi = kullanici_map.get(ders.ogretim_uyesi_id)
        if bolum is None or ogretim_uyesi is None:
            continue
        program_dersleri.append(
            ProgramDersi(
                ders_kodu=ders.ders_kodu,
                ders_adi=ders.ders_adi,
                haftalik_saat=ders.haftalik_saat,
                bolum_kodu=ders.bolum_kodu,
                bolum_adi=bolum.bolum_adi,
                donem=ders.donem,
                sinif=donemden_sinif_bul(ders.donem),
                ogretim_uyesi="" if ogretim_uyesi.ad_soyad.strip().lower() == "yönetici" else ogretim_uyesi.ad_soyad,
                derslik_id=ders.derslik_id,
                ders_turu=ders.ders_turu,
            )
        )
    return program_dersleri


def load_program_dersleri(sql_dir: str | Path) -> list[ProgramDersi]:
    """SQL dump klasöründen program oluşturma için gereken ders kayıtlarını okur."""
    return build_program_dersleri(
        dersler=load_dersler(sql_dir),
        bolumler=load_bolumler(sql_dir),
        kullanicilar=load_kullanicilar(sql_dir),
    )
