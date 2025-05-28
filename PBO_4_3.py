class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def makan(self):
        return f"{self.nama} sedang makan."

    def suara(self):
        return f"{self.nama} mengeluarkan suara."

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


class Singa(Hewan):
    def suara(self):
        return f"{self.nama} mengaum dengan keras!"


class Gajah(Hewan):
    def suara(self):
        return f"{self.nama} mengeluarkan suara terompet!"


class Burung(Hewan):
    def suara(self):
        return f"{self.nama} berkicau dengan merdu."


# Fungsi untuk membuat hewan
def buat_hewan():
    try:
        jenis = input("Masukkan jenis hewan (singa/gajah/burung): ").lower()
        nama = input("Masukkan nama hewan: ")
        umur = int(input("Masukkan umur hewan: "))

        if jenis == "singa":
            return Singa(nama, umur)
        elif jenis == "gajah":
            return Gajah(nama, umur)
        elif jenis == "burung":
            return Burung(nama, umur)
        else:
            raise ValueError("Jenis hewan tidak dikenali!")
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")
        return None


# Program utama
def main():
    daftar_hewan = []

    while True:
        print("\n--- Sistem Manajemen Hewan ---")
        print("1. Tambah Hewan")
        print("2. Tampilkan Semua Hewan")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            hewan = buat_hewan()
            if hewan:
                daftar_hewan.append(hewan)
                print(f"{hewan.nama} berhasil ditambahkan!")
        elif pilihan == "2":
            if not daftar_hewan:
                print("Belum ada hewan di kebun binatang.")
            else:
                for h in daftar_hewan:
                    print(h.info())
                    print(h.makan())
                    print(h.suara())
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
