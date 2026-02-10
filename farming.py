import os
import status
import uang

from status import Status
status = Status()

from uang import uang
money = uang()

class Player:
    def __init__(self):
        self.day = status.day
        self.stamina = status.stamina
        self.maxstamina = status.max_stamina
        self.uang = money.saldo
        self.inventory = []

class Crop:
    def __init__(self):
        pass

class Farm:
    def __init__(self):
        self.slots = [None, None]


class Game:
    def __init__(self):
        self.running = True
        self.player = Player()

    def farmMenu(self):
        os.system("cls")
        print("==========Farm Game==========")
        print(f"day\t:{self.player.day}")
        print(f"duit\t:{self.player.uang}")
        print(f"stamina\t:{self.player.stamina}")
        print("=============================")
        print("1. Tanam\n2. Panen\n3. Siram\n4. Inventory\n5. Shop")
        print("=============================")
        print("0. Kembali?")
        pilih = input("> ")

        if pilih == "1":
            pass
        elif pilih == "2":
            pass
        elif pilih == "3":
            pass
        elif pilih == "4":
            pass
        elif pilih == "5":
            pass
        elif pilih == "0":
            pass

    def slot_tanam(self):
        print("")

game = Game()
game.farmMenu()