
<h1 style="display:none;"># Inici</h1>

# 2. Operacions bàsiques d'Entrada i Sortida a la Consola

## 2.1. Entrada de dades mitjançant el teclat

L'**entrada de dades** a través del teclat és una operació fonamental en qualsevol programa interactiu. En Python, utilitzem la funció `input()` per obtenir dades de l'usuari. El valor retornat per `input()` és sempre una cadena de caràcters, independentment del tipus de dada que l'usuari introdueixi.

Exemple bàsic:
```python
nom = input("Introdueix el teu nom: ")
print("Hola, " + nom)
```
En aquest cas, el programa demana a l'usuari que introdueixi el seu nom i després imprimeix un missatge personalitzat.

### Conversió de tipus de dades

Si l'usuari introdueix un número però necessitem realitzar operacions matemàtiques, hem de convertir la cadena a un tipus numèric.

Exemple de conversió:
```python
edat = int(input("Quants anys tens? "))
```
Aquí, la resposta de l'usuari es converteix en un nombre enter perquè es pugui fer servir en càlculs.

## 2.2. Sortida de dades a la pantalla

La sortida a la pantalla es realitza habitualment mitjançant la funció `print()`. Aquesta funció permet mostrar qualsevol tipus de dada al terminal o pantalla. El més comú és mostrar missatges informatius, resultats de càlculs o altres tipus de dades.

Exemple bàsic:
```python
print("Benvingut al curs de programació!")
```
Aquesta instrucció imprimeix el missatge "Benvingut al curs de programació!" a la pantalla.

### Personalització de la sortida

La funció `print()` permet diversos paràmetres per personalitzar com es mostra la informació. Per exemple, podem utilitzar els paràmetres `sep` i `end` per controlar els separadors entre valors i el que es mostra al final de la línia.

Exemple:
```python
print("Hola", "Món", sep=" ", end="!")
```
En aquest cas:
- `sep=" "` defineix que el separador entre "Hola" i "Món" sigui un espai.
- `end="!"` indica que el caràcter que es mostra al final de la línia serà un signe d'exclamació en comptes d'un salt de línia per defecte.

## 2.3. Aplicació de formats per a la visualització de dades

La personalització de la sortida també pot implicar el format de les dades. Python ofereix diverses maneres de controlar com es mostren els valors.

### Format de cadenes amb `.format()`

Utilitzant el mètode `.format()`, podem inserir variables dins de cadenes de manera més ordenada.

Exemple:
```python
nom = "Joan"
edat = 25
print("El meu nom és {} i tinc {} anys.".format(nom, edat))
```
Aquesta línia imprimeix: `El meu nom és Joan i tinc 25 anys.`.

### F-strings (disponibles a partir de Python 3.6)

Els **f-strings** ofereixen una manera més llegible i senzilla d'inserir variables dins d'una cadena de caràcters.

Exemple:
```python
nom = "Joan"
edat = 25
print(f"El meu nom és {nom} i tinc {edat} anys.")
```
Aquesta línia imprimeix també: `El meu nom és Joan i tinc 25 anys.`. Els f-strings són més eficients i llegibles, especialment en casos on cal inserir moltes variables dins d'una cadena.

### Opció alternativa: Utilitzar concatenació de cadenes

Una altra manera de fer-ho és utilitzant la concatenació de cadenes amb el operador +. Aquesta opció no és tan neta ni tan eficient com les anteriors, especialment quan es treballa amb moltes variables, però és una opció vàlida.

Exemple:

```python
nom = "Joan"
edat = 25
print("El meu nom és " + nom + " i tinc " + str(edat) + " anys.")
```

Aquesta línia també imprimeix: 

```
El meu nom és Joan i tinc 25 anys.
```

