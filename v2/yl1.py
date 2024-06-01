def lugemise_aeg(lehed, suurus):
    match suurus:
        case "suur":
            aeg = 20
        case "keskmine":
            aeg = 30
        case "väike":
            aeg = 40
        case _:
            print("vigane suurus")
            return 0

    return int(lehed)*aeg

name = str(input("Sisesta faili nimi: "))

aeg_kokku_s = 0
with open(name, encoding="UTF-8") as file:
    for lk in file:
        suurus = str(input(f"Raamat on {int(lk)} lk. Kui suur on kirjastiil? "))
        aeg_kokku_s += lugemise_aeg(int(lk), suurus)
s = aeg_kokku_s % (24 * 3600)
h = s // 3600
s %= 3600
m = s // 60
s %= 60

print(f"Kokku kulub raamatute lugemiseks {h} tundi, {m} minutit ja {s} sekundit")
    