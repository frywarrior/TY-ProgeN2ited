def lugemise_aeg(lk_arv, kirjasuurus):
    if kirjasuurus == "suur":
        return lk_arv * 20
    if kirjasuurus == "keskmine":
        return lk_arv * 30
    if kirjasuurus == "väike":
        return lk_arv * 40


def main():
    failinimi = input("Sisestage failinimi: ")

    lk_arvud = []
    kokku = 0
    with open(failinimi) as fail:
        for rida in fail:
            lk_arv = int(rida)
            lk_arvud.append(lk_arv)
            kirjastiil = input(f"Raamat on {lk_arv} lk. Kui suur on kirjastiil?")
            kokku += lugemise_aeg(lk_arv, kirjastiil)
    sek = kokku
    sek = sek % (24 * 3600)
    tund = sek // 3600
    sek %= 3600
    minut = sek // 60
    sek %= 60

    print(f"Kokku kulub raamatute lugemiseks {tund} tundi, {minut} minutit ja {sek} sekundit.")


main()

