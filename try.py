#elso
def osztas():
    try:
        szam1 = float(input("Kérem az első számot: "))
        szam2 = float(input("Kérem a második számot: "))
        eredmeny = szam1 / szam2
        
    except ZeroDivisionError:
        print("nullaval nem lehet osztani. (nincs ertelmezve zsa)")
    except ValueError:
        print("számot adj meg szolgalelku.")
    else:
        print(f"Eredmeny: {eredmeny}")

#masodik

def negyzet(szam):
    try:
        eredmeny = szam**2
    except ValueError:
        print("számot adj meg szolgalelku.")
    else:
        print(f'Eredmeny: {eredmeny}')

#harmadik

def fajl_olvasas():
    try:
        with open("data.txt", "r") as file:
            tartalom = file.read()
            print(tartalom)
    except FileNotFoundError:
        print("nemletezik......")

#negyedik

def lista_elem_lekeres():
    lista = [10, 20, 30, 40, 50]  

    try:
        index = int(input("index: "))
        
        elem = lista[index]
        print(f"A lista {index}. indexu eleme: {elem}")
    
    except IndexError:
        print("Hiba: az index hataron kivuli eset.")
    
    except ValueError:
        print("Hiba: ervenytelen szamot adj meg puszi")