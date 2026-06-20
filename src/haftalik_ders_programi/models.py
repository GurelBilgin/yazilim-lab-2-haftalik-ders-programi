
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Bolum:
    """Bölüm bilgisini temsil eder."""

    bolum_kodu: str
    bolum_adi: str


@dataclass(frozen=True)
class Derslik:
    """Derslik bilgisini temsil eder."""

    derslik_id: str
    kapasite: int
    statu: str


@dataclass(frozen=True)
class Kullanici:
    """Kullanıcı / öğretim üyesi bilgisini temsil eder."""

    id: int
    ad_soyad: str
    email: str
    parola: str
    role: str


@dataclass(frozen=True)
class Ders:
    """Ders bilgisini temsil eder."""

    ders_kodu: str
    ders_adi: str
    haftalik_saat: int
    ogretim_uyesi_id: int
    bolum_kodu: str
    derslik_id: str
    donem: int
    akts: int
    ders_turu: str


@dataclass(frozen=True)
class ProgramDersi:
    """Program çıktısına yerleştirilecek zenginleştirilmiş ders kaydı."""

    ders_kodu: str
    ders_adi: str
    haftalik_saat: int
    bolum_kodu: str
    bolum_adi: str
    donem: int
    sinif: int
    ogretim_uyesi: str
    derslik_id: str
    ders_turu: str

    @property
    def hucre_metni(self) -> str:
        """Excel hücresinde gösterilecek metni üretir."""
        return (
            f"{self.ders_kodu} - {self.ders_adi}\n"
            f"Öğretim Üyesi: {self.ogretim_uyesi}\n"
            f"Derslik: {self.derslik_id}\n"
            f"Tür: {self.ders_turu}"
        )
