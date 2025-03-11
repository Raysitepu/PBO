class Robot:
    def __init__(self, nama, hp=500, attack=50, defense=20, regen=20):
        self.nama = nama
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.regen = regen
        self.is_defending = False

    def attack_enemy(self, target):
        damage = max(0, self.attack - target.get_defense())
        target.take_damage(damage)
        return f"{self.nama} menyerang {target.nama} dan memberikan {damage} damage!"

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self):
        if self.hp > 0:
            self.hp = min(self.max_hp, self.hp + self.regen)
            return f"{self.nama} meregenerasi {self.regen} HP!"
        return ""

    def set_defense(self, is_defending):
        self.is_defending = is_defending

    def get_defense(self):
        return self.defense * 2 if self.is_defending else self.defense

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.nama} [{self.hp}/{self.max_hp}]"

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def display_status(self):
        print(f"\nRound-{self.round} {'='*50}")
        print(self.robot1)
        print(self.robot2)
        print()

    def get_action(self, robot):
        while True:
            try:
                print("1. Attack     2. Defense     3. Regen     4. Giveup")
                action = int(input(f"{robot.nama}, pilih aksi: "))
                if 1 <= action <= 4:
                    return action
                print("Pilihan tidak valid!")
            except ValueError:
                print("Masukkan angka yang valid!")

    def play(self):
        while True:
            self.display_status()
            
            # Aksi Robot 1
            action1 = self.get_action(self.robot1)
            if action1 == 4:
                print(f"\n{self.robot2.nama} menang!")
                break
                
            # Aksi Robot 2
            action2 = self.get_action(self.robot2)
            if action2 == 4:
                print(f"\n{self.robot1.nama} menang!")
                break

            # Proses aksi
            self.process_actions(action1, action2)
            
            # Cek kondisi menang
            if not self.robot1.is_alive():
                print(f"\n{self.robot2.nama} menang!")
                break
            elif not self.robot2.is_alive():
                print(f"\n{self.robot1.nama} menang!")
                break
                
            self.round += 1

    def process_actions(self, action1, action2):
        # Reset defense status
        self.robot1.set_defense(False)
        self.robot2.set_defense(False)

        # Set defense jika dipilih
        if action1 == 2:
            self.robot1.set_defense(True)
        if action2 == 2:
            self.robot2.set_defense(True)

        # Proses serangan dan regenerasi
        if action1 == 1:
            print("\n" + self.robot1.attack_enemy(self.robot2))
        elif action1 == 3:
            print("\n" + self.robot1.heal())
        
        if action2 == 1:
            print(self.robot2.attack_enemy(self.robot1))
        elif action2 == 3:
            print(self.robot2.heal())

# Contoh penggunaan
if __name__ == "__main__":
    robot1 = Robot("Atreus", hp=500, attack=50, defense=20, regen=20)
    robot2 = Robot("Daedalus", hp=750, attack=40, defense=25, regen=25)
    game = Game(robot1, robot2)
    game.play()
