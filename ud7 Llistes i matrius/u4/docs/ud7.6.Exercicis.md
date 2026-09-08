<h1 style="display:none;"># Inici</h1>
<style>
    .md-typeset h2{
        font-weight: bold!important;
    }
</style>

# Exercici 1: Creació de matrius unidimensionals i multidimensionals [6.a]

1. Crea un **vector** amb els següents valors de temperatura: `[23, 25, 19, 30, 21]`.
2. Crea una **matriu 2x3** amb els següents valors:
   ```
   [[1, 2, 3],
    [4, 5, 6]]
   ```
3. Crea una **matriu 3x2x2** (3 blocs, 2 files, 2 columnes) amb els números de l'1 al 12.
4. Mostra el primer element del vector, la segona fila de la matriu 2x3 i el segon element del segon bloc de la matriu 3D.

---

# Exercici 2: Operacions bàsiques entre matrius [6.b]

Treballant amb NumPy, i donades les matrius:

```python
A = np.array([10, 20, 30])
B = np.array([1, 2, 3])
M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])
```

1. Calcula element a element:
      - `A + B`
      - `A - B`
      - `A * 2`
      - `B / 2`
2. Calcula la suma de `M1 + M2` i el producte de matrius `M1.dot(M2)`.
3. Mostra la transposició de `M1` i calcula la mitjana de tots els elements de `M2`.

---

# Exercici 3: Diferències entre matrius i altres estructures [6.c]

Tens les vendes de tres productes (A, B, C) durant 4 mesos:

- *Producte A*: [120, 150, 130, 160]
- *Producte B*: [80, 90, 100, 110]
- *Producte C*: [200, 180, 220, 210]


Guarda aquestes dades en:

- **Una llista de llistes.** Una llista de llistes és una estructura bidimensional: cada subllista representa un producte amb les seves vendes. Digues com **accediries al element** 100 del producte B (en comentaris)

- **Un diccionari amb claus 'A', 'B', 'C'.** Un diccionari permet identificar cada producte per nom, fent el codi més llegible. Digues com **accediries al element** 100 del producte B (en comentaris)

- **Una matriu NumPy 3x4.** Una matriu NumPy és la més adequada per operacions vectorials: sumar files, columnes, calcular mitjanes… Digues com **accediries al element** 100 del producte B (en comentaris) i com trauries el **total de cada producte**

---

# Exercici 4: Expresions regulars i iteració en cadenes. [6.d i 6.f]

Tens un text amb informació de contactes:

```python
text = """
Contactes:
Nom: Inés García, Correu: ines.garcia@gmail.com, Telèfon: 678-123-456
Nom: Carlos Pérez, Correu: carlos_perez@hotmail.com, Telèfon: 612-987-321
Nom: Maria López, Correu: maria.lopez@empresa.es, Telèfon: 619-456-789
"""
```

## Tasques

### 1️⃣ Extreu tots els correus electrònics
Utilitza **expressions regulars** (`re.findall`) per obtenir una llista amb tots els correus del text.

### 2️⃣ Extreu tots els números de telèfon
Els números estan en format `XXX-XXX-XXX`. Crea una llista amb aquests números utilitzant regex.

### 3️⃣ Comptar aparicions del nom "Inés"
Utilitza indexació o mètodes de cadenes (`count`, `find`) per determinar quantes vegades apareix el nom "Inés" dins del text.

### 4️⃣ Crear una llista amb tots els noms
Crea una llista amb els noms complets de tots els contactes. Pots combinar `split()` amb regex si cal.

### 5️⃣ Transformar els correus a majuscules
Genera una nova llista amb els correus convertits a majuscules.

### 6️⃣ Recórrer la llista de correus
Imprimeix cada correu amb el format:
```
Correu trobat: <correu>
```
### 7️⃣ Filtrar i imprimir els telèfons que comencen amb `61`
Recorre la llista de telèfons amb un bucle `for` i imprimeix només aquells que comencen amb `61`.

## Entrada i sortida esperada (indicativa)

**Correus:**
```
['ines.garcia@gmail.com', 'carlos_perez@hotmail.com', 'maria.lopez@empresa.es']
```

**Telèfons:**
```
['678-123-456', '612-987-321', '699-456-789']
```

