
# Yazılım Lab II - Haftalık Ders Programı

Bu proje, **Yazılım Lab II** dersi kapsamında geliştirilmiş haftalık ders programı oluşturma uygulamasıdır. Proje; bölüm, ders, derslik ve öğretim üyesi verilerini kullanarak Yazılım Mühendisliği ve Bilgisayar Mühendisliği için haftalık ders programı Excel çıktıları üretir.

İlk hâlindeki tek dosyalı ve doğrudan veritabanına bağlı yapı, bu sürümde daha düzenli bir Python paket yapısına dönüştürülmüştür. SQL dump dosyaları korunmuş, program oluşturma mantığı modüler hâle getirilmiş ve test edilebilir yapı eklenmiştir.

## Özellikler

- MySQL dump dosyalarından bölüm, ders, derslik ve kullanıcı verilerini okuma
- Yazılım Mühendisliği ve Bilgisayar Mühendisliği için ayrı ders programı oluşturma
- Ortak dersleri ilgili bölüm programlarına dahil etme
- Dersleri dönem bilgisine göre 1, 2, 3 ve 4. sınıf sütunlarına yerleştirme
- Aynı öğretim üyesi ve derslik için aynı zaman diliminde çakışmayı engellemeye çalışma
- Düzenli ve biçimlendirilmiş Excel çıktısı üretme
- Komut satırından bölüm bazlı çıktı alma
- Modüler, okunabilir ve test edilebilir Python proje yapısı

## Proje Yapısı

```text
yazilim-lab-2-haftalik-ders-programi/
├── README.md
├── pyproject.toml
├── .gitignore
├── sql/
│   ├── app_bolum.sql
│   ├── app_dersler.sql
│   ├── app_derslik.sql
│   └── app_kullanici.sql
├── src/
│   └── haftalik_ders_programi/
│       ├── __init__.py
│       ├── cli.py
│       ├── excel_exporter.py
│       ├── models.py
│       ├── mysql_repository.py
│       ├── scheduler.py
│       └── seed_loader.py
└── tests/
    ├── test_excel_exporter.py
    ├── test_scheduler.py
    └── test_seed_loader.py
```

## Kullanılan Teknolojiler

- Python
- openpyxl
- MySQL dump dosyaları
- unittest

## Kurulum

Python 3.10 veya üzeri önerilir.

Proje klasöründe aşağıdaki komut çalıştırılır:

```bash
python -m pip install -e .
```

MySQL bağlantı katmanını da kullanmak isterseniz opsiyonel bağımlılıkla kurulum yapılabilir:

```bash
python -m pip install -e .[mysql]
```

## Çalıştırma

Tüm bölüm programlarını oluşturmak için:

```bash
haftalik-ders-programi --department ALL
```

Sadece Yazılım Mühendisliği programını oluşturmak için:

```bash
haftalik-ders-programi --department YZM
```

Sadece Bilgisayar Mühendisliği programını oluşturmak için:

```bash
haftalik-ders-programi --department BLM
```

Python modülü olarak çalıştırmak için:

```bash
python -m haftalik_ders_programi.cli --department ALL
```

## Giriş Dosyaları

Program varsayılan olarak `sql/` klasöründeki MySQL dump dosyalarını kullanır:

```text
sql/app_bolum.sql
sql/app_dersler.sql
sql/app_derslik.sql
sql/app_kullanici.sql
```

Farklı bir SQL klasörü kullanılacaksa:

```bash
haftalik-ders-programi --sql-dir sql --output-dir outputs --department ALL
```

## Çıktı Dosyaları

Program çalıştırıldığında `outputs/` klasöründe Excel dosyaları oluşturulur:

```text
outputs/output_yazilim.xlsx
outputs/output_bilgisayar.xlsx
```

Bu çıktılar repoya eklenmez; program çalıştırıldığında yeniden üretilebilir.

## Testler

Testleri çalıştırmak için:

```bash
python -m unittest discover -s tests -v
```

Testler; SQL dump okuma, ders programı oluşturma ve Excel dosyası üretme işlemlerinin temel doğruluğunu kontrol eder.

## Geliştirme Notları

Orijinal projede MySQL bağlantısı ve Excel üretimi farklı dosyalarda tekrarlı şekilde bulunuyordu. Güncel sürümde:

- Veri modelleri `models.py` dosyasına ayrıldı.
- SQL dump okuma işlemleri `seed_loader.py` dosyasına alındı.
- Program oluşturma algoritması `scheduler.py` dosyasında toplandı.
- Excel çıktısı üretimi `excel_exporter.py` dosyasına taşındı.
- Komut satırı arayüzü `cli.py` ile ayrı hâle getirildi.
- MySQL bağlantı desteği opsiyonel olarak `mysql_repository.py` içinde korundu.

## Hazırlayanlar

- Gürel BİLGİN
- Gizem YALÇIN
- Berkay ARAS
- Ali AKSOY
