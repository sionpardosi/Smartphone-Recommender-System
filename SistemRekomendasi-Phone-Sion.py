# %% [markdown]
# # **SISTEM REKOMENDASI PONSEL PINTAR BERDASARKAN PREFERENSI PENGGUNA**

# %% [markdown]
# - **Nama:** Sion Saut Parulian Pardosi
# - **Email:** spardosi12@gmail.com
# - **Email Dicoding:** mc114d5y1919@student.devacademy.id
# - **ID Dicoding:** MC114D5Y1919

# %% [markdown]
# -- -

# %% [markdown]
# ## **Deskripsi Proyek**
# 
# ### **Deskripsi Latar Belakang Proyek**
# 
# Dengan pesatnya perkembangan teknologi, pasar ponsel pintar mengalami pertumbuhan yang signifikan dengan berbagai pilihan model yang tersedia. Konsumen sering menghadapi kesulitan dalam menentukan ponsel yang tepat karena banyaknya opsi yang ada. Kompleksitas spesifikasi teknis dan beragamnya fitur membuat proses pemilihan menjadi menantang, terutama bagi pengguna awam yang tidak memahami detail teknis.
# Sistem rekomendasi merupakan solusi untuk berinteraksi dengan ruang informasi yang besar dan kompleks. Proyek ini mengembangkan sistem rekomendasi yang dapat menyederhanakan proses pemilihan ponsel dengan memberikan rekomendasi yang relevan berdasarkan preferensi dan kebutuhan pengguna. Dengan memanfaatkan data rating pengguna dan spesifikasi teknis ponsel, sistem ini diharapkan dapat membantu pengguna menemukan ponsel yang paling sesuai dengan kebutuhan mereka.
# 
# ### **Tujuan Proyek**
# 
# - Mengembangkan sistem rekomendasi ponsel yang dapat memberikan saran berdasarkan preferensi pengguna
# - Membantu pengguna menemukan ponsel yang mirip dengan perangkat sebelumnya
# - Meningkatkan pengalaman pengguna dalam proses pemilihan ponsel
# - Mengimplementasikan dua pendekatan: Content-Based Filtering dan Collaborative Filtering

# %% [markdown]
# ## #

# %% [markdown]
# ## 1. Import Library yang Dibutuhkan

# %% [markdown]
# Mengimpor semua library yang diperlukan untuk pengembangan sistem rekomendasi.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import library untuk machine learning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Import library untuk deep learning
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Import library untuk sistem file
from pathlib import Path
import os

# Pengaturan untuk visualisasi
plt.style.use('default')
sns.set_palette("husl")

# %% [markdown]
# ## #

# %% [markdown]
# ## 2. Data Understanding

# %% [markdown]
# #### Persiapan Dataset
# 
# Dataset yang digunakan terdiri dari 3 file CSV yang berisi informasi lengkap tentang ponsel, rating pengguna, dan profil pengguna.

# %%
# Menentukan path dataset
dataset_path = r"D:\PROJECT\DBS DICODING\machine learning terapan\sistem rekomendasi\Dicoding-ModelSistemRekomendasi-main\dataset"

# Memverifikasi keberadaan file
data_file = os.path.join(dataset_path, "cellphones data.csv")
rating_file = os.path.join(dataset_path, "cellphones ratings.csv")
users_file = os.path.join(dataset_path, "cellphones users.csv")

# Mengecek apakah file ada
files_to_check = [data_file, rating_file, users_file]
file_names = ["cellphones data.csv", "cellphones ratings.csv", "cellphones users.csv"]

print("Verifikasi keberadaan file:")
for file, name in zip(files_to_check, file_names):
    if os.path.exists(file):
        print(f"✓ {name} - Tersedia")
    else:
        print(f"✗ {name} - Tidak ditemukan")
        print(f"  Path yang dicari: {file}")

# %% [markdown]
# #### Membaca Dataset