**Noms:**
```
['Inés García', 'Carlos Pérez', 'Maria López']
```

**Sortida amb iterador de correus:**
```
Correu trobat: ines.garcia@gmail.com
Correu trobat: carlos_perez@hotmail.com
Correu trobat: maria.lopez@empresa.es
```

**Telèfons que comencen amb 61:**
```
612-987-321
619-456-789
```

-----

*A partir d'ací, anem a treballar amb exercicis corresponents a operacions agregades [6.e i 6.f]*

-----


# Exercici 5: Filtració d’usuaris actius

Ets el responsable d’una aplicació web que gestiona comptes d’usuari. La teva tasca és identificar quins usuaris estan actius i quins tenen més de 18 anys per poder enviar-los notificacions personalitzades.

**Dades:**

```python
usuaris = [
    {"nom": "Anna", "edat": 17, "actiu": True},
    {"nom": "Pau", "edat": 21, "actiu": False},
    {"nom": "Joan", "edat": 15, "actiu": True},
    {"nom": "Clara", "edat": 25, "actiu": True}
]
```

**Tasques:**

1. Filtra només els **usuaris actius**.
2. Filtra els **usuaris majors d’edat** actius.
3. Mostra el resultat final amb nom i edat.

---

# Exercici 6: Resum d’ingressos mensuals d’una botiga online

Ets analista de vendes d’una botiga online i vols obtenir un resum ràpid dels ingressos mensuals per fer un informe econòmic.

**Dades:**

```python
vendes = [1200, 950, 300, 180, 600, 750]
```

**Tasques:**

1. Calcula el **total d’ingressos** amb `reduce()`.
2. Calcula la **mitjana de vendes**.
3. Troba la **venda més alta**.
4. Mostra un missatge resum:

```
Total: XXXX€, Mitjana: XX€, Venda més alta: XXX€
```

---

# Exercici 7: Transformació de dades meteorològiques

**Escenari:**
Treballes en una empresa que ofereix prediccions meteorològiques a diverses ciutats. Necessites convertir les temperatures de Celsius a Fahrenheit per mostrar-les als clients nord-americans.

**Dades:**

```python
celsius = [0, 10, 20, 30, 25]
ciutats = ["Barcelona", "Madrid", "València", "Sevilla", "Bilbao"]
```

**Tasques:**

1. Converteix totes les temperatures a **Fahrenheit** amb `map()`.
2. Crea un **diccionari ciutat → temperatura Fahrenheit** amb `zip()`.
3. Mostra el resultat final amb format:

```
Barcelona: XX°F
València: XX°F
...
```

**Objectiu:** Practicar **recol·lecció de dades i transformació a un nou format**.

---

# Exercici 8: Anàlisi de vendes setmanals

Gestiona les vendes d’una botiga de mobles. Cada fila de la matriu representa una setmana i cada columna un producte. Vols identificar setmanes amb bones vendes i calcular totals per producte.

**Dades:**

```python
matriu_vendes = [
    [5, 12, 8],  # setmana 1
    [7, 3, 14],  # setmana 2
    [10, 11, 9]  # setmana 3
]
productes = ["taula", "cadira", "llit"]
```

**Tasques:**

1. Filtra les **setmanes que tenen algun producte amb vendes superiors a 10**.
2. Calcula les **vendes totals per producte** (sumant columnes).
3. Duplica les vendes de totes les setmanes amb `map()` dins de `map()`.
4. Mostra els resultats finals.

**Objectiu:** Aplicar **filtració, reducció i recol·lecció** sobre dades similars a un entorn de botiga real.

---

# Exercici 9: Productes amb IVA i filtratge

Ets encarregat del departament de preus d’una botiga. Vols afegir l’IVA a tots els productes i seleccionar els més cars per una promoció especial.

**Dades:**

```python
productes = {
    "taula": 50,
    "cadira": 25,
    "sofà": 300,
    "llit": 180
}
```

**Tasques:**

1. Filtra els productes amb **preu superior a 100€**.
2. Aplica un **increment d’IVA del 21%** a tots els productes.
3. Filtra els productes amb **preu final superior a 200€**.
4. Mostra el diccionari final amb noms i preus actualitzats.


---

## Observacions
- No està permés utilitzar bucles `for` per a les operacions indicades amb `map()`, `filter()` o `reduce()`.
