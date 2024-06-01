def loe_seis(failinimi):
    sõnastik = {}
    with open(failinimi, encoding="UTF-8") as fail:
        for rida in fail:
            osad = rida.split()
            punktid = [eval(i) for i in osad[1:]]
            sõnastik[osad[0]] = punktid
    return sõnastik


def lisa_tulemus(nimi, sõnastik, tulemus):
    if nimi in sõnastik:
        sõnastik[nimi].append(tulemus)
        print("Tulemus lisatud!")
    else:
        print("Sellist korvpallurit pole sõnastikus!")
    return sõnastik


def leia_keskmine(nimi, sõnastik):
    return sum(sõnastik[nimi]) / len(sõnastik[nimi])


def leia_parim(sõnastik):
    parim_tulemus = 0
    parim_nimi = ""
    for võti in sõnastik:
        if leia_keskmine(võti, sõnastik) > parim_tulemus:
            parim_nimi = võti
            parim_tulemus = leia_keskmine(võti, sõnastik)
    print(f"Parim on {parim_nimi} tulemusega {parim_tulemus}.")


def sõnastik_faili(sõnastik, failinimi):
    with open(failinimi, "w") as fail:
        for võti, väärtus in sõnastik.items():
            punktid = ' '.join(str(e) for e in väärtus)
            fail.write(f"{võti} {punktid}\n")


def main():
    sõnastik = loe_seis("punktid.txt")
    print("""1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Leia korvpalluri keskmine
4 - Leia parim
5 - Lõpeta programmi töö
""")
    end = False
    while end == False:
        valik = input("\nVali tegevus: ")
        if valik == "1":
            for võti, väärtus in sõnastik.items():
                punktid = ' '.join(str(e) for e in väärtus)
                print(f"{võti} {punktid}")
        elif valik == "2":
            nimi = input("Sisesta nimi: ")
            tulemus = int(input("Sisesta punktid: "))
            sõnastik = lisa_tulemus(nimi, sõnastik, tulemus)
        elif valik == "3":
            nimi = input("Nimi: ")
            print(leia_keskmine(nimi, sõnastik))
        elif valik == "4":
            leia_parim(sõnastik)
        elif valik == "5":
            sõnastik_faili(sõnastik, "punktid_uus.txt")
            print("Faili salvestatud. Programm lõpetas töö.")
            end = True
        else:
            print("Sellist valikud ei ole.")

main()