# %%
try:
    # Membaca dataset dengan error handling
    print("Memuat dataset...")
    
    data = pd.read_csv(data_file)
    rating = pd.read_csv(rating_file)
    users = pd.read_csv(users_file)
    
    print("✓ Semua dataset berhasil dimuat!")
    print(f"✓ Data ponsel: {data.shape[0]} baris, {data.shape[1]} kolom")
    print(f"✓ Data rating: {rating.shape[0]} baris, {rating.shape[1]} kolom")
    print(f"✓ Data pengguna: {users.shape[0]} baris, {users.shape[1]} kolom")
    
except FileNotFoundError as e:
    print(f"Error: File tidak ditemukan - {e}")
    print("Pastikan path dataset sudah benar dan file tersedia")
except Exception as e:
    print(f"Error tidak terduga: {e}")

# %% [markdown]
# #### Struktur Dataset

# %% [markdown]
# Dataset terbagi menjadi 3 komponen utama:
# 
# 1. Cellphones Data (data.csv)
# 
# - Berisi spesifikasi lengkap dari 33 model ponsel
# - Informasi meliputi brand, model, sistem operasi, dan spesifikasi teknis
# 
# 
# 2. Cellphones Ratings (rating.csv)
# 
# - Berisi 990 data rating yang diberikan pengguna terhadap ponsel
# - Rating dalam skala 1-10
# 
# 
# 3. Cellphones Users (users.csv)
# 
# - Berisi profil 99 pengguna
# - Informasi demografis seperti usia, gender, dan pekerjaan

# %%
# Menampilkan informasi detail dataset
print("=== INFORMASI DATASET PONSEL ===")
print(data.info())
print("\n=== SAMPLE DATA PONSEL ===")
print(data.head())

print("\n=== INFORMASI DATASET RATING ===")
print(rating.info())
print("\n=== SAMPLE DATA RATING ===")
print(rating.head())

print("\n=== INFORMASI DATASET PENGGUNA ===")
print(users.info())
print("\n=== SAMPLE DATA PENGGUNA ===")
print(users.head())

# %% [markdown]
# Membaca file .csv dan menyimpannya pada suatu variabel.

# %%
import os

# Path ke folder dataset
dataset_path = r"D:\PROJECT\DBS DICODING\machine learning terapan\sistem rekomendasi\Dicoding-ModelSistemRekomendasi-main\dataset"

# Pindah ke direktori dataset
os.chdir(dataset_path)

# Mengubah nama file menggunakan os.rename()
try:
    os.rename("cellphones data.csv", "data.csv")
    print("✓ cellphones data.csv → data.csv")
except FileNotFoundError:
    print("⚠ File 'cellphones data.csv' tidak ditemukan atau sudah diubah")
except FileExistsError:
    print("⚠ File 'data.csv' sudah ada")

try:
    os.rename("cellphones ratings.csv", "rating.csv")
    print("✓ cellphones ratings.csv → rating.csv")
except FileNotFoundError:
    print("⚠ File 'cellphones ratings.csv' tidak ditemukan atau sudah diubah")
except FileExistsError:
    print("⚠ File 'rating.csv' sudah ada")

try:
    os.rename("cellphones users.csv", "users.csv")
    print("✓ cellphones users.csv → users.csv")
except FileNotFoundError:
    print("⚠ File 'cellphones users.csv' tidak ditemukan atau sudah diubah")
except FileExistsError:
    print("⚠ File 'users.csv' sudah ada")

# Hapus file zip jika ada
try:
    os.remove("dataset.zip")
    print("✓ dataset.zip dihapus")
except FileNotFoundError:
    print("⚠ File 'dataset.zip' tidak ditemukan")

print("\nFile berhasil diubah! Sekarang Anda bisa membaca dengan:")
print("data = pd.read_csv('data.csv')")
print("rating = pd.read_csv('rating.csv')")
print("users = pd.read_csv('users.csv')")

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan informasi dari dataset menggunakan .info()

# %%
#Menampilkan info dari dataset
data.info()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Total baris ada 33
# - Total kolom ada 14
# - Terdapat 10 kolom bertipe data numerik
# - Terdapat 4 kolom bertipe data object
# 

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan 5 sampel teratas dari varibel data.

# %%
data.head()

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan informasi dari dataset menggunakan .info()

