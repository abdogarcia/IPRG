
# Exercicis de Gestió de Fitxers i Fluxos de Dades

## 1. Gestió de Fitxers - Crear, Llegir i Afegir Dades

### Descripció:
Crea un programa que faci el següent:
1. Demana a l'usuari que introdueixi el seu nom i edat.
2. Guarda aquestes dades en un fitxer de text anomenat `dades_usuari.txt`.
3. Llegeix el contingut del fitxer i mostra-ho per pantalla.
4. Després, afegeix una nova línia amb una altra dada introduïda pel mateix usuari (per exemple, una nova afegida de ciutat).

### Requisits:
- Utilitza **excepcions** per gestionar possibles errors com "fitxer no trobat" o "accés denegat".


```python
try:
    with open('dades_usuari.txt', 'w') as fitxer:
        nom = input("Quin és el teu nom? ")
        edat = input("Quants anys tens? ")
        fitxer.write(f"Nom: {nom}, Edat: {edat}
")
except IOError:
    print("S'ha produït un error en obrir o escriure al fitxer.")
```



## 2. Organització de Fitxers - Moure Fitxers entre Directoris

### Descripció:
Crea un programa que mogui un fitxer d'un directori a un altre. El programa també ha de llistar els fitxers en el directori de destinació després de moure el fitxer.

### Requisits:
- Utilitza els mòduls `os` o `pathlib` per moure fitxers.
- Gestiona **excepcions** si el fitxer no es pot moure o si el directori no existeix.


```python
import shutil
import os

# Comprovar si el directori de destinació existeix
if not os.path.exists('nou_directori'):
    os.mkdir('nou_directori')

# Moure el fitxer
try:
    shutil.move('document.txt', 'nou_directori/document.txt')
    print("Fitxer mogut correctament.")
except FileNotFoundError:
    print("El fitxer no existeix.")
except PermissionError:
    print("No tens permisos per moure el fitxer.")
```


## 3. Concatenació de Fitxers de Text

### Descripció:
Crea un programa que llegeixi el contingut de diversos fitxers de text i els concatenï en un nou fitxer. El programa també ha de controlar que els fitxers d'origen existeixin abans de copiar-los.

### Requisits:
- Llegeix fitxers de text amb `read()`.
- Crea un nou fitxer de text i escriu-hi el contingut concatenat.
- Utilitza excepcions per verificar l'existència dels fitxers d'origen i gestionar possibles errors.


```python
# Llistar els fitxers d'origen
fitxers_origen = ['fitxer1.txt', 'fitxer2.txt']

# Crear el fitxer de destinació
with open('concatenat.txt', 'w') as fitxer_dest:
    for fitxer in fitxers_origen:
        try:
            with open(fitxer, 'r') as fitxer_origen:
                fitxer_dest.write(fitxer_origen.read())
        except FileNotFoundError:
            print(f"El fitxer {fitxer} no es troba.")
```


## 4. Comprovació de la Llargada de Fitxers

### Descripció:
Crea un programa que verifiqui la mida d'un fitxer i notifiqui l'usuari si el fitxer supera una mida límit especificada (en bytes). Si el fitxer és massa gran, el programa ha d'oferir l'opció de moure'l a un directori de "fitxers grans".

### Requisits:
- Utilitza `os.path.getsize()` per obtenir la mida del fitxer.
- Compara la mida del fitxer amb una mida límit i, si és massa gran, mou el fitxer a un directori específic.
- Gestiona les excepcions per garantir que el fitxer existeixi i que el directori de destinació sigui vàlid.


```python
import os
import shutil

# Mida límit (en bytes)
mida_limit = 5000  # Exemple: 5000 bytes

# Comprovar la mida del fitxer
fitxer = 'document.txt'
mida_fitxer = os.path.getsize(fitxer)

if mida_fitxer > mida_limit:
    print(f"El fitxer {fitxer} és massa gran.")
    # Moure el fitxer a 'fitxers_grans'
    if not os.path.exists('fitxers_grans'):
        os.mkdir('fitxers_grans')
    shutil.move(fitxer, 'fitxers_grans/')
    print(f"El fitxer {fitxer} ha estat mogut a la carpeta 'fitxers_grans'.")
else:
    print(f"El fitxer {fitxer} és de mida adequada.")
```


## 5. Còpia de Directoris Complets

