# Import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Minggu 1: Memuat Dataset
dataset_path = "C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/Minggu 1-7/cakupan-deteksi-dini-kanker-leher-rahim-dan-kanker-payudara.csv"
data = pd.read_csv(dataset_path)

# Menampilkan beberapa baris awal data
print("Dataset Awal:")
print(data.head())

# Info dataset
print("\nInfo Dataset:")
print(data.info())

# Minggu 2: Pembersihan Data
# Mengecek missing values
print("\nCek Missing Values:")
print(data.isnull().sum())

# Imputasi missing values dengan median
data.fillna(data.median(numeric_only=True), inplace=True)

# Menghapus data duplikat
data = data.drop_duplicates()

# Minggu 3: Explorasi Data Awal
deskripsi_data = data.describe(include='all')

# Minggu 4: Visualisasi Data
if 'Wilayah' in data.columns and 'Jumlah' in data.columns:
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Wilayah', y='Jumlah', data=data, palette='viridis')
    plt.title('Cakupan Deteksi Dini per Wilayah')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualisasi_cakupan_per_wilayah.png")
    plt.close()

# Minggu 5: Encoding Fitur Kategorikal
encoder = LabelEncoder()
if 'Metode Deteksi' in data.columns:
    data['Metode_Deteksi_Encoded'] = encoder.fit_transform(data['Metode Deteksi'])

# Minggu 6: Pembagian Dataset
if 'Jumlah' in data.columns:
    X = data.drop(['Jumlah'], axis=1)  # Fitur
    y = data['Jumlah']  # Target
    
    # Pastikan untuk menormalisasi fitur jika perlu
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Pembagian data menjadi data latih dan uji
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"Jumlah Data Latih: {X_train.shape[0]}, Jumlah Data Uji: {X_test.shape[0]}")
    except Exception as e:
        print(f"Terjadi kesalahan dalam pembagian dataset: {e}")
        X_train, X_test, y_train, y_test = None, None, None, None

# Pastikan X_train dan y_train berhasil didefinisikan
if X_train is not None and y_train is not None:
    # Minggu 7: Pemodelan Awal
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    laporan_klasifikasi = classification_report(y_test, y_pred, output_dict=True)
    laporan_df = pd.DataFrame(laporan_klasifikasi).transpose()

    # Menentukan lokasi penyimpanan file Excel
    save_path = "C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/Minggu 1-7/hasil_deteksi_dini_kanker.xlsx"

   # Menyimpan ke file Excel menggunakan engine 'openpyxl'
with pd.ExcelWriter('C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/Minggu 1-7/hasil_deteksi_dini_kanker.xlsx', engine='openpyxl') as writer:
    data.to_excel(writer, sheet_name='Dataset Bersih', index=False)
    deskripsi_data.to_excel(writer, sheet_name='Deskripsi Data')
    laporan_df.to_excel(writer, sheet_name='Laporan Klasifikasi')

print('File Excel berhasil disimpan sebagai "hasil_deteksi_dini_kanker.xlsx".')