# %%
rating.info()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Total baris ada 990
# - Total kolom ada 3
# - Terdapat 3 kolom bertipe data numerik

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan 5 sampel teratas dari varibel rating.

# %%
rating.head()

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan informasi dari dataset menggunakan .info()

# %%
#Menampilkan info dari dataset
users.info()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Total baris ada 99
# - Total kolom ada 4
# - Terdapat 2 kolom bertipe data numerik
# - Terdapat 2 kolom bertipe data object

# %% [markdown]
# ####

# %% [markdown]
# #### Menampilkan 5 sampel teratas dari varibel users.

# %%
#Menampilkan isi dari variabel users
users.head()

# %% [markdown]
# ## Univariate Exploratory Data Analysis

# %% [markdown]
# ## Overview
# Dataset ini terdiri dari tiga file CSV yang berisi informasi mengenai ponsel, rating pengguna, dan profil pengguna untuk sistem rekomendasi ponsel.
# 
# ## File Structure
# 
# ### 📱 data.csv (Informasi Ponsel)
# File ini berisi informasi detail mengenai spesifikasi dan karakteristik ponsel.
# 
# | Variabel | Tipe Data | Deskripsi |
# |----------|-----------|-----------|
# | `cellphone_id` | Integer | Identifikasi unik untuk setiap unit ponsel |
# | `brand` | String | Nama merek atau brand ponsel |
# | `model` | String | Tipe atau model spesifik ponsel |
# | `operating_system` | String | Jenis sistem operasi yang digunakan |
# | `internal_memory` | Integer | Kapasitas penyimpanan internal dalam satuan GB |
# | `RAM` | Integer | Kapasitas memori akses acak dalam satuan GB |
# | `performance` | Float | Nilai evaluasi performa ponsel |
# | `main_camera` | Integer | Kualitas kamera belakang dalam satuan MP |
# | `selfie_camera` | Integer | Kualitas kamera depan dalam satuan MP |
# | `battery_size` | Integer | Daya tampung baterai dalam satuan mAh |
# | `screen_size` | Float | Dimensi layar dalam satuan inci |
# | `weight` | Integer | Bobot ponsel dalam satuan gram |
# | `price` | Float | Nilai harga ponsel dalam mata uang USD |
# | `release_date` | Date | Waktu peluncuran produk ponsel |
# 
# ### ⭐ rating.csv (Penilaian Pengguna)
# File ini berisi data rating yang diberikan pengguna terhadap ponsel tertentu.
# 
# | Variabel | Tipe Data | Deskripsi |
# |----------|-----------|-----------|
# | `user_id` | Integer | Kode identifikasi unik setiap pengguna |
# | `cellphone_id` | Integer | Kode identifikasi unik ponsel (terhubung dengan data.csv) |
# | `rating` | Integer | Nilai penilaian yang diberikan pengguna terhadap ponsel (rentang 1-10) |
# 
# ### 👤 users.csv (Profil Pengguna)
# File ini berisi informasi demografis pengguna.
# 
# | Variabel | Tipe Data | Deskripsi |
# |----------|-----------|-----------|
# | `user_id` | Integer | Kode identifikasi unik setiap pengguna |
# | `age` | Integer | Umur pengguna |
# | `gender` | String | Jenis kelamin pengguna |
# | `occupation` | String | Profesi atau pekerjaan pengguna |
# 
# ## Relationships
# 
# ```
# users.csv ──┐
#             │
#             ├─── user_id ─── rating.csv ─── cellphone_id ─── data.csv
#             │
#             └─── (One-to-Many relationship)
# ```
# 
# - **users.csv** dan **rating.csv** terhubung melalui `user_id`
# - **rating.csv** dan **data.csv** terhubung melalui `cellphone_id`
# - Satu pengguna dapat memberikan rating untuk beberapa ponsel
# - Satu ponsel dapat memiliki rating dari beberapa pengguna

# %% [markdown]
# ## **Dataset Data**

# %% [markdown]
# #### Menampilkan satu contoh dari dataset data

# %%
#Menampilkan satu contoh
data.head(1)

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah cellphone masing-masing brand dan menampilkan grafik.

