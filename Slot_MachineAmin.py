#Slot Machine Casino
import random

def spin_row():
    symbols = ['🍋', '🍒', '🍉', '🔔', '⭐']

    return[random.choice(symbols) for _ in range(3)]

    

def print_row(row):
    print("************")
    print("|".join(row))
    print("************")

def get_payout(row, scommessa):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return scommessa * 2
        elif row[0] == '🍉':
            return scommessa * 3
        elif row[0] == '🍋':
            return scommessa * 4
        elif row[0] == '🔔':
            return scommessa * 5
        elif row[0] == '⭐':
            return scommessa * 100
    return 0
        
        


    

def main():
    saldo = 100

    print(" *************************************")
    print(" Benvenuto al Casino Amin in Python ")
    print(" Simboli:🍋🍒🍉🔔⭐ ")
    print(" ************************************* ")

    while saldo > 0:
        print(f"Il saldo al corrente è : ${saldo}")

        scommessa = input("Immetti l'importo della scommessa: ")

        if not scommessa.isdigit():
            print("Inserisci un numero valido")
            continue

        scommessa = int(scommessa)

        if scommessa > saldo:
            print("Saldo insufficiente.")
            continue

        if scommessa <= 0:
            print("La scommessa deve essere maggiore di 0")
            continue

        saldo -= scommessa


        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, scommessa)

        if payout > 0:
            print(f"Hai vinto! ${payout}")
        else:
            print("Mi dispiace hai perso sta volta.(continuerai a perdere sfigato...)")

        saldo += payout

        gioca_ancora = input("Vuoi spinnare ancora? (Y/N):").upper()

        if gioca_ancora != 'Y':
            break




if __name__ == '__main__':
    main()
