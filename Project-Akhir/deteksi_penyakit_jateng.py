# 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Memuat Dataset
dataset = pd.read_csv("C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/jawa_tengah_disease_cases.csv")

# 3. Menghapus Spasi Ekstra di Nama Kolom (jika ada)
dataset.columns = dataset.columns.str.strip()

# 4. Menampilkan Nama Kolom dan 5 Data Pertama untuk Verifikasi
print("Nama Kolom:", dataset.columns)
print(dataset.head())

# 5. Memeriksa apakah Kolom 'Jumlah Kasus' ada
if 'Jumlah Kasus' in dataset.columns:
    # 6. Visualisasi Distribusi Jumlah Kasus
    sns.histplot(dataset['Jumlah Kasus'], kde=True)
    plt.title('Distribusi Jumlah Kasus Penyakit')
    plt.xlabel('Jumlah Kasus')
    plt.ylabel('Frekuensi')
    plt.show()
else:
    print("Kolom 'Jumlah Kasus' tidak ditemukan!")

# 7. Menyimpan Hasil Analisis ke File Excel
# Misalnya, hasil prediksi atau analisis yang ingin disimpan
hasil_prediksi = dataset  # Gantilah dengan hasil analisis atau prediksi kamu

# Menyimpan ke file Excel
hasil_prediksi.to_excel("hasil_prediksi_jateng.xlsx", index=False)
print("Hasil disimpan dalam file 'hasil_prediksi_jateng.xlsx'")

