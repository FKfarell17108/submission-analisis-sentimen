from google_play_scraper import reviews, Sort
import pandas as pd

# Scraping 4000 review dari aplikasi Duolingo
result, _ = reviews(
    'com.duolingo',  # ID aplikasi Duolingo di Play Store
    lang='en',        # Bahasa Inggris
    country='us',     # Negara US
    sort=Sort.NEWEST, # Urutkan berdasarkan yang terbaru
    count=4000        # Ambil 4000 ulasan
)

# Konversi ke DataFrame
df = pd.DataFrame(result)

# Pilih kolom yang relevan
df = df[['userName', 'score', 'content']]

# Simpan sebagai CSV
df.to_csv('duolingo_reviews.csv', index=False)

print("Scraping selesai! Data tersimpan dalam duolingo_reviews.csv")