### Descripció:
Crea un programa que copiï tot el contingut d'un directori (fitxers i subdirectoris) a un altre directori. El programa ha de mantenir la mateixa estructura de directoris.

### Requisits:
- Utilitza `shutil.copytree()` o una combinació de mètodes `os` i `shutil` per copiar els fitxers i subdirectoris.
- Gestiona excepcions per garantir que el directori d'origen existeixi i que el directori de destinació sigui vàlid.


```python
import shutil

# Copiar tot el contingut d'un directori
try:
    shutil.copytree('directori_origen', 'directori_destinacio')
    print("Directori copiat correctament.")
except Exception as e:
    print(f"S'ha produït un error: {e}")
```


## 6. Lectura i Escritura de Fitxers JSON

### Descripció:
Crea un programa que llegeixi un fitxer JSON que conté un diccionari amb les dades d'un estudiant (nom, edat, nota), el modifiqui per afegir una nova dada (com una nova assignatura), i el guardi en el mateix fitxer.

### Exemple de diccionari d'estudiant
```json
estudiant = {
    "nom": "Joan",
    "edat": 20,
    "nota": 8.5,
    "assignatures": ["Matemàtiques", "Física"]
}
```

### Requisits:
- Utilitza el mòdul `json` per gestionar els fitxers JSON.
- Gestiona **excepcions** per assegurar-te que el fitxer existeix i que el contingut és vàlid.

```python
import json

# Llegir dades des d'un fitxer JSON
with open('estudiant.json', 'r') as fitxer:
    dades_estudiant = json.load(fitxer)

# Afegir una nova assignatura
dades_estudiant["assignatures"].append("Química")

# Guardar les dades actualitzades al mateix fitxer
with open('estudiant.json', 'w') as fitxer:
    json.dump(dades_estudiant, fitxer, indent=4)
```

## 7. Lectura i Escriptura de Fitxers CSV

### Descripció:
Crea un programa que llegeixi un fitxer CSV, n'extregui les dades i les modifiqui (per exemple, afegint una nova fila o modificant una existent). Després, guarda les dades modificades en un nou fitxer CSV.

