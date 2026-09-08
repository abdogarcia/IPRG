<h1 style="display:none;"># Inici</h1>

# 4. Gestió de Fitxers

## 4.1. Introducció als fitxers

Un **fitxer** és un conjunt de dades emmagatzemades en un dispositiu de memòria, com un disc dur o una unitat SSD. Els fitxers poden ser de diferents tipus: text, binaris, o fins i tot bases de dades.

Els fitxers es poden classificar en:

- **Fitxers de text**: Contenen dades llegibles per l'usuari, com arxius `.txt`, `.csv` o `.json`.
- **Fitxers binaris**: Contenen dades en format binari, que no es poden llegir directament, com arxius d'imatges, àudio o fitxers `.exe`.

## 4.2. Obrir i tancar fitxers

Per treballar amb fitxers en Python, s'utilitza la funció `open()`, que obre un fitxer i retorna un objecte fitxer que permet llegir-lo o escriure-hi. Un cop hem acabat de treballar amb un fitxer, cal tancar-lo per alliberar els recursos associats.

### Obrir un fitxer
El mètode `open()` accepta diversos paràmetres, entre els quals el més important és el **nom del fitxer** i el **mode d'obertura**. Els modes més comuns són:

- `'r'` per llegir (mode de lectura). Si **no existeix**, donarà **`FileNotFoundError`**, i **si ja existeix, el sobrescriu**
- `'w'` per escriure (mode d'escriptura, crea el fitxer si no existeix).
- `'a'` per afegir (mode d'afegir dades al final del fitxer).
- `'x'` per fer el que es coneix com "creació exclusiva". Si **ja existeix**, Python llença un **`FileExistsError`** i si no, el crea.
- `'rb'` i `'wb'` per llegir i escriure en mode binari.

Exemple d'obertura d'un fitxer:
```python
# Obrir un fitxer per llegir-lo
fitxer = open('document.txt', 'r')
```

### Tancar un fitxer
Un cop hem acabat de llegir o escriure, és important tancar el fitxer per evitar pèrdues de dades o problemes amb l'accés al fitxer.

Exemple de tancament d'un fitxer:
```python
# Tancar el fitxer
fitxer.close()
```

És recomanable utilitzar el context de `with`, que tanca automàticament el fitxer un cop finalitzat el bloc de codi.

```python
# Exemple amb 'with', que tanca automàticament el fitxer
with open('document.txt', 'r') as fitxer:
    contingut = fitxer.read()
```

## 4.3. Lectura i escriptura de fitxers

Una vegada que tenim un fitxer obert, podem llegir el seu contingut o escriure-hi dades, depenent del mode en què s'ha obert el fitxer.

### Lectura de fitxers

Per llegir el contingut d'un fitxer, utilitzem mètodes com `read()`, `readline()` i `readlines()`.

- `read()` llegeix tot el contingut del fitxer.
- `readline()` llegeix una línia del fitxer a la vegada.
- `readlines()` llegeix totes les línies i les retorna com una llista de cadenes.

Exemple de lectura:
```python
# Llegir tot el contingut d'un fitxer
with open('document.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
```

### Escriptura de fitxers
Per escriure dades en un fitxer, utilitzem els mètodes `write()` o `writelines()`. `write()` escriu una cadena al fitxer, mentre que `writelines()` escriu una sèrie de cadenes.

Exemple d'escriptura:

```python
# Escriure en un fitxer
with open('documente_nou.txt', 'w') as fitxer:
    fitxer.write("Aquesta és una nova línia.")
    fitxer.write("Aquesta és una altra línia.")
```

## 4.4. Gestió d'errors en l'obertura i manipulació de fitxers

Quan treballem amb fitxers, és important gestionar adequadament els errors que poden sorgir, com ara quan un fitxer no existeix, quan no tenim permisos per llegir o escriure, o quan hi ha errors d'entrada/sortida. Python ens ofereix eines per capturar i gestionar aquests errors mitjançant excepcions.

### Ús de `try` i `except`
El mètode més comú per gestionar errors és envoltar el codi que treballa amb fitxers dins d'un bloc `try`, i gestionar els errors possibles mitjançant un bloc `except`.

Exemple:
```python
try:
    with open('document_inexistent.txt', 'r') as fitxer:
        contingut = fitxer.read()
except FileNotFoundError:
    print("El fitxer no existeix.")
except PermissionError:
    print("No tens permisos per llegir el fitxer.")
```
En aquest exemple, si el fitxer no existeix, Python generarà una excepció `FileNotFoundError`, i si el fitxer no pot ser llegit per falta de permisos, es generarà una excepció `PermissionError`.

### Ús de `else` i `finally`
Podem afegir un bloc `else` que s'executarà si no es genera cap error, i un bloc `finally` que s'executarà sempre, independentment de si hi ha hagut un error o no.

Exemple complet:
```python
try:
    with open('document.txt', 'r') as fitxer:
        contingut = fitxer.read()
except FileNotFoundError:
    print("El fitxer no existeix.")
except PermissionError:
    print("No tens permisos per llegir el fitxer.")
else:
    print("Fitxer llegit correctament.")
finally:
    print("Operació de fitxer acabada.")
```

!!!note "Pregunta"
        Com podriem fer que esta execució no parara fins que puguerem obrir el fitxer?

!!!note "Pregunta"
        Com podriem fer que si el fitxer no existeix et demane si vols crear-lo abans de seguir?


## 4.5. Creació de fitxers.

En Python, el comportament en intentar crear un fitxer que ja existeix depèn del **mode d'obertura** que fem servir.

## Modes principals

### Mode `'w'` (write / escriure)
```python
with open("fitxer.txt", "w") as f:
    f.write("Hola")
```
- Si `fitxer.txt` **ja existeix**, es **sobreescriu** completament.  
- Si no existeix, es crea un fitxer nou.

### Modo `'x'` (exclusive creation / creació exclusiva)
```python
with open("fitxer.txt", "x") as f:
    f.write("Hola")
```
- Si `fitxer.txt` **ja existeix**, Python llença un **`FileExistsError`**.  
- Si no existeix, es crea un fitxer nou.

### Modo `'a'` (append / afegir al final)
```python
with open("fitxer.txt", "a") as f:
    f.write("Hola")
```
- Si existeix, es **afegeix el contingut al final** del fitxer.  
- Si no existeix, es crea un fitxer nou.

## Resum ràpid

| Mode | Comportament si el fitxer existeix | Comportament si no existeix |
|------|-----------------------------------|-----------------------------|
| `'w'` | Sobreescriu | Crea |
| `'x'` | Error (`FileExistsError`) | Crea |
| `'a'` | Afegeix al final | Crea |




## 4.6. Organització de fitxers i ús de directoris

Els fitxers poden ser organitzats en **directorios** (carpetes), que són contenidors que agrupen fitxers relacionats. El sistema de fitxers de l'ordinador s'organitza jeràrquicament en una estructura d'arbre, on els fitxers i directoris estan emmagatzemats dins d'altres directoris.

En Python, podem gestionar directoris utilitzant el mòdul `os` o `pathlib`, que ho vorem en l'apartat 6. Llibreries.

---

## 4.7. Exemple complet de treball amb fitxers en Python

En aquest exemple, crearem un fitxer, llegirem les dades, escriurem noves dades al fitxer i gestionarem possibles errors com "fitxer no trobat" o errors en escriure al fitxer.

### Codi complet per obrir, llegir, escriure i gestionar errors:

```python
try:
    # Obrim o creem el fitxer per escriure-hi dades
    with open('document.txt', 'w') as fitxer:
        # Escriure contingut en el fitxer
        fitxer.write("Aquesta és la primera línia.\n")
        fitxer.write("Aquesta és la segona línia.\n")

    print("Dades escrites amb èxit al fitxer.")

except IOError:
    print("S'ha produït un error en obrir o escriure al fitxer.")
    
try:
    # Obrir el fitxer per llegir-hi
    with open('document.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer llegit:")
        print(contingut)

except FileNotFoundError:
    print("El fitxer no existeix. Comprova el nom i la ruta.")
except IOError:
    print("S'ha produït un error en llegir el fitxer.")


# Intentar llegir des d'un fitxer que potser no existeix
try:
    with open('document_inexistent.txt', 'r') as fitxer:
        contingut = fitxer.read()
except FileNotFoundError:
    print("El fitxer no es troba. Cal crear-lo primer.")
except IOError:
    print("S'ha produït un error en obrir el fitxer.")
```