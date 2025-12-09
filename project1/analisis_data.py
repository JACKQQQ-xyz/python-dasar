import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

# Melihat struktur data
data.info()
print(data.head())
print(data.describe())

# Menghitung nilai statistik
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# Menampilkan data hanya untuk pelajaran Matematika
matematika = data[data['Matpel'] == 'Matematika']
print("\nData Nilai Matematika:\n", matematika)

# Menampilkan data untuk pelajaran Bahasa Indonesia
bahasaIndonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("\nData Nilai Bahasa Indonesia:\n", bahasaIndonesia)

# Mencari nilai maksimum dan minimum tiap mapel
print("\nNilai Maksimum dan Minimum Tiap Mapel:")
print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

# Grafik rata-rata nilai tiap mapel
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()

# Boxplot untuk melihat sebaran nilai
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()