### Requisits:
- Utilitza el mòdul `csv` per llegir i escriure fitxers CSV.
- Llegeix les dades d'un fitxer CSV i mostra-les per pantalla.
- Modifica les dades (per exemple, afegint una nova fila amb dades de l'usuari).
- Guarda les dades modificades en un nou fitxer CSV.
- Gestiona excepcions per assegurar-se que el fitxer CSV existeix i és vàlid.


```python
import csv

# Llegir dades d'un fitxer CSV
try:
    with open('dades.csv', 'r') as fitxer:
        lector_csv = csv.reader(fitxer)
        dades = [fila for fila in lector_csv]  # Llegeix totes les files

    print("Dades llegides del fitxer:")
    for fila in dades:
        print(fila)

    # Afegir una nova fila amb dades de l'usuari
    nou_nom = input("Introdueix un nom: ")
    nova_edat = input("Introdueix una edat: ")
    dades.append([nou_nom, nova_edat])

    # Escriure les dades modificades en un nou fitxer CSV
    with open('dades_modificades.csv', 'w', newline='') as fitxer:
        escriptor_csv = csv.writer(fitxer)
        escriptor_csv.writerows(dades)

    print("Les dades s'han actualitzat i desat correctament.")
except FileNotFoundError:
    print("El fitxer no existeix. Comprova el camí i intenta-ho de nou.")
except Exception as e:
    print(f"S'ha produït un error: {e}")
```


---

# 8. Gestió d'un Sistema de Registre d'Estudiants

## Descripció:
Imagina que treballes en una aplicació per gestionar informació sobre estudiants d'una escola. Cada estudiant té un nom, una edat, una nota i una llista d'assignatures. La informació dels estudiants es guarda en un fitxer **JSON** i **CSV**. L'objectiu és llegir i escriure fitxers amb la informació dels estudiants, moure fitxers entre directoris per organitzar-los millor, i afegir nous estudiants mitjançant l'entrada d'usuari.

### Escenari:
1. El sistema llegeix un fitxer JSON anomenat `estudiants.json` que conté les dades dels estudiants.
2. Després, el sistema ha de:
   - Afegir un nou estudiant amb nom, edat, nota i assignatures.
   - Desar la informació actualitzada en el fitxer `estudiants.json`.
   - Crear un fitxer **CSV** anomenat `estudiants.csv` amb la mateixa informació dels estudiants (nom, edat, nota, assignatures).
   - Si el fitxer CSV ja existeix, el programa haurà de moure'l a un directori de "fitxers antics".
   - Finalment, el sistema ha de gestionar errors en tots els passos per assegurar-se que els fitxers existeixin i que els formats siguin vàlids.

### Requisits:
1. **Lectura i escriptura de fitxers JSON i CSV**.
2. **Gestió d'errors** en la lectura/escriptura de fitxers.
3. **Mou fitxers** entre directoris si el fitxer CSV ja existeix.
4. **Afegir nous estudiants** a les dades existents.


```python
import json
import csv
import os
import shutil

# Funció per afegir un nou estudiant al fitxer JSON
def afegir_estudiant_json():
    try:
        # Llegir dades existents des del fitxer JSON
        with open('estudiants.json', 'r') as fitxer_json:
            estudiants = json.load(fitxer_json)
    except FileNotFoundError:
        print("Fitxer JSON no trobat. Creant un fitxer nou.")
        estudiants = []

    # Demanem les dades de l'estudiant
    nom = input("Introdueix el nom de l'estudiant: ")
    edat = int(input("Introdueix l'edat de l'estudiant: "))
    nota = float(input("Introdueix la nota de l'estudiant: "))
    assignatures = input("Introdueix les assignatures (separades per coma): ").split(',')

    # Afegim l'estudiant
    estudiants.append({
        "nom": nom,
        "edat": edat,
        "nota": nota,
        "assignatures": assignatures
    })

    # Desem les dades actualitzades al fitxer JSON
    with open('estudiants.json', 'w') as fitxer_json:
        json.dump(estudiants, fitxer_json, indent=4)

    print("Estudiant afegit correctament al fitxer JSON.")

# Funció per escriure les dades en un fitxer CSV
def escriure_estudiants_csv():
    try:
        with open('estudiants.json', 'r') as fitxer_json:
            estudiants = json.load(fitxer_json)

        # Escrivim les dades al fitxer CSV
        with open('estudiants.csv', 'w', newline='') as fitxer_csv:
            escriptor_csv = csv.writer(fitxer_csv)
            escriptor_csv.writerow(["Nom", "Edat", "Nota", "Assignatures"])

            for estudiant in estudiants:
                escriptor_csv.writerow([estudiant["nom"], estudiant["edat"], estudiant["nota"], ",".join(estudiant["assignatures"])])
        print("Les dades han estat guardades al fitxer CSV.")
        
    except FileNotFoundError:
        print("El fitxer JSON no existeix. No es pot generar el fitxer CSV.")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

# Funció per moure un fitxer a un altre directori
def moure_fitxer():
    try:
        if os.path.exists('estudiants.csv'):
            shutil.move('estudiants.csv', 'fitxers_antics/estudiants.csv')
            print("Fitxer CSV mogut a la carpeta 'fitxers_antics'.")
        else:
            print("El fitxer CSV no existeix.")
    except Exception as e:
        print(f"S'ha produït un error en moure el fitxer: {e}")

# Funció principal per gestionar el flux
def gestionar_fitxers():
    if not os.path.exists('fitxers_antics'):
        os.mkdir('fitxers_antics')  # Creem el directori per moure els fitxers antics

    # Afegir un nou estudiant
    afegir_estudiant_json()

    # Escriure les dades al fitxer CSV
    escriure_estudiants_csv()

    # Moure el fitxer CSV si ja existeix
    moure_fitxer()

# Executem la funció principal
gestionar_fitxers()
```

### Explicació:

1. **Afegir un nou estudiant**: Primer, el programa llegeix les dades existents del fitxer `estudiants.json`, afegeix un nou estudiant, i després desa les dades actualitzades en el mateix fitxer.
2. **Escriure fitxer CSV**: Després d'afegir el nou estudiant, el programa escriu les dades en un fitxer CSV anomenat `estudiants.csv`, amb els noms, edats, notes i assignatures.
3. **Moure fitxer CSV**: Si el fitxer CSV ja existeix, el programa el mou a un directori anomenat `fitxers_antics`.
4. **Gestió d'errors**: El codi gestiona errors comuns com la falta de fitxers i errors de lectura/escriptura.


Aquest tipus d'exercici és pràctic i abasta un conjunt ampli de tasques que un programador podria enfrontar-se en la seva feina diària, especialment en la gestió de dades de diversos formats i organització de fitxers.
