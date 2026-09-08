
# 5. Control d'Excepcions (C3.4)

## Objectius

- Entendre què són les excepcions i com controlar-les adequadament.
- Aprendre la sintaxi per controlar errors durant l'execució.

## Continguts

### **Què són les excepcions?**

Les **excepcions** són errors que es produeixen durant l'execució d'un programa. Quan una excepció es produeix, el programa s'atura de manera inesperada. Les excepcions poden ser causades per moltes raons, com ara divisió per zero, accés a fitxers que no existeixen o entrada de dades no vàlides per part de l'usuari.

Els llenguatges de programació permeten controlar les excepcions per evitar que el programa es detingui de manera inesperada. Això es fa mitjançant estructures com `try`, `except`, `else` i `finally`.

#### **Tipus comuns d’excepcions:**

- **ZeroDivisionError**: Quan es fa una divisió per zero.
- **ValueError**: Quan una operació rep un valor que no és el que s'esperava (per exemple, convertir un text no numèric a enter).
- **FileNotFoundError**: Quan un fitxer que intentem obrir no existeix.
- **IndexError**: Quan intentem accedir a un índex que no existeix en una llista.

---

### **Sintaxi de `try` / `except`**

La sintaxi bàsica per manejar excepcions és:

```python
try:
    # codi que pot provocar una excepció
except TipusExcepcio:
    # codi que s'executa quan es produeix l'excepció
```

L’estructura de **`try`** intenta executar el codi. Si es produeix una excepció, el flux del programa passa a l'estructura **`except`**, on es pot gestionar l'error.

**Exemple bàsic:**

```python
try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    resultat = num1 / num2
    print("El resultat de la divisió és:", resultat)
except ZeroDivisionError:
    print("No es pot dividir per zero.")
except ValueError:
    print("Per favor, introdueix valors numèrics vàlids.")
```

En aquest exemple, si l'usuari intenta dividir per zero o introdueix un valor no vàlid, es gestionarà l'excepció amb el missatge corresponent.

### **Sintaxi de `else` i `finally`**

Els blocs **`else`** i **`finally`** permeten afegir més control en el maneig d'excepcions.

- **`else`**: S'executa si no es produeix cap excepció.
- **`finally`**: S'executa sempre, independentment de si s'ha produït o no una excepció.

**Exemple de `else` i `finally`:**

```python
try:
    num1 = int(input("Introdueix un número: "))
    num2 = int(input("Introdueix un altre número: "))
    resultat = num1 / num2
except ZeroDivisionError:
    print("No es pot dividir per zero.")
except ValueError:
    print("Per favor, introdueix valors numèrics vàlids.")
else:
    print("El resultat és:", resultat)
finally:
    print("Operació completada.")
```

En aquest exemple, el codi del bloc `else` només s'executarà si no es produeixen excepcions, i el bloc `finally` s'executarà independentment de si s'ha gestionat alguna excepció.

---

### **Exemples pràctics**

1. **Exemple de divisió per zero**:

   Crea un programa que permeti a l'usuari introduir dos nombres i mostrar el resultat de la divisió. El programa ha de capturar l'excepció si l'usuari intenta dividir per zero.

   ```python
   try:
       num1 = int(input("Introdueix el primer número: "))
       num2 = int(input("Introdueix el segon número: "))
       print("El resultat de la divisió és:", num1 / num2)
   except ZeroDivisionError:
       print("No es pot dividir per zero.")
   except ValueError:
       print("Entrada no vàlida. Assegura't de introduir valors numèrics.")
   ```

2. **Exemple de conversió de text a número**:

   Crea un programa que intenti convertir un text a un número enter. Si l'usuari introdueix un text no numèric, el programa haurà de capturar l'error i mostrar un missatge d'alerta.

   ```python
   try:
       text = input("Introdueix un número: ")
       numero = int(text)
       print(f"Has introduït el número {numero}.")
   except ValueError:
       print("Error: El valor introduït no és un número vàlid.")
   ```

---

## Activitats

1. **Exercici pràctic amb `try`/`except`**: Crea un programa que capturi una excepció quan l'usuari introdueixi un valor no vàlid (per exemple, intentar convertir un text a número).

2. **Exercici amb diversos tipus d'excepcions**: Crea un programa que demani dos nombres a l'usuari i realitzi una divisió. Captura les excepcions comunes com divisió per zero i entrada de dades no vàlides.

---

## Criteris d'Avaluació Coberts

- **d)** S’ha escrit codi utilitzant control d’excepcions.