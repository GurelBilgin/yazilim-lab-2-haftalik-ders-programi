
from pathlib import Path
import unittest

from haftalik_ders_programi.seed_loader import (
    donemden_sinif_bul,
    load_bolumler,
    load_dersler,
    load_derslikler,
    load_kullanicilar,
    load_program_dersleri,
)


SQL_DIR = Path(__file__).resolve().parents[1] / "sql"


class SeedLoaderTestleri(unittest.TestCase):
    def test_sql_dump_dosyalarini_okur(self):
        self.assertGreaterEqual(len(load_bolumler(SQL_DIR)), 3)
        self.assertGreaterEqual(len(load_derslikler(SQL_DIR)), 10)
        self.assertGreaterEqual(len(load_kullanicilar(SQL_DIR)), 10)
        self.assertGreaterEqual(len(load_dersler(SQL_DIR)), 50)

    def test_donemden_sinif_bulur(self):
        self.assertEqual(donemden_sinif_bul(1), 1)
        self.assertEqual(donemden_sinif_bul(2), 1)
        self.assertEqual(donemden_sinif_bul(7), 4)

    def test_program_dersleri_birlestirilir(self):
        dersler = load_program_dersleri(SQL_DIR)
        self.assertTrue(any(ders.bolum_kodu == "YZM" for ders in dersler))
        self.assertTrue(any(ders.bolum_kodu == "BLM" for ders in dersler))
        self.assertTrue(any(ders.ogretim_uyesi for ders in dersler))


if __name__ == "__main__":
    unittest.main()
