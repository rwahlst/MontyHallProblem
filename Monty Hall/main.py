import random
import os

class MontyHall():

    Set = None
    WinningIndex = -1
    ChoiceIndex = -1
    NumDoors = 3

    NumWinsSwitch = 0
    TotalItersSwitch = 0
    NumWinsNoSwitch = 0
    TotalItersNoSwitch = 0

    def __init__(self):
        while True:
            self.Setup()
            self.RevealDoors()
            self.Switch()
            self.Setup()
            self.RevealDoors()
            self.NoSwitch()
            os.system("clear")

    def Setup(self):

        self.Set = [ ]
        for i in range(self.NumDoors):
            self.Set.append(Door(False))

        self.WinningIndex = random.randrange(len(self.Set))
        self.Set[self.WinningIndex].Win = True

        self.ChoiceIndex = random.randrange(len(self.Set))

    def RevealDoors(self):
        if self.WinningIndex == self.ChoiceIndex:
            randDoorIndex = random.randrange(len(self.Set))
            while randDoorIndex == self.ChoiceIndex:
                randDoorIndex = random.randrange(len(self.Set))
            for i in range(0, len(self.Set)):
                if i == randDoorIndex or i == self.ChoiceIndex:
                    continue
                else:
                    self.Set[i].Revealed = True
            return

        for i in range(len(self.Set)):
            if i == self.WinningIndex or i == self.ChoiceIndex:
                continue
            else:
                self.Set[i].Revealed = True

    def Switch(self):
        for i in range(0, len(self.Set)):
            if not self.Set[i].Revealed and i != self.ChoiceIndex:
                self.ChoiceIndex = i
                break
        result: Door = self.Set[self.ChoiceIndex]
        if result.Win:
            self.NumWinsSwitch += 1
        self.TotalItersSwitch += 1
        print("Win Pct Switch: " + str((self.NumWinsSwitch / self.TotalItersSwitch) * 100) + "%")
        print("Num Experiments (switch): " + str(self.TotalItersSwitch))

    def NoSwitch(self):
        result: Door = self.Set[self.ChoiceIndex]
        if result.Win:
            self.NumWinsNoSwitch += 1
        self.TotalItersNoSwitch += 1
        print("Win Pct NoSwitch: " + str((self.NumWinsNoSwitch / self.TotalItersNoSwitch) * 100) + "%")
        print("Num Experiments (no switch): " + str(self.TotalItersNoSwitch))

class Door():

    Win = False
    Revealed = False

    def __init__(self, isWin):
        self.Win = isWin
        self.Revealed = False

    def __str__(self):
        string = "Win: " + str(self.Win) + "\nRevealed: " + str(self.Revealed)
        return string


mh = MontyHall()