# Meminta input tinggi segitiga dari pengguna
height = int(input("Masukkan tinggi segitiga: "))

# Membuat segitiga
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))
