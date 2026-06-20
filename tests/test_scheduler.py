from pathlib import Path
import unittest

from haftalik_ders_programi.models import ProgramDersi
from haftalik_ders_programi.scheduler import ScheduleGenerator
from haftalik_ders_programi.seed_loader import load_program_dersleri


SQL_DIR = Path(__file__).resolve().parents[1] / "sql"


class ScheduleGeneratorTestleri(unittest.TestCase):
    def setUp(self):
        self.dersler = load_program_dersleri(SQL_DIR)
        self.generator = ScheduleGenerator()

    def test_bolum_filtresi_ortak_dersleri_dahil_eder(self):
        yzm = self.generator.filter_by_department(self.dersler, "YZM")
        self.assertTrue(any(ders.bolum_kodu == "YZM" for ders in yzm))
        self.assertTrue(any(ders.bolum_kodu == "ORT" for ders in yzm))
        self.assertFalse(any(ders.bolum_kodu == "BLM" for ders in yzm))

    def test_program_olusturur(self):
        yzm = self.generator.filter_by_department(self.dersler, "YZM")
        schedule = self.generator.generate(yzm, "Yazılım Mühendisliği")
        dolu_hucreler = [
            cell for cell in schedule.tablo.values()
            if cell.dersler
        ]
        self.assertGreater(len(dolu_hucreler), 0)

    def test_ogretim_uyesi_zaman_cakismasi_uretmez(self):
        yzm = self.generator.filter_by_department(self.dersler, "YZM")
        schedule = self.generator.generate(yzm, "Yazılım Mühendisliği")
        seen = set()
        for (gun, saat, _sinif), cell in schedule.tablo.items():
            for ders in cell.dersler:
                if not ders.ogretim_uyesi.strip():
                    continue
                key = (gun, saat, ders.ogretim_uyesi)
                self.assertNotIn(key, seen)
                seen.add(key)

    def test_yonetici_ogretim_uyesi_bos_birakilir(self):
        dersler = load_program_dersleri(SQL_DIR)
        self.assertTrue(any(ders.ogretim_uyesi == "" for ders in dersler))
        self.assertFalse(any(ders.ogretim_uyesi == "Yönetici" for ders in dersler))

    def test_uc_saatlik_ders_mumkunse_blok_yerlesir(self):
        ders = ProgramDersi(
            ders_kodu="TST101",
            ders_adi="Test Dersi",
            haftalik_saat=3,
            bolum_kodu="YZM",
            bolum_adi="Yazılım Mühendisliği",
            donem=1,
            sinif=1,
            ogretim_uyesi="Test Öğretim Üyesi",
            derslik_id="D101",
            ders_turu="Zorunlu",
        )
        schedule = self.generator.generate([ders], "Test Programı")
        yerler = [
            (gun, saat)
            for (gun, saat, _sinif), cell in schedule.tablo.items()
            if cell.dersler
        ]
        self.assertEqual(yerler, [
            ("Pazartesi", "09:00-10:00"),
            ("Pazartesi", "10:00-11:00"),
            ("Pazartesi", "11:00-12:00"),
        ])


if __name__ == "__main__":
    unittest.main()
