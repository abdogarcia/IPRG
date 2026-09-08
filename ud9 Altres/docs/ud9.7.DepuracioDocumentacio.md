# Depuració i Documentació del Codi (C3.6)

## Objectius

- Aprendre a depurar el codi per detectar i solucionar errors de manera eficaç.
- Comprendre la importància de documentar adequadament el codi.

## Continguts

### **Tècniques de depuració**

La **depuració** és el procés de trobar i solucionar errors o **bugs** en el codi. Per depurar de manera eficaç, és important utilitzar tècniques que permetin identificar els problemes de forma ràpida i senzilla.

#### **Utilització de prints i depuradors**

Un mètode comú per depurar és utilitzar **prints** per a visualitzar els valors de les variables i el flux del programa durant l'execució. A més, **pdb** (Python Debugger) és una eina poderosa que permet depurar el codi pas a pas i analitzar les variables en temps real.

**Exemple de prints per depurar:**

```python
x = 5
y = 0
print(f"Valor de x: {x}, Valor de y: {y}")
resultat = x / y  # Divisió per zero
```

L'ús de prints ajuda a identificar on es produeixen els errors. Però, quan es necessita una depuració més detallada, es poden utilitzar depuradors com pdb.

##### Les traçades

Un mètode comú per depurar utlitzant prints és generar **traçades**. Una **traçada** és una tècnica més avançada que consisteix a registrar les crides a funcions i l'evolució de les variables de manera sistemàtica al llarg de l'execució del programa.


**Exemple de traçades per depurar:**

```python
import traceback

def suma(a, b):
    print(f"Iniciant la funció suma amb a={a} i b={b}")
    resultat = a + b
    print(f"El resultat de la suma és: {resultat}")
    return resultat

def divisio(a, b):
    print(f"Iniciant la funció divisio amb a={a} i b={b}")
    if b == 0:
        print("Error: Divisió per zero!")
        return None
    return a / b

try:
    x = 10
    y = 0
    suma_resultat = suma(x, y)
    divisio_resultat = divisio(x, y)
except Exception as e:
    print(f"S'ha produït un error: {e}")
    traceback.print_exc()  # Mostra l'error complet
```

Les traçades es poden generar de manera automàtica en casos més complexos amb eines com **logging** (per registrar l'activitat d'un programa en un fitxer de log) o el mòdul *trace* de Python per registrar l'execució a un nivell més detallat.

#### Logging

# Ús del mòdul `logging` per registrar activitats

El mòdul **`logging`** és una eina poderosa que ens permet registrar informació, avisos, errors i altres esdeveniments en un programa. Això és útil tant per a la depuració com per a la creació de registres (logs) que permeten monitoritzar l'activitat del sistema.

## Com iniciar el registre

Per començar a utilitzar `logging`, primer cal configurar-lo. Això es fa mitjançant la funció `basicConfig()`, que permet establir la configuració bàsica de com es registraran els missatges (com el nivell de severitat, el format del missatge, el fitxer on es registraran, etc.).

**Exemple de configuració bàsica**:

```python
import logging

# Configuració bàsica del registre
logging.basicConfig(filename='gestio_entrades.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
```

- **filename**: Estableix el nom del fitxer on es guardaran els registres (en aquest cas, 'gestio_entrades.log').
- **level**: Determina el nivell de severitat dels missatges que s'enregistraran. Els valors possibles són:
  - `DEBUG`: Per registrar tots els missatges, incloent informació detallada per depuració.
  - `INFO`: Per registrar missatges informatius (per exemple, quan una tasca es completa amb èxit).
  - `WARNING`: Per registrar advertències que no impedeixen l'execució del programa.
  - `ERROR`: Per registrar errors que poden afectar el funcionament del programa.
  - `CRITICAL`: Per registrar errors greus que aturen l'execució del programa.
- **format**: Especifica com es formatejaran els missatges del registre. En aquest cas, utilitzem una cadena amb el temps (`%(asctime)s`), el nivell (`%(levelname)s`) i el missatge (`%(message)s`).

## Nivells de registre

Els missatges que registrem poden tenir diferents nivells d'importància. Els nivells més comuns són:

- **DEBUG**: Utilitzat per informació detallada per a depuració.
- **INFO**: Utilitzat per missatges informatius sobre l'execució normal del programa.
- **WARNING**: Per advertències, quan alguna cosa no va bé però el programa pot continuar executant-se.
- **ERROR**: Quan hi ha un problema que pot afectar el funcionament del programa.
- **CRITICAL**: Per errors greus que poden aturar el programa.

**Exemple d'ús dels diferents nivells**:

