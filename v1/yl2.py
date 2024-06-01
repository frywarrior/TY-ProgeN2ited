def loe_seis(filename):
    dicty = {}
    with open(filename, encoding="UTF-8") as file:
        data = [i.split(" ") for i in file.read().splitlines()][1:]        
        #print(data)
        for i in data:
            dicty[i[0]] = i[1:]
            
        for voti, value in dicty.items():
            for i, j in enumerate(value):
                if j.isdigit() == True:
                    dicty[voti][i] = int(j)
    return dicty
                
    
def lisa_tulemus(name, vr_nr, data, new_value):
    if data[name][vr_nr - 1] != '-':
       print("Tulemus on juba varem lisatud!")
    else:  
        data[name][vr_nr - 1] = int(new_value)
        print("Tulemus lisatud!")
        
    print(data)

sõnastik = loe_seis("turniir.txt")

#lisa_tulemus('Mari', 3, sõnastik, 0)
#lisa_tulemus('Mari', 4, sõnastik, 2)
    
def leia_skoor(name, data):
    summa = 0
    for i in data[name]:
        if isinstance(i, int):
            summa += i
    print(summa)

leia_skoor('Malle', sõnastik)

#pooleli aga ei viici, else ifidega või switch casega, oleneb



    
