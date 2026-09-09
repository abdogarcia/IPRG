<h1 style="display:none;"># Inici</h1>

# 7. Algoritmes bàsics

## 7.1. Validar una dada

Un patró molt habitual és **repetir la lectura fins que la dada siga vàlida**.

```text
Demanar dada

Mentre la dada és incorrecta:
    Missatge d’error
    Demanar dada

Treballar amb la dada correcta
```

**Exemple:**

```python
nota = float(input("Nota (0-10): "))

while nota < 0 or nota > 10:
    print("Nota incorrecta.")
    nota = float(input("Torna a introduir-la: "))

print("Nota correcta:", nota)
```

### Exercicis: validació de dada

29. Demana quina hora és (hores i minuts). Quan siga una hora vàlida, mostra el total de minuts transcorreguts des de les 0 hores.

## 7.2. Menú repetitiu

Els menús combinen normalment un `while` amb un `match`. El programa continua fins que l'usuari tria l'opció d'eixir.

```text
Mentre siga cert:
    Mostrar menú
    Demanar opció

    Segons l'opció:
        Executar l'opció seleccionada
        ...
        Si és l'opció d'eixir:
            Eixir del bucle
```

És a dir:

```python
while True:
    print("1. Opció 1")
    print("2. Opció 2")
    ...
    print("0. Eixir")

    opcio = int(input("Tria una opció: "))

    match opcio:
        case 1:
            ...  # Accions de l’opció 1

        case 2:
            ...  # Accions de l’opció 2

        ...

        case 0:
            break
```

### Exercicis: menú repetitiu

30. Programa que, repetidament, mostre un menú amb 4 opcions (**Demanar temperatura / Pujar 1 grau / Baixar 1 grau / Eixir**), que demane per teclat una opció i l'execute. Cada vegada que s'augmente o disminuïsca, també es mostrarà la nova temperatura. Després del bucle es mostrarà quantes vegades s'ha canviat la temperatura.

## 7.3. Obtindre el major de molts números

Fins ara hem vist com obtindre el major de 2 o 3 números. Però com obtenim el major de 100 números? No podem tindre 100 variables i anar comparant-les.

Imaginem que, sense cap ordinador, vull anar preguntant l'edat de tot l'alumnat per a poder saber l'edat màxima. Com ho faria? No he de recordar l'edat de tots (no he de guardar 100 edats en 100 variables), sinó que només necessite saber en cada moment **l'edat de l'alumne actual** i **l'edat màxima obtinguda fins eixe moment**.

Per tant, necessite 2 variables: `edat` (per a guardar l'edat de l'alumne actual) i `maxima` (per a guardar l'edat màxima fins a eixe moment).

L'algoritme seria:

```text
Inicialitzar maxima a la primera edat introduïda

Per cadascun dels altres alumnes:
    Demanar l'edat de l'alumne
    Si eixa edat és major que maxima:
        Canviar maxima a eixa edat
```

En Python:

```python
maxima = int(input("Edat:"))

for i in range(99):
    edat = int(input("Edat:"))

    if edat > maxima:
        maxima = edat

print("Edat màxima:", maxima)
```

Per a l’edat mínima seria el mateix procediment però canviant `>` per `<` i el nom de la variable `maxima` per `minima`.

!!! question "Càlcul del major i menor"
    Llig uns quants números fins que posem el 0. Mostra el major, el menor i la mitjana (el 0 no l’ha de tindre en compte).