```python
logging.debug("Missatge de depuració")
logging.info("L'usuari ha reservat un seient")
logging.warning("Advertència: El seient ja està ocupat")
logging.error("Error: No es pot dividir per zero")
logging.critical("Error crític: El sistema s'ha aturat inesperadament")
```

## Exemple pràctic de registre amb `logging`

En el sistema de **gestió d'entrades** per al projecte, podríem utilitzar `logging` per registrar accions com la reserva de seients i els errors.

**Exemple de registre d'una reserva de seient**:

```python
import logging

# Configuració de logging
logging.basicConfig(filename='gestio_entrades.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Simulació d'una funció de reserva de seient
def reservar_seient(seient, nom):
    if seient < 1 or seient > 10:
        logging.warning(f"Intent de reserva invàlida: Seient {seient} fora de rang.")
        return "Seient invàlid"
    else:
        logging.info(f"Seient {seient} reservat per {nom}.")
        return f"Seient {seient} reservat correctament per {nom}"

# Prova de reserva
resultat = reservar_seient(5, "Joan")
print(resultat)

# Error a l'intentar reservar un seient invàlid
resultat = reservar_seient(15, "Maria")
print(resultat)
```

**Fitxer de registre generat (gestio_entrades.log):**

```
2025-09-03 12:00:00,001 - INFO - Seient 5 reservat per Joan.
2025-09-03 12:00:05,001 - WARNING - Intent de reserva invàlida: Seient 15 fora de rang.
```

## Registre d'errors

Quan es produeix un error, podem registrar-lo com a **ERROR** o **CRITICAL** per identificar fàcilment els problemes en l'execució del programa.

**Exemple de registre d'error**:

```python
try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    resultat = num1 / num2
except ZeroDivisionError:
    logging.error("Error: Divisió per zero!")
    print("No es pot dividir per zero!")
except ValueError:
    logging.error("Error: Entrada no vàlida.")
    print("Has d'introduir un número enter.")
```



#### **Utilització de pdb per depurar el codi**

**pdb** és un depurador interactiu que permet aturar l'execució del codi i analitzar el flux, les variables i les funcions pas a pas.

* Exemple bàsic de pdb:

```python

import pdb

x = 10
y = 0
pdb.set_trace()  # S'atura l'execució aquí per depurar
resultat = x / y

```

Quan es crida pdb.set_trace(), el programa s'atura i permet a l'usuari interactuar amb el depurador. Es poden examinar les variables, continuar amb l'execució o fer altres accions.


!!! note "Pregunta d'investigació"
    Visual Studio Code inclou moltes extensions. Investiga si:
        - Hi ha alguna extensió que facilite la depuració del codi.
        - Podem depurar el codi amb alguna d'estes extensions sense usar pdb.


### Documentació del codi 

Una part essencial del desenvolupament de programari és la documentació del codi. Comentar el codi i utilitzar docstrings ajuda altres desenvolupadors (i a tu mateix) a comprendre el que fa cada part del codi.

#### Comentaris clars i útils

Els comentaris han de ser clars i proporcionar explicacions útils del codi. Un bon comentari explica per què es fa alguna cosa, no només què es fa.

Exemple de comentaris:

# Calcula la suma dels dos números
```python
suma = a + b  # a és el primer número, b és el segon número
```

#### Docstrings per documentar funcions i mòduls

Els docstrings són cadenes de text que es col·loquen immediatament després de la definició d'una funció o mòdul. S'utilitzen per **descriure què fa una funció, quins arguments rep i què retorna.**

Exemple de docstring:

```python

def suma(a, b):
    """
    Aquesta funció retorna la suma de dos números.

    :param a: El primer número a sumar.
    :param b: El segon número a sumar.
    :return: La suma de a i b.
    """
    return a + b

```

El docstring ajuda qualsevol persona que llegeixi el codi a entendre ràpidament què fa la funció i com s'ha de fer servir.

##### Exemples pràctics

- Exemple de depuració amb print:

        Crea un programa que demani dos números a l'usuari i imprimeixi el resultat de la divisió, utilitzant prints per depurar qualsevol error.

- Exemple de depuració amb pdb:

        Crea un programa amb una divisió i utilitza el depurador pdb per analitzar els valors de les variables i el flux del codi.

- Exemple de documentació amb docstrings:

        Crea una funció per calcular l'àrea d'un cercle i documenta-la utilitzant un docstring.

### Activitats

- **Exercici pràctic amb depuració:**

        Crea un programa que faci càlculs matemàtics i utilitza prints i pdb per depurar el codi en cas d'errors.

- **Exercici de documentació:**

        Crea un programa que calculi la mitjana de diverses notes i utilitza comentaris i docstrings per documentar el codi.

## Criteris d'Avaluació Coberts

- **f)** S’han provat i depurat els programes.
- **g)** S’ha comentat i documentat el codi.

