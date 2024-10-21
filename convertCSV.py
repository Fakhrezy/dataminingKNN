import pandas as pd

# Ganti 'file_excel.xlsx' dengan nama file Excel Anda
excel_file = 'data uji.xlsx'

# Membaca file Excel
df = pd.read_excel(excel_file)

# Ganti 'file_csv.csv' dengan nama file CSV yang diinginkan
csv_file = 'data uji kmeans.csv'

# Menyimpan DataFrame ke file CSV
df.to_csv(csv_file, index=False)

print(f'File {excel_file} berhasil dikonversi menjadi {csv_file}')
