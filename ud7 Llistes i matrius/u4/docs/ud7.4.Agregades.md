# 4. Operacions Agregades: Filtració, Reducció, Recol·lecció i Combinació

## Introducció

Les operacions agregades són una part fonamental de Python perquè permeten **processar col·leccions de dades (llistes, tuples, diccionaris…) d'una manera clara, ràpida i eficient**. Aquestes operacions són molt utilitzades en programació funcional i en manipulació de dades.

En aquest apartat aprendrem quatre grans tipus d’operacions:
- **Filtració** → quedar-nos només amb els elements que compleixen una condició.
- **Recol·lecció (transformació)** → transformar tots els elements d’una col·lecció en una altra col·lecció.
- **Combinació** → unir diverses col·leccions relacionades.
- **Reducció** → transformar una col·lecció en UN SOL resultat.

A més, veurem aplicacions reals amb **matrius, diccionaris i dades preparades per a fitxers JSON, XML i CSV**.

---

## 4.1 Operacions bàsiques d'agregació

### 🔹 Filtració de dades

La filtració consisteix en **seleccionar elements** d’una seqüència que compleixen una condició.

Hi ha dues formes principals:
- La funció `filter()` serveix per **quedar-se només amb els elements que compleixen una condició**.
    - Necessites una **funció** que retorni `True` o `False` (normalment un `lambda`).
    - I una **seqüència** (llista, tuple, etc.).
  
- **Comprensions de llistes** *(List Comprehensions)*: Forma molt típica i recomanada en Python per crear llistes aplicant una condició.


!!! note "Què és un lambda?"
    Un lambda és una funció **anònima**, sense nom, definida de manera molt compacta per a operacions senzilles.

    ```python
    lambda arguments: expressió
    ```

        - arguments → paràmetres que rep la funció
        - expressió → el càlcul o valor que retorna

        Exemple: comprobar si un número és parell:

        ```python
        parell = lambda n: n % 2 == 0
        print(parell(4))  # True
        print(parell(7))  # False
        ```

#### ✔ Exemple 1: Filtrar només els números parells

**Amb filter():**
```python
nums = [1, 2, 3, 4, 5, 6]
parells = list(filter(lambda n: n % 2 == 0, nums))
print(parells)  # [2, 4, 6]
```

**Amb llistes per comprensió:**
```python
parells = [n for n in nums if n % 2 == 0]
print(parells)  # [2, 4, 6]
```

#### ✔ Exemple 2: Filtrar paraules més llargues de 5 lletres

**Amb filter():**
```python
    paraules = ["python", "sol", "programació", "taula"]
    llargues = list(filter(lambda n: len(n) > 5, paraules))
    print(llargues) # ['python', 'programació']
```


**Amb llistes per comprensió:**
```python
    paraules = ["python", "sol", "programació", "taula"]
    llargues = [p for p in paraules if len(p) > 5]
    print(llargues)  # ['python', 'programació']
```

---

### 🔹 Recol·lecció de dades amb `map()`

`map()` aplica una funció a **tots els elements** d’una seqüència i retorna una nova seqüència transformada.

#### ✔ Exemple 1: Multiplicar tots els elements per 10
```python
nums = [1, 2, 3, 4]
resultat = list(map(lambda x: x * 10, nums))
```

#### ✔ Exemple 2: Passar paraules a majúscules
```python
paraules = ["hola", "python", "classe"]
maj = list(map(str.upper, paraules))
```

---

### 🔹 Reducció de dades amb `reduce()`

La reducció permet **convertir una seqüència de valors en un únic resultat**, aplicant una funció acumulativa.

Per utilitzar-la cal importar-la:
```python
from functools import reduce
```

#### ✔ Exemple 1: Sumar tots els valors d’una llista
```python
from functools import reduce
nums = [1, 2, 3, 4]
suma = reduce(lambda a, b: a + b, nums)
print(suma)  # 10
```

#### ✔ Exemple 2: Calcular el producte de tots els valors
```python
producte = reduce(lambda a, b: a * b, nums)
print(producte)  # 24
```

#### ✔ Exemple 3: Trobar el número més gran
```python
major = reduce(lambda a, b: a if a > b else b, nums)
print(major)  # 4
```

---

### 🔹 Combinació de dades amb `zip()`

`zip()` permet **combinar diverses col·leccions element a element**, creant tuples.  
És una operació fonamental quan treballem amb **dades tabulars**.

#### ✔ Exemple 1: Combinar dues llistes
```python
noms = ["Anna", "Marc", "Laura"]
edats = [28, 35, 42]

persones = list(zip(noms, edats))
```

#### ✔ Exemple 2: Crear diccionaris a partir de zip
```python
persones_dict = list(map(lambda x: {"nom": x[0], "edat": x[1]}, persones))
```

#### ✔ Exemple 3: Zip amb tres columnes (CSV / JSON)
```python
ciutats = ["València", "Alacant", "Castelló"]
dades = list(zip(noms, edats, ciutats))
```

---

## 4.2 Aplicacions de les operacions agregades

### 🔹 Filtrar valors

```python
notes = [3.5, 7.0, 8.2, 4.9, 10]
aprovats = [n for n in notes if n >= 5]
```

```python
usuaris = [
    {"nom": "Anna", "edat": 17},
    {"nom": "Pau", "edat": 21},
    {"nom": "Joan", "edat": 15}
]

majors = [u for u in usuaris if u["edat"] >= 18]
```

---

### 🔹 Reduir llistes

```python
ingressos = [1200, 950, 300, 180]
total = reduce(lambda a, b: a + b, ingressos)
```

```python
paraules = ["gat", "elefant", "ordinador", "sol"]
mes_llarga = reduce(lambda a, b: a if len(a) > len(b) else b, paraules)
```

---

### 🔹 Transformar dades amb `map()`

```python
notes = [5, 7.5, 9]
percent = list(map(lambda n: n * 10, notes))
```

```python
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
```

---

## 4.3 Operacions agregades amb matrius

```python
matriu = [
    [2, 15, 3],
    [20, 5, 7],
    [1, 2, 30]
]

files_valors_alts = [fila for fila in matriu if any(x > 10 for x in fila)]
```

```python
matriu = [[1, 2], [3, 4]]
matriu_x2 = list(map(lambda f: list(map(lambda x: x * 2, f)), matriu))
```

---

## 4.4 Relació directa amb fitxers

Les operacions agregades són claus quan:
- Llegim CSV i combinem columnes amb `zip()`
- Transformem dades abans de guardar-les en JSON amb `map()`
- Filtrarem registres abans d’escriure fitxers
- Calculem totals amb `reduce()`

> Els exercicis següents utilitzen exactament aquestes tècniques.

---

## Resum final

| Operació | Funció | Ús principal |
|--------|--------|--------------|
| Filtració | filter | Seleccionar dades |
| Transformació | map | Canviar format/valor |
| Combinació | zip | Unir columnes |
| Reducció | reduce | Valor únic |