# %%
#Menghitung jumlah brand
print('Jumlah brand: ',len(data.brand.unique()))

#Menghitung jumlah cellphone masing-masing brand
brand_counts = data['brand'].value_counts()
print(brand_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['brand'])
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 10 brand berbeda
# - Brand dengan jumlah cellphone paling banyak adalah Samsung
# - Brand dengan jumlah cellphone paling sedikit adalah Asus, Oppo, Vivo, dan Sony

# %% [markdown]
# #### 

# %% [markdown]
# #### Menampilkan jenis-jenis model cellphone.

# %%
#Menampilkan semua model cellphone
model_counts = data['model'].unique()
print('Jumlah model cellphone: ',len(model_counts))
model_counts

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 33 model cellphone berbeda

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah operating system untuk masing-masing kategori.

# %%
#Menghitung jumlah operating system
os_counts = data['operating system'].value_counts()
print(os_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['operating system'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat dua kategori operating system
# - Android memiliki jumlah terbanyak dengan total 27

# %% [markdown]
# #### 
# 

# %% [markdown]
# #### Menghitung jumlah internal memory untuk masing-masing kategori.

# %%
#Menghitung jumlah internal memory
internalMemory_counts = data['internal memory'].value_counts()
print(internalMemory_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['internal memory'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat lima kategori internal memory
# - Kategori internal memory 128 memiliki jumlah terbanyak dengan total 20
# - Kategori internal memory 512 memiliki jumlah tersedikit dengan total 1

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah RAM untuk masing-masing kategori.

# %%
#Menghitung jumlah RAM
RAM_counts = data['RAM'].value_counts()
print(RAM_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['RAM'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat lima kategori RAM
# - Kategori RAM 8 memiliki jumlah terbanyak dengan total 13
# - Kategori RAM 3 dan RAM 12 memiliki jumlah tersedikit dengan total 4

# %% [markdown]
# #### 

# %% [markdown]
# #### Menampilkan analisis untuk kolom performance. Analisis dilakukan dengan membagi performance menjadi dua kategori karena nilai yang dimiliki sangat beragam.

# %%
#Filter data berdasarkan performance
performance_above_5 = data[data['performance'] > 5]
performance_below_5 = data[data['performance'] <= 5]

#Menghitung total untuk setiap kategori
total_above_5 = len(performance_above_5)
total_below_5 = len(performance_below_5)

print('Total data dengan performance > 5:', total_above_5)
print('Total data dengan performance <= 5:', total_below_5)

#Data untuk plotting
performance_data = pd.DataFrame({
    'Category': ['Performance > 5', 'Performance <= 5'],
    'Total': [total_above_5, total_below_5]
})

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Total', data=performance_data)
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Cellphones yang memiliki performance lebih dari lima ada 23
# - Cellphones yang memiliki performance kurang dari lima ada 10

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah main camera untuk masing-masing kategori.

# %%
#Menghitung jumlah main camera
mainCamera_counts = data['main camera'].value_counts()
print(mainCamera_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['main camera'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat enam kategori main camera
# - Kategori main camera 50 memiliki jumlah terbanyak dengan total 13
# - Kategori main camera 13, 48, 108 memiliki jumlah tersedikit dengan total 2

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah battery size.

# %%
#Menghitung jumlah battery size
batterySize_counts = data['battery size'].value_counts()
print(batterySize_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(15, 3))
sns.countplot(data=data, x=data['battery size'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 18 kategori battery size
# - kategori battery size 5000 memiliki jumlah terbanyak dengan total 11

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah screen size.

# %%
#Menghitung jumlah screen size
screenSize_counts = data['screen size'].value_counts()
print(screenSize_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data['screen size'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat sepuluh kategori screen size
# - Kategori screen size 6.7 memiliki jumlah terbanyak dengan total 8

# %% [markdown]
# #### 

# %% [markdown]
# #### Menghitung jumlah weight.

# %%
#Menghitung jumlah weight
weight_counts = data['weight'].value_counts()
print(len(weight_counts))
print(weight_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(15, 3))
sns.countplot(data=data, x=data['weight'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 27 kategori weight
# - Kategori weight 204 memiliki jumlah terbanyak dengan total 5

# %% [markdown]
# #### 

# %% [markdown]
# #### Melakukan analisis kolom release date dengan membagi data berdasarkan tahun.

# %%
#Mengcopy dataset original
data_new = data.copy()

#Konversi kolom 'release date' ke tipe datetime
data_new['release date'] = pd.to_datetime(data['release date'], format='%d/%m/%Y')

# Ekstraksi tahun rilis
data_new['release_year'] = data_new['release date'].dt.year

# Hitung jumlah rilis per tahun
release_counts = data_new['release_year'].value_counts().sort_index()

print(release_counts)

#Menampilkan dalam bentuk grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=data, x=data_new['release_year'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat tiga kategori tahun
# - Tahun 2025 memiliki jumlah terbanyak dengan total 16
# - Tahun 2018 memiliki jumlah tersedikit dengan total 1

# %% [markdown]
# **Rating**

# %% [markdown]
# Mencari tahu masing-masing user melakukan review berapa kali dan mencari tahu apakah ada user yang melakukan jumlah review berbeda dari user lainnya.

# %%
#Menghitung masing-masing user melakukan review berapa kali
user_review_counts = rating['user_id'].value_counts()
print(user_review_counts)

#Mencari nilai unik untuk mencari tahu apakah ada user yang memiliki nilai berbeda
print("\n",user_review_counts.unique())

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Masing-masing user melakukan review sebanyak sepuluh kali
# - Semua user memiliki jumlah review yang sama yaitu sepuluh

# %% [markdown]
# Menghitung jumlah kemunculan cellphone yang diriview.

# %%
#Menghitung cellphone dengan id X muncul berapa kali
cellphone_review_counts = rating['cellphone_id'].value_counts()
print("\nJumlah kemunculan per cellphone_id:\n", cellphone_review_counts.sort_index())

#Menghitung nilai minimum dan maximum
print("\nMinimum:", cellphone_review_counts.min())
print("Maximum:", cellphone_review_counts.max())

#Menampilkan grafik
plt.figure(figsize=(15, 3))
sns.countplot(data=rating, x=rating['cellphone_id'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Cellphone paling banyak direview sebanyak 41 kali
# - Cellphone paling sedikit direview sebanyak 20 kali

# %% [markdown]
# Menghitung jumlah rating.

# %%
#Menghitung rating X muncul berapa kali
rating_counts = rating['rating'].value_counts()
print("\nJumlah kemunculan per rating:\n", rating_counts.sort_index())

#Menampilkan grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=rating, x=rating['rating'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Rating memiliki skala 0 - 10
# - Rating terbanyak dengan nilai 8
# - Rating tersedikit dengan nilai 3
# - Terdapat outliers yaitu rating dengan nilai 18

# %% [markdown]
# **User**

# %%
#Menghitung age X muncul berapa kali
age_counts = users['age'].value_counts()
print("\nJumlah kemunculan age:\n", age_counts.sort_index())

#Menampilkan grafik
plt.figure(figsize=(10, 3))
sns.countplot(data=users, x=users['age'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Usia paling tua dari user adalah 61
# - Usia paling muda dari user adalah 21
# - User dengan usia 25 memiliki jumlah paling banyak yaitu 12

# %% [markdown]
# Menghitung jumlah masing-masing kategori gender.

# %%
#Menghitung gender X muncul berapa kali
users_counts = users['gender'].value_counts()
print("\nJumlah kemunculan gender:\n", users_counts.sort_index())

#Menampilkan grafik
plt.figure(figsize=(5, 3))
sns.countplot(data=users, x=users['gender'])
plt.show()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Gender female memiliki jumlah 46
# - Gender male memiliki jumlah 50
# - Terdapat outliers yaitu `-Select Gender-`

# %% [markdown]
# Menghitung jumlah occupation X muncul berapa kali.

# %%
#Menghitung occupation X muncul berapa kali
occupation_counts = users['occupation'].str.lower().value_counts()
print('Jumlah occupation: ',len(occupation_counts))
print("\nJumlah kemunculan occupation:\n", occupation_counts.sort_index())

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 45 jenis pekerjaan
# - Terdapat kesalahan penulisan pada `healthare`
# - Pekerjaan `information technology` dan `it` dapat dijadikan satu

# %% [markdown]
# ####

# %% [markdown]
# ## Data Preprocessing

# %% [markdown]
# Menggabungkan dataset data, rating, dan users menjadi satu.

# %%
#Gabungkan cellphones_ratings dengan cellphones_data
ratings_data = pd.merge(rating, data, on='cellphone_id')

#Gabungkan hasil dengan cellphones_users
merged_data = pd.merge(ratings_data, users, on='user_id')

#Menampilkan dataset hasil merged
merged_data.head()

# %% [markdown]
# Melakukan cek missing value.

# %%
#Cek missing value
merged_data.isnull().sum()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat 10 missing value pada occupation

# %% [markdown]
# Menampilkan isi dari baris yang memiliki missing value.

# %%
#Menampilkan baris yang memiliki nilai null
rows_with_null = merged_data[merged_data.isnull().any(axis=1)]
print(rows_with_null)

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Seperti yang ditemukan saat univariate analysis bahwa terdapat outlier pada kolom gender yaitu `-Select Gender-` yang ternyata berhubungan dengan nilai occupation NaN
# - Akan dilakukan drop

# %% [markdown]
# ####

# %% [markdown]
# #### Drop missing value.

# %%
#Menghapus missing value
merged_data = merged_data.dropna()

# %% [markdown]
# ####
# 

# %% [markdown]
# Memastikan bahwa tidak terdapat missing value lagi.

# %%
#Cek missing value
merged_data.isnull().sum()

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Sudah tidak terdapat missing value.

# %% [markdown]
# Berdasarkan univariate analysis terdapat outlier pada kolom rating, terdapat kesalahan tulis pada kolom occupation dan terdapat penyamaan nama pekerjaan pada kolom occupation.

# %%
#Drop rating 18
merged_data = merged_data[merged_data['rating'] != 18]

#Mengubah seluruh value occupation menjadi lowercase
merged_data['occupation'] = merged_data['occupation'].str.lower()

#Mengubah value 'healthare' pada kolom "occupation" menjadi 'healthcare'
merged_data['occupation'] = merged_data['occupation'].replace('healthare', 'healthcare')

#Mengubah value 'it' pada kolom "occupation" menjadi 'information technology'
merged_data['occupation'] = merged_data['occupation'].replace('it', 'information technology')

# %% [markdown]
# Menampilkan dataset yang sudah dibersihkan.

# %%
#Menampilkan dataset
cleaned_data = merged_data
cleaned_data

# %% [markdown]
# ####

# %% [markdown]
# # Data Preparation

# %% [markdown]
# Menghapus data duplikat sehingga cellphone hanya muncul satu kali.

# %%
#Menghapus data duplikat
cleaned_data = cleaned_data.drop_duplicates('cellphone_id')

# %% [markdown]
# Melakukan konversi data series menjadi list.

# %%
#Melakukan konversi data series menjadi list
cellphone_id = cleaned_data['cellphone_id'].tolist()
brand = cleaned_data['brand'].tolist()
model = cleaned_data['model'].tolist()
operating_system = cleaned_data['operating system'].tolist()

print(len(cellphone_id))
print(len(brand))
print(len(model))
print(len(operating_system))

# %% [markdown]
# Membuat dictionary untuk menentukan pasangan key-value.
# 
# Karena TF-IDF hanya cocok untuk data teks maka hanya kolom yang bertipe object saja yang dipilih.

# %%
#Membuat dictionary untuk menentukan pasangan key-value
phone_new = pd.DataFrame({
    'cellphone_id': cellphone_id,
    'brand': brand,
    'model': model,
    'operating_system': operating_system,
})

phone_new

# %% [markdown]
# #Model Development Dengan Content Based Filtering

# %% [markdown]
# Melakukan assign dataframe ke variabel baru yaitu data.

# %%
#Assign dataframe phone_new ke variabel data
data = phone_new

# %% [markdown]
# Membangun sistem rekomendasi.

# %%
#Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

#Melakukan perhitungan idf pada data brand
tf.fit(data['brand'])

#Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# %% [markdown]
# Melakukan fit dan transformasi ke bentuk matriks.

# %%
#Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['brand'])

#Melihat ukuran matrix tfidf
tfidf_matrix.shape

# %% [markdown]
# Menghasilkan vektor TF-IDF dalam bentuk matriks.

# %%
#Menghasilkan vektor TF-IDF dalam bentuk matriks.
tfidf_matrix.todense()

# %% [markdown]
# Melihat matriks TF-IDF untuk beberapa model dan brand.

# %%
#Menampilkan matriks TF-IDF untuk beberapa model dan brand.
pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.model
).sample(10, axis=1).sample(10, axis=0)

# %% [markdown]
# Menghitung derajat kesamaan (similarity degree) antar model dengan teknik cosine similarity.

# %%
#Menampilkan cosine_similatiry
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# %% [markdown]
# Matriks kesamaan setiap model dengan menampilkan nama model dalam 33 sampel kolom (axis = 1) dan 10 sampel baris (axis=0).

# %%
#Membuat dataframe dari variabel cosine_sim
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['model'], columns=data['model'])
print('Shape:', cosine_sim_df.shape)

#Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(33, axis=1).sample(10, axis=0)

# %% [markdown]
# Membuat fungsi model_recommendations

# %%
def model_recommendations(model, similarity_data=cosine_sim_df, items=phone_new[['model','brand','operating_system']], k=4):
    #Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    #Dataframe diubah menjadi numpy
    #Range(start, stop, step)
    index = similarity_data.loc[:,model].to_numpy().argpartition(
        range(-1, -k, -1))

    #Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_model agar nama model yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(model, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

# %% [markdown]
# Menampilkan hasil rekomendasi untuk `iPhone XR`

# %%
#Menampilkan hasil rekomendasi
model_recommendations('iPhone XR')

# %% [markdown]
# Menampilkan hasil rekomendasi untuk `Galaxy S22`

# %%
#Menampilkan hasil rekomendasi
model_recommendations('Galaxy S22')

# %% [markdown]
# ####

# %% [markdown]
# # Model Model Development dengan Collaborative Filtering

# %% [markdown]
# Menyimpan dataset rating yang sudah pernah diread di variabel df.

# %%
#Membaca dataset
df = rating
df

# %% [markdown]
# Menyandikan (encode) fitur user_id.

# %%
#Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = df['user_id'].unique().tolist()
print('list userID: ', user_ids)

#Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

#Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

# %% [markdown]
# Menyandikan (encode) fitur cellphone_id.

# %%
#Mengubah cellphone_id menjadi list tanpa nilai yang sama
cellphone_ids = df['cellphone_id'].unique().tolist()

#Melakukan proses encoding cellphone_id
cellphone_to_cellphone_encoded = {x: i for i, x in enumerate(cellphone_ids)}

#Melakukan proses encoding angka ke cellphone_id
cellphone_encoded_to_cellphone = {i: x for i, x in enumerate(cellphone_ids)}

# %% [markdown]
# Mapping user_id dan cellphone_id.

# %%
#Mapping user_id ke dataframe user
df['user'] = df['user_id'].map(user_to_user_encoded)

#Mapping cellphone_id ke dataframe cellphone
df['cellphone'] = df['cellphone_id'].map(cellphone_to_cellphone_encoded)

# %% [markdown]
# Menampilkan jumlah user dan cellphone.
# 
# Menampilkan nilai minimum dan maximum dari rating.

# %%
#Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

#Mendapatkan jumlah cellphone
num_cellphone = len(cellphone_to_cellphone_encoded)
print(num_cellphone)

#Mengubah rating menjadi nilai float
df['rating'] = df['rating'].values.astype(np.float32)

#Nilai minimum rating
min_rating = min(df['rating'])

#Nilai maksimal rating
max_rating = max(df['rating'])

print('Number of User: {}, Number of cellphone: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_cellphone, min_rating, max_rating
))

# %% [markdown]
# Output kode di atas memberikan informasi :
# - Terdapat outliers pada fitur rating yaitu value '18'
# - Outlier tersebut harus di drop

# %% [markdown]
# Drop baris dengan value pada kolom rating 18.

# %%
#Drop data
df = df[df['rating'] != 18]

# %% [markdown]
# Memastikan kembali tidak ada nilai max yang melebihi 10.

# %%
#Nilai minimum rating
min_rating = min(df['rating'])

#Nilai maksimal rating
max_rating = max(df['rating'])

print('Min Rating: {}, Max Rating: {}'.format(
    min_rating, max_rating
))

# %% [markdown]
# Melakukan acak terhadap dataset.

# %%
#Mengacak dataset
df = df.sample(frac=1, random_state=42)
df

# %% [markdown]
# #### Memetakan (mapping) data user dan cellphone menjadi satu value.
# 
# Mebagi data train dan validasi dengan komposisi 80:20.

# %%
#Membuat variabel x untuk mencocokkan data user dan cellphone menjadi satu value
x = df[['user', 'cellphone']].values

#Membuat variabel y untuk membuat rating dari hasil
y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

#Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

# %% [markdown]
# Membuat class recommenderNet.

# %%
import tensorflow as tf
class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_cellphone, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_cellphone = num_cellphone
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.cellphone_embedding = layers.Embedding( # layer embeddings cellphone
        num_cellphone,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.cellphone_bias = layers.Embedding(num_cellphone, 1) # layer embedding cellphone bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    cellphone_vector = self.cellphone_embedding(inputs[:, 1]) # memanggil layer embedding 3
    cellphone_bias = self.cellphone_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_cellphone = tf.tensordot(user_vector, cellphone_vector, 2)

    x = dot_user_cellphone + user_bias + cellphone_bias

    return tf.nn.sigmoid(x) # activation sigmoid

# %% [markdown]
# Melakukan inisialisasi model dan compile.

# %%
model = RecommenderNet(num_users, num_cellphone, 50) #inisialisasi model

#model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# %% [markdown]
# ####

# %% [markdown]
# ## Melakukan training terhadap model.

# %%
#Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

# %% [markdown]
# ####

# %% [markdown]
# ## Menampilkan grafik proses training.

# %%
#Menampilkan grafik traning vs test
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# %% [markdown]
# ####

# %% [markdown]
# #### Membuat variabel cellhpone_not_reviewed sebagai daftar cellphone untuk direkomendasikan pada pengguna.

# %%
phone_df = phone_new
df = pd.read_csv('rating.csv')

#Mengambil sample user
user_id = df.user_id.sample(1).iloc[0]
cellphone_reviewed_by_user = df[df.user_id == user_id]

cellphone_not_reviewed = phone_df[~phone_df['cellphone_id'].isin(cellphone_reviewed_by_user.cellphone_id.values)]['cellphone_id']
cellphone_not_reviewed = list(
    set(cellphone_not_reviewed)
    .intersection(set(cellphone_to_cellphone_encoded.keys()))
)

cellphone_not_reviewed = [[cellphone_to_cellphone_encoded.get(x)] for x in cellphone_not_reviewed]
user_encoder = user_to_user_encoded.get(user_id)
user_cellphone_array = np.hstack(
    ([[user_encoder]] * len(cellphone_not_reviewed), cellphone_not_reviewed)
)

# %% [markdown]
# ####

# %% [markdown]
# ## Meperoleh hasil rekomendasi cellphone.

# %%
ratings = model.predict(user_cellphone_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_cellphone_ids = [
    cellphone_encoded_to_cellphone.get(cellphone_not_reviewed[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('cellphone with high ratings from user')
print('----' * 8)

top_cellphone_user = (
    cellphone_reviewed_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .cellphone_id.values
)

cellphone_df_rows = phone_df[phone_df['cellphone_id'].isin(top_cellphone_user)]
for row in cellphone_df_rows.itertuples():
    print(row.brand, ':', row.model)

print('----' * 8)
print('Top 10 cellphone recommendation')
print('----' * 8)

recommended_cellphone = phone_df[phone_df['cellphone_id'].isin(recommended_cellphone_ids)]
for row in recommended_cellphone.itertuples():
    print(row.brand, ':', row.model)


