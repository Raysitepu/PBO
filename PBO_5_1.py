import tkinter as tk
from tkinter import messagebox

def tampilkan_nama():
    nama = entry_nama.get()
    messagebox.showinfo("Halo!", f"Halo, {nama}!")

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI Tkinter")
root.geometry("300x150")  # ukuran jendela

# Label
label = tk.Label(root, text="Masukkan nama Anda:")
label.pack(pady=10)

# Entry
entry_nama = tk.Entry(root, width=30)
entry_nama.pack()

# Tombol
tombol = tk.Button(root, text="Tampilkan Nama", command=tampilkan_nama)
tombol.pack(pady=10)

# Menjalankan GUI
root.mainloop()
