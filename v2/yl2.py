def loe_seis(fail):
    dicty = {}
    with open(fail, encoding="UTF-8") as file:
        data = file.read().splitlines()
        for i in data:
            i = i.split(" ")
            dicty[i[0]] = i[1:]
            
        for voti, value in dicty.items():
            for i, j in enumerate(value):
                dicty[voti][i] = int(j)
    return dicty

def lisa_tulemus(nimi, data, tulemus):
    if nimi in data.keys():
        data[nimi].append(tulemus)
        print("Tulemus listud")
    else:
        print("Sellist korvpallurti pole sõnastikus!")
    
def leia_keskmine(nimi, data):
    return round(sum(data[nimi])/len(data[nimi]), 2)

def leia_parim(data):
    largest = ["",0]
    for voti, value in data.items():
        if round(sum(value)/len(value), 2) > largest[1]:
            largest = [voti, round(sum(value)/len(value), 2)]
    print(f"Parim on {largest[0]} tulemusega {largest[1]}")        

sõnastik = loe_seis("punktid.txt")
print(sõnastik)
done = False

while not done:
    print("""1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Leia korvpalluri keskmine
4 - Leia parim
5 - Lõpeta programmi töö""")
    tegevus = int(input("Vali tegevus: "))
    
    match tegevus:
        case 1:
            for võti, value in sõnastik.items():
                print(f"{võti}", end=" ")
                for i in value:
                    print(i, end = " ")
                print("")
        case 2:
            nimi = str(input("Sisesta nimi: "))
            punktid = int(input("Sisesta punktid: "))
            
            lisa_tulemus(nimi, sõnastik, punktid)
        
        case 3:
            nimi = str(input("Sisesta nimi: "))
            
            print(f"Mängja {nimi} keskmine skoor on {leia_keskmine(nimi, sõnastik)}")
            
        case 4:
            leia_parim(sõnastik)
        
        case 5:
            with open("punktid_uus.txt", "w", encoding="UTF-8") as file:
                for võti, value in sõnastik.items():
                    text = ""
                    text += võti + " "
                    for i in value:
                        text += f"{i} "
                    file.write(text)
                    file.write("\n")
            print("faili salvestatud. Programm lõpetas töö.")
            done = True
                    
    