import pandas as pd
import requests
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore")

print("1. 'clothes_data.csv' dosyasından veriler okunuyor...")

try:
    df = pd.read_csv('clothes_data.csv')
except FileNotFoundError:
    print("HATA: clothes_data.csv bulunamadı!")
    exit()

# Veriyi bölme
train_data = []
test_data = []

for i in range(0, len(df), 10):
    chunk = df.iloc[i:i + 10]
    train_data.append(chunk.iloc[:8])
    test_data.append(chunk.iloc[8:])

train_df = pd.concat(train_data)
test_df = pd.concat(test_data)

X_train = train_df[['temp', 'wind', 'precip']]
y_train = train_df['outfit']
X_test = test_df[['temp', 'wind', 'precip']]
y_test = test_df['outfit']

# Modeli Eğitme
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"2. Yapay Zeka Eğitildi!")

# API BAĞLANTISI VE KULLANICI GİRİŞİ
API_KEY = "YOUR_API_KEY"

secilen_sehir = input("🌍 Hangi şehir için öneri istersiniz? (Örn: izmir): ").strip()
secilen_gun = input("📅 Bugün mü, yoksa Yarın için mi öneri istersiniz? (bugün / yarın): ").strip().lower()

print(f"\nVeriler çekiliyor... Şehir: {secilen_sehir.capitalize()}, Zaman: {secilen_gun.capitalize()}")

try:
    if secilen_gun == "yarın" or secilen_gun == "yarin":
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={secilen_sehir}&days=2&aqi=no"
        response = requests.get(url).json()

        # Yarının 24 saatlik verisini listeye alıyoruz
        hourly_data = response['forecast']['forecastday'][1]['hour']

        # Sadece gündüz saatlerini (is_day == 1) filtreliyoruz
        gunduz_saatleri = [saat for saat in hourly_data if saat['is_day'] == 1]

        # Gündüz saatlerinin ortalama sıcaklığı, max rüzgarı ve toplam yağışı
        temp = round(sum(saat['temp_c'] for saat in gunduz_saatleri) / len(gunduz_saatleri), 1)
        wind = max(saat['wind_kph'] for saat in gunduz_saatleri)  # Gündüz çıkabilecek en yüksek rüzgar
        precip = round(sum(saat['precip_mm'] for saat in gunduz_saatleri), 1)

        print(
            f"🌡️ {secilen_sehir.capitalize()} Yarın (Gündüz Ortalaması): {temp}°C, Rüzgar: {wind} km/h, Yağış: {precip} mm")

    else:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={secilen_sehir}&aqi=no"
        response = requests.get(url).json()

        temp = response['current']['temp_c']
        wind = response['current']['wind_kph']
        precip = response['current']['precip_mm']
        print(f"🌡️ {secilen_sehir.capitalize()} Anlık Durum: {temp}°C, Rüzgar: {wind} km/h, Yağış: {precip} mm")

    # YAPAY ZEKA TAHMİNİ
    olasiliklar = model.predict_proba([[temp, wind, precip]])[0]
    siniflar = model.classes_

    uygun_kombinler = [siniflar[i] for i in range(len(siniflar)) if olasiliklar[i] > 0.15]

    if uygun_kombinler:
        secilen_kombin = random.choice(uygun_kombinler)
    else:
        secilen_kombin = model.predict([[temp, wind, precip]])[0]

    print("-" * 40)
    print(f"🤖 YAPAY ZEKA ÖNERİSİ: {secilen_gun.capitalize()} '{secilen_kombin}' giymelisin.")
    print("-" * 40)

except Exception as e:
    print("❌ Bir hata oluştu! Detay:", e)
