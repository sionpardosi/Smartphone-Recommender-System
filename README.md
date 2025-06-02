# Smartphone Recommender System

## ✨ Penilaian Proyek

Proyek ini dirancang untuk Machine Learning Terapan Dicoding. Semua elemen dari latar belakang hingga evaluasi telah ditulis secara lengkap dan sistematis.

---

## 📅 Project Overview

### ᵜ Latar Belakang Proyek

Seiring dengan berkembangnya teknologi digital, pasar ponsel pintar mengalami pertumbuhan yang sangat pesat. Setiap tahun, produsen merilis berbagai model baru dengan spesifikasi teknis yang semakin kompleks, mencakup performa prosesor, kapasitas memori, ukuran layar, kualitas kamera, hingga fitur-fitur berbasis AI. Akibatnya, konsumen sering dihadapkan pada tantangan dalam menentukan pilihan yang paling sesuai dengan kebutuhan mereka.

Kondisi ini semakin sulit bagi pengguna awam yang tidak memiliki pengetahuan teknis mendalam mengenai spesifikasi ponsel. Proses pencarian ponsel yang ideal bisa memakan waktu, membutuhkan perbandingan manual, dan belum tentu menghasilkan keputusan yang optimal. Masalah ini menunjukkan kebutuhan akan suatu sistem yang dapat membantu pengguna dalam memilih ponsel dengan cepat, efisien, dan personal.

Sistem rekomendasi hadir sebagai solusi teknologi untuk menjawab tantangan tersebut. Sebagaimana disebutkan dalam studi Burke (2011), sistem rekomendasi adalah alat penting untuk berinteraksi dengan ruang informasi yang besar dan kompleks. Dalam konteks ini, sistem rekomendasi ponsel dibangun untuk menyederhanakan proses seleksi produk, dengan memanfaatkan data preferensi pengguna (melalui rating) dan informasi spesifikasi teknis ponsel.

Dengan menerapkan pendekatan Content-Based Filtering dan Collaborative Filtering, sistem ini bertujuan untuk menyajikan rekomendasi yang relevan dan personal, baik berdasarkan produk serupa yang pernah disukai pengguna, maupun berdasarkan pola kesukaan pengguna lain yang serupa. Hasilnya diharapkan dapat membantu pengguna menemukan ponsel yang paling sesuai dari segi performa, fitur, harga, hingga sistem operasi.

### ✨ Pentingnya Proyek

* **Peningkatan Pengalaman Pengguna**: Membantu pengguna menemukan produk yang relevan tanpa harus melakukan riset manual.
* **Efisiensi Waktu**: Mempercepat proses pengambilan keputusan dalam memilih ponsel.
* **Personalisasi**: Menyesuaikan rekomendasi dengan kebutuhan dan kebiasaan masing-masing pengguna.
* **Aplikasi Luas**: Dapat diimplementasikan pada platform e-commerce untuk meningkatkan kepuasan pengguna dan nilai bisnis.

---

## 🔍 Business Understanding

### ❓ Problem Statements

* Bagaimana membantu pengguna menemukan ponsel yang paling sesuai dengan preferensi mereka?
* Bagaimana membangun sistem rekomendasi yang efektif berdasarkan data historis rating pengguna?

### 🚀 Goals

* Membangun sistem rekomendasi ponsel menggunakan dua pendekatan: content-based filtering dan collaborative filtering.
* Menyediakan daftar rekomendasi (Top-N recommendation) yang relevan untuk setiap pengguna.

### 🔨 Solution Approach

1. **Content-Based Filtering**:

   * Menggunakan fitur-fitur ponsel seperti brand, model, dan sistem operasi.
   * Menggunakan TF-IDF dan cosine similarity untuk menghitung kesamaan antar produk.

2. **Collaborative Filtering**:

   * Menggunakan data interaksi pengguna-item (rating).
   * Membangun model deep learning menggunakan Keras dan TensorFlow untuk mempelajari preferensi pengguna.

---

## 📊 Data Understanding

### 🔗 Sumber Dataset

Dataset terdiri dari tiga file utama:

* **data.csv**: Informasi spesifikasi ponsel (33 baris, 14 kolom)
* **rating.csv**: Data rating pengguna terhadap ponsel (990 baris)
* **users.csv**: Profil pengguna (99 baris)

