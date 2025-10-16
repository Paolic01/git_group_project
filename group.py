# Riga di commento di Flavio
def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "pari"
    else:
        return "dispari"

if __name__ == "__main__":
    numero = int(input("Inserisci un numero: "))
    print(f"Il numero {numero} è {pari_o_dispari(numero)}")

    
