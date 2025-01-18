import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import os

# Load dataset
dataset_path = "C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/Minggu 8-14/cakupan-deteksi-dini-kanker-leher-rahim-dan-kanker-payudara.csv"
save_path = "C:/Users/user/Documents/Tugas Kuliah/SEMESTER 5/DataMining/Minggu 8-14/hasil_laporan_deteksi_dini.xlsx"

if not os.path.exists(dataset_path):
    print(f"File tidak ditemukan: {dataset_path}")
    exit()

# Membaca dataset
data = pd.read_csv(dataset_path)
print("Dataset berhasil dimuat.")

# Cek kolom dalam dataset
print("\nKolom dalam dataset:")
print(data.columns)

# Encoding kolom kategorikal
encoder = LabelEncoder()
if 'jenis_deteksi_dini_kanker_leher_rahim_dan_kanker_payudara' in data.columns:
    data['Metode_Deteksi_Encoded'] = encoder.fit_transform(
        data['jenis_deteksi_dini_kanker_leher_rahim_dan_kanker_payudara'])
    print("\nKolom 'jenis_deteksi_dini_kanker_leher_rahim_dan_kanker_payudara' berhasil diencode.")
else:
    print("\nKolom 'jenis_deteksi_dini_kanker_leher_rahim_dan_kanker_payudara' tidak ditemukan.")
    exit()

# Memastikan kolom target tersedia
if 'jumlah_deteksi_dini' not in data.columns:
    print("\nKolom 'jumlah_deteksi_dini' tidak ditemukan. Proses dihentikan.")
    exit()

# Split data menjadi fitur dan target
X = data[['Metode_Deteksi_Encoded']]
y = data['jumlah_deteksi_dini']

# Split data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("\nAkurasi Model:")
print(accuracy_score(y_test, y_pred))

# Laporan klasifikasi
laporan_klasifikasi = classification_report(y_test, y_pred, output_dict=True)
laporan_df = pd.DataFrame(laporan_klasifikasi).transpose()

# Menyimpan hasil ke Excel
try:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Pastikan folder tujuan ada
    with pd.ExcelWriter(save_path) as writer:
        data.to_excel(writer, sheet_name="Dataset Bersih", index=False)
        laporan_df.to_excel(writer, sheet_name="Laporan Klasifikasi")
    print(f"\nHasil laporan disimpan di: {save_path}")
except Exception as e:
    print(f"\nTerjadi kesalahan saat menyimpan file Excel: {e}")