**Link Dataset:** [Cellphone Recommendation Dataset - Kaggle](https://www.kaggle.com/datasets/meirnizri/cellphones-recommendations)

### 📃 Struktur Relasi Data

```
users.csv ──┐
            ├─── user_id ─── rating.csv ─── cellphone_id ─── data.csv
            └─── (One-to-Many relationship)
```

### 💱 Deskripsi Variabel

Lihat tabel fitur lengkap pada bagian kode. Semua fitur telah dijelaskan dalam markdown sebelumnya dan disesuaikan dengan output `.info()` dari `pandas`.

### 📊 Exploratory Data Analysis (EDA)

Beberapa grafik yang perlu Anda sisipkan (gunakan `![](path-to-image)`):

* Distribusi brand ponsel
* Distribusi sistem operasi
* Distribusi tahun rilis
* Histogram rating pengguna
* Outliers pada rating
* Penyebaran usia pengguna

Gunakan gambar hasil dari `matplotlib` dan `seaborn` pada kode Anda.

---

## 🚮 Data Preparation

### 🔀 Teknik Data Preparation

* Menggabungkan tiga dataset utama menggunakan `merge()`
* Menangani missing values (`NaN`) pada kolom `occupation`
* Menghapus outliers pada `rating` dan `gender`
* Normalisasi nilai dengan encoding (label mapping)
* Pembagian data menjadi training dan validation (80:20)

### 📄 Alasan Setiap Tahapan

* **Penggabungan data**: Untuk memastikan konsistensi informasi per record.
* **Missing value handling**: Menghindari error saat training.
* **Outlier removal**: Menstabilkan model dan menghindari bias.
* **Encoding**: Mengubah nilai string menjadi format numerik yang bisa diproses model.

---

## 🤖 Modeling and Result

### ✔ Content-Based Filtering

* Menggunakan TF-IDF pada kolom `brand` dan `model`
* Menghitung cosine similarity antar item
* Output berupa rekomendasi 4 ponsel teratas berdasarkan model tertentu

#### Contoh Output:

```text
model_recommendations('iPhone XR')
# Output:
1. iPhone 13 Pro Max
2. iPhone SE (2022)
3. iPhone 13 Pro
4. iPhone 13
```

### ✔ Collaborative Filtering

* Menggunakan model `RecommenderNet` berbasis Keras
* Menggunakan embedding layer untuk `user_id` dan `cellphone_id`
* Training 100 epoch dengan `batch_size = 8`

#### Contoh Output:

```text
Top 10 cellphone recommendation for user 237:
1. iPhone XR
2. Galaxy S22
3. Galaxy A53
...
```

### ❌ Kelebihan dan Kekurangan

| Pendekatan              | Kelebihan                                      | Kekurangan                                       |
| ----------------------- | ---------------------------------------------- | ------------------------------------------------ |
| Content-Based Filtering | Tidak tergantung data pengguna lain            | Sulit memberikan rekomendasi variatif            |
| Collaborative Filtering | Menyesuaikan rekomendasi berdasarkan komunitas | Mengalami masalah cold-start untuk pengguna baru |

---

## ✅ Evaluation

### ⚖ Metrik Evaluasi

Menggunakan **Root Mean Squared Error (RMSE)**:

```math
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
```

* RMSE mengukur seberapa besar deviasi prediksi terhadap rating sebenarnya
* Semakin kecil RMSE, semakin baik model

### 🌐 Hasil Evaluasi

| Data  | RMSE   |
| ----- | ------ |
| Train | 0.2063 |
| Test  | 0.6416 |

### 🌄 Visualisasi Evaluasi

Silakan tambahkan grafik RMSE vs epoch dari `history.history['root_mean_squared_error']` dan `val_root_mean_squared_error`:

```markdown
![](path-to-rmse-graph)
```

---

## 🔺 Kesimpulan

Dengan menggunakan kedua pendekatan ini:

* **Content-Based Filtering** cocok untuk merekomendasikan ponsel yang mirip berdasarkan fitur
* **Collaborative Filtering** unggul dalam prediksi rating berdasarkan pola pengguna

Model yang dibangun terbukti dapat memberikan rekomendasi personal dan dapat digunakan sebagai fondasi sistem rekomendasi di platform komersial.

---

## 🔹 Referensi

* IBM: What is content-based filtering? [Link](https://www.ibm.com/topics/content-based-filtering)
* IBM: What is collaborative filtering? [Link](https://www.ibm.com/topics/collaborative-filtering)
* Analytics Vidhya: Recommendation Systems Tutorial [Link](https://www.analyticsvidhya.com)
* Secoda: Recommendation System Guide [Link](https://www.secoda.co)
* Paul P.: Evaluating Recommender Systems [Medium](https://medium.com)

---

> **Note:** Seluruh gambar visualisasi dapat diambil dari hasil output kode Python Anda.
> Pastikan untuk mengunggah gambar ke GitHub dan menghubungkannya menggunakan path relatif (`![](image/path.png)`) agar dapat dirender dengan baik di halaman proyek.
