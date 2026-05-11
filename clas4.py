class Futbolchi:
    def __init__(self, ism, yosh, klub, gol):
        self.ism = ism
        self.yosh = yosh
        self.klub = klub
        self.gol = gol

    def malumot(self):
        print(" FUTBOLCHI HAQIDA")
        print(f" Ism: {self.ism}")
        print(f" Yosh: {self.yosh}")
        print(f" Klub: {self.klub}")
        print(f" Gollar soni: {self.gol}")

    def oyin(self):
        print(f"{self.ism} chiroyli gol urdi! ")


# Obyekt
player1 = Futbolchi("Ronaldo", 39, "Al Nassr", 900)

# Metodlar
player1.malumot()
player1.oyin()