def juurdekasv(pind, kasv):
    return (round((kasv * pind * 0.4047), 2))


#print(juurdekasv(3.78, 6.6))

name = str(input("Sisestage failinimi: "))
kasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

count = 0
with open(name) as file:
    for aaker in file:
        if float(aaker) < piir:
            print("Metsatükki ei võeta arvesse")
        else:
            print(juurdekasv(float(aaker), kasv))
            count += 1
            
print(f"Arvutati {count} metsatüki juurdekasv")