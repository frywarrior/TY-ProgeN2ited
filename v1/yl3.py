class Tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanus = vanus
        self.elukoht = elukoht
        
    def __str__(self):
        return f"Nimi: {self.nimi}, vanus: {self.vanus}, elukoht: {self.elukoht}"
    
    def kummita(self):
        print(f"{self.nimi} kummitab elukohas {self.elukoht}!")
        
class Võlur(Tont):
    def nõiu(self, isend):
        print(f"{self.nimi} pani nõiduse, millega sai pihta {isend.nimi}!")
    
tont = Tont("Norbert", 31, "Tartu")
print(tont)
tont.kummita()

harry = Võlur("Harry", 17, "Tartu")
print(harry)
snape = Võlur("Snape", 35, "Tartu")
print(snape)

harry.nõiu(snape)