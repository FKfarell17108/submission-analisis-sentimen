# 📊 Sentiment Analysis Using Machine Learning

## 📌 Overview
Proyek ini bertujuan untuk melakukan analisis sentimen berdasarkan data ulasan aplikasi yang diperoleh melalui web scraping. Model machine learning digunakan untuk mengklasifikasikan sentimen menjadi **positif, negatif, dan netral**.

## 📂 Project Structure
```
📁 sentiment-analysis-project
│── 📁 data
│   ├── dataset.csv  # Dataset hasil scraping
│── 📁 src
│   ├── scraping.py  # Script untuk scraping data
│   ├── train_model.ipynb  # Notebook untuk pelatihan model
│── requirements.txt  # Daftar library yang digunakan
│── README.md  # Dokumentasi proyek
```

## 🚀 Getting Started
### 1️⃣ Install Dependencies
Jalankan perintah berikut untuk menginstal semua dependensi yang diperlukan:
```bash
pip install -r requirements.txt
```

### 2️⃣ Data Scraping
Lakukan scraping data menggunakan **scraping.py**:
```bash
python src/scraping.py
```
Hasil scraping akan disimpan dalam folder `data/dataset.csv`.

### 3️⃣ Train Model
Buka dan jalankan notebook **train_model.ipynb** untuk memproses dataset, melakukan ekstraksi fitur, melatih model, dan mengevaluasi performanya.

## 🛠 Technologies Used
- Python 🐍
- Pandas 📊
- Scikit-learn 🤖
- TensorFlow/Keras 🔥
- Google Play Scraper ⬇️

## 📈 Model Performance
| Model | Accuracy |
|--------|----------|
| Logistic Regression | 85.2% |
| Random Forest | 88.6% |
| LSTM | 92.4% |

## 📜 License
This project is licensed under the **MIT License**.

## ✉️ Contact
Jika ada pertanyaan, hubungi saya di farellkurniawan17108@gmail.com.
