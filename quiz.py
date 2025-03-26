
print("ez egy kviz")
print("A kerdesek 1-5-ig lesznek")
print("1-es a legkonnyebb, 5-os a legnehezebb")

pont = 0
szazalek = 0



for i in range(4):
    melyikkerdes = input("Melyik kerdest valasztod?")
    if melyikkerdes == "1":
        a = 4
        b = 8
        c = 1
        d = 5
        print(f"a = {a}, \nb = {b}, \nc = {c}, \nd = {d}")
        kerdes1 = input("Mennyi 2+2(a, b, c, d) ")
        if kerdes1 == "a":
            print("Helyes")
            pont = pont + 1
            szazalek = szazalek + 25
        else:
            print("Hibas")
    elif melyikkerdes == "2":
        a = 100
        b = 94
        c = 144
        d = 522
        print(f"a = {a}, \nb = {b}, \nc = {c}, \nd = {d}")
        kerdes2 = input("Mennyi 12*12(a, b, c, d) ")
        if kerdes2 == "c":
            print("Helyes")
            pont = pont + 1
            szazalek = szazalek + 25
        else:
            print("Hibas")
    elif melyikkerdes == "3":
        a = 14400
        b = 5636
        c = 29353
        d = 4444
        print(f"a = {a}, \nb = {b}, \nc = {c}, \nd = {d}")
        kerdes3 = input("Mennyi 120*120(a, b, c, d) ")
        if kerdes3 == "a":
            print("Helyes")
            pont = pont + 1
            szazalek = szazalek + 25
        else:
            print("Hibas")
    elif melyikkerdes == "4":
        a = 2564845
        b = 34654
        c = 467745
        d = 165528
        print(f"a = {a}, \nb = {b}, \nc = {c}, \nd = {d}")
        kerdes2 = input("Mennyi 627*264(a, b, c, d) ")
        if kerdes2 == "d":
            print("Helyes")
            pont = pont + 1
            szazalek = szazalek + 25
        else:
            print("Hibas")
    elif melyikkerdes == "quit":
        break
print(f"Az eredmenyed: {pont}")
print(f"A teljesitmenyed: {szazalek}%")
