# Exemple complet per al càlcul de l'any de naixement

while True:
    try:
        # Demanem l'edat a l'usuari
        edat = int(input("Quants anys tens? "))
        
        # Comprovem que l'edat sigui un valor positiu
        if edat < 0:
            print("L'edat no pot ser negativa. Introdueix una edat vàlida.")
            continue  # Tornem a començar el bucle si l'edat és negativa
        
        # Comprovació de límits d'edat
        if edat <= 0 or edat >= 120:
            print("Per favor, introdueix una edat vàlida entre 1 i 120 anys.")
            continue  # Tornem a començar el bucle si l'edat no està en rang
        
        break  # Sortim del bucle quan l'edat és vàlida
        
    except ValueError:
        print("Per favor, introdueix un número vàlid.")

# Si l'usuari introdueix l'edat correctament, demanem l'any actual
while True:
    try:
        any_actual = int(input("Quin any és actualment? "))
        
        assert any_actual == 2025

        break  # Sortim del bucle quan l'any actual és vàlid
    except ValueError:
        print("Per favor, introdueix un any vàlid.")
    except AssertionError:
        print("T'estàs quedant en mi? Va tira va, introdueix l'any actual...")

# Calculem l'any de naixement
any_naixement = any_actual - edat

# Mostrem el resultat amb un missatge personalitzat
print(f"Si tens {edat} anys, vas néixer al {any_naixement}. Gràcies per introduir la teva edat!")
