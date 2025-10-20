# ==============================================
# Analisis Data & Visualisasi Data Nilai Siswa
# ==============================================

# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset (pastikan file nilai_siswa.csv ada di folder yang sama)
data = pd.read_csv('nilai_siswa.csv')

# Tampilkan informasi dataset
print("=== Informasi Dataset ===")
data.info()

# Tampilkan 5 data pertama
print("\n=== 5 Data Pertama ===")
print(data.head())

# Tampilkan statistik deskriptif
print("\n=== Statistik Deskriptif ===")
print(data.describe())

# Tampilkan semua data untuk pengecekan
print("\n=== Data Lengkap ===")
print(data)

# Hitung ukuran statistik dasar
print("\n=== Ukuran Statistik Dasar ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# Nilai maksimum dan minimum per mata pelajaran
print("\n=== Nilai Maksimum dan Minimum per Mapel ===")
print(data.groupby('Mapel')['Nilai'].agg(['max','min']))

# Buat grafik batang rata-rata nilai per mapel
rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Buat diagram boxplot untuk melihat sebaran nilai
sns.boxplot(x='Mapel', y='Nilai', data=data, palette='pastel')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================
# Akhir Program
# ==============================================