- **Contres de la concatenació amb +:**

    - Menys llegible: Quan treballem amb diverses variables, el codi pot resultar menys llegible perquè hem de garantir que totes les parts siguin cadenes (per exemple, **la conversió de edat a cadena amb str(edat)**), a més de que cal tenir en compte els espais entre text i variables.

    - Menys eficient: Si el codi es fa més complex amb moltes concatenacions, el rendiment pot veure's afectat, ja que cada concatenació crea una nova cadena, mentre que .format() i f-strings poden ser més eficients.



## 2.4. Exemple pràctic d'entrada i sortida a la consola

Vegem un exemple pràctic on combinarem l'entrada i la sortida per a realitzar una petita aplicació de càlcul de l'edat.

### Exemple: Càlcul de l'any de naixement

```python
# Demanem l'edat a l'usuari
edat = int(input("Quants anys tens? "))

# Calculem l'any de naixement
any_actual = 2025
any_naixement = any_actual - edat

# Mostrem el resultat
print(f"Si tens {edat} anys, vas néixer al {any_naixement}.")
```

En aquest exemple:
1. L'usuari introdueix la seva edat.
2. El programa calcula l'any de naixement subtraient l'edat de l'any actual.
3. El resultat es mostra a la pantalla amb un missatge personalitzat.

### Casuístiques a tenir en compte:

#### 1. L'usuari introdueix un valor no numèric
- Si l'usuari introdueix un valor que no pot ser convertit a enter, com una cadena de text o un caràcter especial, el programa generarà una excepció `ValueError`.

**Solució:**
Utilitza un bloc `try-except` per capturar errors i tornar a demanar l'entrada de manera correcta.

```python
while True:
    try:
        edat = int(input("Quants anys tens? "))
        break  # Sortir del bucle quan la dada és correcta
    except ValueError:
        print("Per favor, introdueix un número vàlid.")
```

#### 2. L'usuari introdueix una edat negativa
- Si l'usuari introdueix un valor negatiu per l'edat, això podria no ser lògic en la majoria de casos, però el programa no generarà un error perquè `int()` accepta valors negatius. El problema és que l'any de naixement seria incorrecte.

**Solució:**
Afegir una comprovació per assegurar que l'edat sigui un valor positiu.

```python
while True:
    try:
        edat = int(input("Quants anys tens? "))
        if edat < 0:
            print("L'edat no pot ser negativa. Introdueix una edat vàlida.")
        else:
            break  # Sortir del bucle quan l'edat és correcta
    except ValueError:
        print("Per favor, introdueix un número vàlid.")
```

!!!note "ATENCIÓ" 
    No cregueu que es podria fer millor d'altra manera? Vos sona d'algo assert?

#### 3. L'usuari introdueix l'any actual incorrectament
- Si l'usuari vol calcular l'any de naixement manualment, el programa assumeix que l'any actual és correcte (2025). Però si l'usuari introdueix l'any incorrectament, la resta del càlcul serà errònia.

**Solució:**
Afegir la possibilitat de permetre a l'usuari introduir l'any actual.

```python
while True:
    try:
        any_actual = int(input("Quin any és actualment? "))
        break
    except ValueError:
        print("Per favor, introdueix un any vàlid.")
```

#### 4. Format específic
- Potser algú vol un format específic de resultat, com "Vas néixer al 1995. Gràcies per introduir la teva edat!"

**Solució:**
Fer servir el **format de cadenes** per afegir més informació personalitzada.

```python
print(f"Si tens {edat} anys, vas néixer al {any_naixement}. Gràcies per introduir la teva edat!")
```

#### 5. Comprovació de límits d'edat
Si l'usuari introdueix una edat excessivament alta o baixa (per exemple, 200 anys), es pot afegir un control de límits per garantir que els valors siguin realistes.

**Solució:**
Afegir una comprovació de rang per a l'edat.

```python
while True:
    try:
        edat = int(input("Quants anys tens? "))
        if edat <= 0 or edat >= 120:
            print("Per favor, introdueix una edat vàlida entre 1 i 120 anys.")
        else:
            break
    except ValueError:
        print("Per favor, introdueix un número vàlid.")
```
