# Solució Projecte - Part 1


```python
import logging

# Configuració de logging
logging.basicConfig(filename='gestio_entrades.log', level=logging.DEBUG)

# Llista de seients (1-10) disponibles, True si està ocupat, False si està disponible
seients = [False] * 10  # Inicialment tots els seients estan disponibles (False)

def mostrar_seients():
    """
    Mostra els seients disponibles i ocupats.
    """
    print("Estat actual dels seients:")
    for i in range(len(seients)):
        estat = "Ocupat" if seients[i] else "Disponible"
        print(f"Seient {i + 1}: {estat}")

def reservar_seient():
    """
    Permet a l'usuari reservar un seient.
    """
    try:
        seient = int(input("Introdueix el número del seient que vols reservar (1-10): "))
        
        # Comprovació que el número del seient és vàlid
        if seient < 1 or seient > 10:
            print("Número de seient no vàlid. El número ha de ser entre 1 i 10.")
            logging.warning(f"Usuari ha intentat reservar un seient invàlid: {seient}")
            return
        
        # Comprovació si el seient ja està ocupat
        if seients[seient - 1]:
            print(f"El seient {seient} ja està ocupat.")
            logging.info(f"Seient {seient} ja ocupat. Intent de reserva fallit.")
        else:
            nom = input(f"Introdueix el teu nom per reservar el seient {seient}: ")
            seients[seient - 1] = True  # Marquem el seient com a ocupat
            print(f"El seient {seient} ha estat reservat per {nom}.")
            logging.info(f"Seient {seient} reservat per {nom}.")
    
    except ValueError:
        print("Entrada no vàlida! Has d'introduir un número enter per al seient.")
        logging.error("Error: Entrada no vàlida per al número de seient.")

def menu():
    """
    Menú principal del sistema de gestió d'entrades.
    """
    while True:
        print("\n--- Sistema de Gestió d'Entrades ---")
        print("1. Mostrar seients")
        print("2. Reservar un seient")
        print("3. Sortir")
        
        opcio = input("Tria una opció (1-3): ")
        
        if opcio == "1":
            mostrar_seients()
        elif opcio == "2":
            reservar_seient()
        elif opcio == "3":
            print("Gràcies per utilitzar el sistema!")
            logging.info("Sistema tancat.")
            break
        else:
            print("Opció no vàlida, intenta-ho de nou.")

if __name__ == "__main__":
    menu()
```