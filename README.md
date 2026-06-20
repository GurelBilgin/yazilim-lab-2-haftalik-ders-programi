
# Yazılım Lab II - Haftalık Ders Programı

Bu proje, **Yazılım Lab II** dersi kapsamında geliştirilmiş haftalık ders programı oluşturma uygulamasıdır. Proje; bölüm, ders, derslik ve öğretim üyesi verilerini kullanarak Yazılım Mühendisliği ve Bilgisayar Mühendisliği için haftalık ders programı Excel çıktıları üretir.

İlk hâlindeki tek dosyalı ve doğrudan veritabanına bağlı yapı, bu sürümde daha düzenli bir Python paket yapısına dönüştürülmüştür. SQL dump dosyaları korunmuş, program oluşturma mantığı modüler hâle getirilmiş ve test edilebilir yapı eklenmiştir.

## Özellikler

- MySQL dump dosyalarından bölüm, ders, derslik ve kullanıcı verilerini okuma
- Yazılım Mühendisliği ve Bilgisayar Mühendisliği için ayrı ders programı oluşturma
- Ortak dersleri ilgili bölüm programlarına dahil etme
- Dersleri dönem bilgisine göre 1, 2, 3 ve 4. sınıf sütunlarına yerleştirme
- Aynı öğretim üyesi ve derslik için aynı zaman diliminde çakışmayı engelleme
- Ders saatlerini mümkün olduğunca aynı gün içinde blok hâlinde yerleştirme
- 3 saatlik dersleri mümkünse arka arkaya 3 saatlik blok olarak planlama
- Tam blok bulunamazsa dersleri daha düzenli 2+1 veya 2+2 bloklara bölme
- Öğretim üyesi alanı `Yönetici` olan derslerde öğretim üyesi bilgisini boş bırakma
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


## Ders Programı Oluşturma Mantığı

Program, SQL dump dosyalarından alınan bölüm, ders, derslik ve öğretim üyesi verilerini kullanarak haftalık ders programı oluşturur. Dersler, ait oldukları bölüm ve dönem bilgilerine göre değerlendirilir; dönem bilgisi 1, 2, 3 ve 4. sınıf sütunlarına dönüştürülür.

Ders yerleştirme sırasında aşağıdaki kurallar uygulanır:

- Aynı öğretim üyesi aynı saat aralığında birden fazla derse atanmaz.
- Aynı derslik aynı saat aralığında birden fazla ders için kullanılmaz.
- Dersin haftalık saatleri mümkün olduğunca aynı gün içinde arka arkaya yerleştirilir.
- 3 saatlik dersler için önce 3 saatlik blok aranır. Uygun blok bulunamazsa 2+1 şeklinde daha düzenli bölünmüş yerleşim denenir.
- 4 saatlik dersler için önce 4 saatlik blok aranır. Uygun blok bulunamazsa 2+2 blok yerleşimi denenir.
- Öğretim üyesi adı `Yönetici` olarak gelen kayıtlar geçici veri kabul edilir ve Excel çıktısında öğretim üyesi satırı boş bırakılır.

Algoritma kural tabanlı ve sıralı yerleştirme mantığıyla çalışır. Amaç, dersleri rastgele dağıtmak yerine çakışmasız, okunabilir ve mümkün olduğunca blok yapıda bir haftalık program üretmektir.

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
- Dersler mümkün olduğunca blok hâlinde yerleştirilecek şekilde zamanlama mantığı geliştirildi.
- `Yönetici` olarak görünen öğretim üyesi kayıtları Excel çıktısında boş bırakılacak şekilde düzenlendi.
- Excel çıktısı üretimi `excel_exporter.py` dosyasına taşındı.
- Komut satırı arayüzü `cli.py` ile ayrı hâle getirildi.
- MySQL bağlantı desteği opsiyonel olarak `mysql_repository.py` içinde korundu.

## Hazırlayan

- Gürel BİLGİN
- Gizem YALÇIN
- Berkay ARAS
- Ali AKSOY