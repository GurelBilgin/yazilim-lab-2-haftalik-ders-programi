
from __future__ import annotations

import argparse
from pathlib import Path

from .excel_exporter import export_schedule
from .scheduler import ScheduleGenerator
from .seed_loader import load_program_dersleri


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Haftalık ders programı Excel çıktısı oluşturur.")
    parser.add_argument("--sql-dir", default="sql", help="MySQL dump dosyalarının bulunduğu klasör.")
    parser.add_argument("--output-dir", default="outputs", help="Excel çıktı klasörü.")
    parser.add_argument(
        "--department",
        choices=["YZM", "BLM", "ALL"],
        default="ALL",
        help="Üretilecek bölüm programı.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    sql_dir = Path(args.sql_dir)
    output_dir = Path(args.output_dir)

    dersler = load_program_dersleri(sql_dir)
    generator = ScheduleGenerator()

    jobs = []
    if args.department in ("YZM", "ALL"):
        jobs.append(("YZM", "Yazılım Mühendisliği Haftalık Ders Programı", "output_yazilim.xlsx"))
    if args.department in ("BLM", "ALL"):
        jobs.append(("BLM", "Bilgisayar Mühendisliği Haftalık Ders Programı", "output_bilgisayar.xlsx"))

    for bolum_kodu, baslik, filename in jobs:
        schedule = generator.generate_for_department(dersler, bolum_kodu, baslik)
        path = export_schedule(schedule, output_dir / filename)
        print(f"Oluşturuldu: {path}")


if __name__ == "__main__":
    main()
