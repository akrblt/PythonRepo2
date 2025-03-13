import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ Excel dosyasını oku
dosya_yolu = "C:/Users/pr08glt/Desktop/Module 1/PythonRepo2/ICT_164/xlsx/teachers.xlsx"  # Dosyanızın yolunu buraya yazın
df = pd.read_excel(dosya_yolu)

print("Excel dosyası başarıyla okundu!")
print(df.head())

# 2️⃣ MySQL veritabanına bağlanma
kullanici = "root"          # MySQL kullanıcı adınız
parola = "root"            # MySQL şifreniz
host = "localhost"          # Sunucu adresi (genellikle localhost)
veritabani = "school"     # Veritabanı adı

# Bağlantı oluştur
engine = create_engine(f"mysql+pymysql://{kullanici}:{parola}@{host}/{veritabani}")

print("Veritabanına bağlandı!")

# 3️⃣ Veriyi MySQL’e aktarma
tablo_adi = "teachers"  # MySQL'deki tablo adı
df.to_sql(tablo_adi, con=engine, if_exists='append', index=False)

print(f"Veriler {tablo_adi} tablosuna başarıyla aktarıldı!")

# 4️⃣ Verilerin doğru aktarılıp aktarılmadığını kontrol etme
sorgu = f"SELECT * FROM {tablo_adi} LIMIT 5"
sonuclar = pd.read_sql(sorgu, con=engine)

print("Tablodan çekilen veriler:")
print(sonuclar)

# Bağlantıyı kapatma (opsiyonel)
engine.dispose()
