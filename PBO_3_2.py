import random

class Parent:
    VALID_BLOOD_TYPES = ['AA', 'AO', 'BB', 'BO', 'AB', 'OO']
    
    def __init__(self, blood_type):
        if blood_type not in self.VALID_BLOOD_TYPES:
            raise ValueError(f"Golongan darah '{blood_type}' tidak valid! Harus salah satu dari {self.VALID_BLOOD_TYPES}")
        self.blood_type = blood_type

    def get_allele(self):
        return list(self.blood_type)

class Child:
    def __init__(self, father, mother):
        if not isinstance(father, Parent) or not isinstance(mother, Parent):
            raise TypeError("Father dan Mother harus berupa objek Parent!")
            
        self.father = father
        self.mother = mother
        self.blood_type = self._determine_blood_type()

    def _determine_blood_type(self):
        father_allele = random.choice(self.father.get_allele())
        mother_allele = random.choice(self.mother.get_allele())
        return ''.join(sorted([father_allele, mother_allele]))

    def get_blood_group(self):
        if 'A' in self.blood_type and 'B' in self.blood_type:
            return "AB"
        elif 'A' in self.blood_type:
            return "A"
        elif 'B' in self.blood_type:
            return "B"
        else:
            return "O"

if __name__ == "__main__":
    while True:
        try:
            father_blood = input("Masukkan golongan darah ayah (AA, AO, BB, BO, AB, OO): ").strip().upper()
            ayah = Parent(father_blood)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            mother_blood = input("Masukkan golongan darah ibu (AA, AO, BB, BO, AB, OO): ").strip().upper()
            ibu = Parent(mother_blood)
            break
        except ValueError as e:
            print(e)
    
    num_children = int(input("Masukkan jumlah anak yang ingin disimulasikan: "))
    for i in range(num_children):
        anak = Child(ayah, ibu)
        print(f"\nAnak {i+1}:")
        print(f"Genotip: {anak.blood_type}")
        print(f"Golongan Darah: {anak.get_blood_group()}")
