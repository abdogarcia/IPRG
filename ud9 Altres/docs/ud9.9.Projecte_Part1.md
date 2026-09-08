
# Introducció al Projecte: Gestió d'Entrades per a un Esdeveniment

## Descripció del Projecte

En aquest projecte, crearem un sistema de **gestió d'entrades per a un esdeveniment** (per exemple, un concert). El sistema permetrà als usuaris **reservar seients** per a un esdeveniment, **comprovar quins seients estan ocupats o disponibles**, i gestionar errors de manera eficient. El projecte es desenvoluparà de manera progressiva a través de les unitats del curs, i cada unitat afegirà funcionalitats noves al sistema.

### Funcionalitats que es treballaran en aquesta unitat:

1. **Reserva de seients**: Els usuaris podran reservar seients, però el sistema haurà de verificar que el seient no estigui ocupat.
2. **Comprovació de seients disponibles**: Els usuaris podran consultar els seients disponibles o ocupats.
3. **Control d'errors**: El sistema ha de ser capaç de gestionar errors, com la introducció d'un número de seient invàlid.
4. **Traçades per a depuració**: Registra totes les operacions realitzades (com les reserves i els intents fallits).

---

## Seguit del projecte en les unitats posteriors

- **Unitat 2 (Estructures de dades)**: Afegirem l'ús de fitxers per emmagatzemar les dades i estructures de dades més complexes (com diccionaris o llistes de diccionaris) per gestionar millor les reserves.
- **Unitat 3 (Programació Orientada a Objectes)**: Crearem classes i objectes per gestionar les reserves de manera més estructurada i modular.
- **Unitat 4 (Interfície Gràfica d'Usuari)**: Afegirem una interfície gràfica utilitzant biblioteques com `Tkinter`, per millorar la interacció de l'usuari amb el sistema.

---

## Continguts i Criteris d'Avaluació

Aquesta primera unitat es centrarà en el treball de les **estructures de control**, **depuració** i **control d'excepcions**. Els continguts i criteris d’avaluació treballats en aquesta unitat seran els següents:

### **Continguts que es treballaran:**
- **Estructures de selecció**: Utilitzar `if`, `elif`, i `else` per gestionar el flux del programa en funció de condicions.
- **Estructures de repetició**: Aplicar bucles `while` i `for` per gestionar iteracions.
- **Estructures de salt**: Utilitzar `break`, `continue` i `pass` per controlar el flux dins dels bucles.
- **Control d'excepcions**: Utilitzar `try` i `except` per gestionar errors i assegurar que el programa segueix funcionant correctament.
- **Traçades**: Utilitzar el mòdul `logging` per registrar accions i errors del programa.

### **Criteris d'Avaluació coberts:**
- **a)** S'ha escrit i provat codi que fa ús d'estructures de selecció (utilitzant `if`, `elif` i `else`).
- **b)** S'han utilitzat estructures de repetició (com `while` i `for`) per controlar el flux de l'aplicació.
- **c)** S'han reconegut les possibilitats de les sentències de salt (`break`, `continue` i `pass`).
- **d)** S'ha escrit codi utilitzant control d'excepcions per gestionar errors com la divisió per zero o entrades invàlides.
- **f)** S'han provat i depurat els programes, utilitzant tècniques com prints i el depurador `pdb`.
- **g)** S'ha comentat i documentat el codi, utilitzant comentaris i docstrings per explicar les funcions i els blocs de codi.

---

## Com esvaluem cada part del projecte en aquesta unitat?

### 1. **Registre de Seients**:
   - **Criteris d'Avaluació**: S'ha utilitzat una estructura de selecció per comprovar la disponibilitat dels seients i gestionar l'entrada de l'usuari.
   - **Continguts avalats**: 
     - Estructures de selecció (`if`, `elif`, `else`).
     - Control d'excepcions (gestió d'errors de tipus).

### 2. **Comprovació de Seients Disponibles**:
   - **Criteris d'Avaluació**: S'ha utilitzat un bucle per mostrar els seients disponibles i ocupats.
   - **Continguts avalats**: 
     - Estructures de repetició (`while` o `for`).
     - Traçades amb el mòdul `logging` per mostrar l'estat dels seients.

### 3. **Control d'Errors (Introducció d'Entrades Invàlides)**:
   - **Criteris d'Avaluació**: S'ha implementat control d'excepcions per gestionar errors d'entrada incorrecta (per exemple, si l'usuari introdueix un número de seient fora de rang).
   - **Continguts avalats**: 
     - Control d'excepcions (`try` i `except`).
     - Traçades per registrar errors (amb `logging`).

### 4. **Traçades i Depuració**:
   - **Criteris d'Avaluació**: S'ha utilitzat el mòdul `logging` per registrar totes les accions del sistema.
   - **Continguts avalats**: 
     - Traçades per monitoritzar el flux del programa.