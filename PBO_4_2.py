def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan semua tugas")
    print("4. Keluar")

def tambah_tugas(todo_list):
    try:
        tugas = input("Masukkan tugas: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        todo_list.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan.")
    except ValueError as e:
        print(f"Error: {e}")

def hapus_tugas(todo_list):
    try:
        if not todo_list:
            raise Exception("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
        tugas = input("Masukkan tugas yang ingin dihapus: ").strip()
        if not tugas:
            raise ValueError("Input tidak boleh kosong.")
        if tugas not in todo_list:
            raise ValueError(f"Tugas '{tugas}' tidak ditemukan dalam daftar.")
        todo_list.remove(tugas)
        print(f"Tugas '{tugas}' berhasil dihapus.")
    except Exception as e:
        print(f"Error: {e}")

def tampilkan_tugas(todo_list):
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(todo_list, start=1):
            print(f"{i}. {tugas}")

def main():
    todo_list = []

    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (1-4): ").strip()
            if pilihan not in ["1", "2", "3", "4"]:
                raise ValueError("Pilihan tidak valid. Silakan pilih antara 1 sampai 4.")
            
            if pilihan == "1":
                tambah_tugas(todo_list)
            elif pilihan == "2":
                hapus_tugas(todo_list)
            elif pilihan == "3":
                tampilkan_tugas(todo_list)
            elif pilihan == "4":
                print("Keluar dari program.")
                break
        except ValueError as e:
            print(f"Error: {e}")

# Jalankan program
main()
