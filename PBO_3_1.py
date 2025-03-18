class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Calculator(self.value + other.value)
    
    def __sub__(self, other):
        return Calculator(self.value - other.value)
    
    def __mul__(self, other):
        return Calculator(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return Calculator(self.value / other.value)
    
    def __pow__(self, other):
        return Calculator(self.value ** other.value)
    
    def log(self, other):
        from math import log
        if self.value <= 0 or other.value <= 0:
            raise ValueError("Logaritma hanya berlaku untuk nilai positif!")
        return Calculator(log(other.value, self.value))
    
    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    try:
        value1 = float(input("Masukkan nilai pertama: "))
        value2 = float(input("Masukkan nilai kedua: "))
        
        a = Calculator(value1)
        b = Calculator(value2)
        
        print("Pilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Eksponen (^)")
        print("6. Logaritma (log_a(b))")
        
        pilihan = input("Masukkan pilihan (1-6): ")
        
        if pilihan == "1":
            print(f"Hasil: {a + b}")
        elif pilihan == "2":
            print(f"Hasil: {a - b}")
        elif pilihan == "3":
            print(f"Hasil: {a * b}")
        elif pilihan == "4":
            print(f"Hasil: {a / b}")
        elif pilihan == "5":
            print(f"Hasil: {a ** b}")
        elif pilihan == "6":
            print(f"Hasil: {a.log(b)}")
        else:
            print("Pilihan tidak valid!")
    except ValueError as e:
        print(f"Error: {e}")
