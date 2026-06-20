
from pathlib import Path
import unittest

from haftalik_ders_programi.scheduler import DAYS, HOURS, ScheduleGenerator
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
                key = (gun, saat, ders.ogretim_uyesi)
                self.assertNotIn(key, seen)
                seen.add(key)


if __name__ == "__main__":
    unittest.main()
