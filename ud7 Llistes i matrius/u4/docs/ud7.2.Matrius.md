<h1 style="display:none;"># Inici</h1>
# 2. Matrius (Arrays) i Matrius Multidimensionals

Les **matrius** (o *arrays*) són estructures de dades molt utilitzades en programació, especialment en entorns científics, tractament d’imatges, estadística i intel·ligència artificial. En Python, el treball amb matrius es realitza principalment mitjançant la llibreria **NumPy**, que ofereix un conjunt d’eines optimitzades i molt eficients.

Aquest tema et proporcionarà una base sòlida per a entendre i manipular matrius d’una i diverses dimensions, realitzar operacions matemàtiques i entendre quan convé utilitzar matrius en lloc de llistes.

---

## 2.1 Creació de matrius unidimensionals i multidimensionals

### 🔹 Què és una matriu?
Una **matriu** és una estructura formada per files i columnes (com una taula). Cada element s’ubica en una posició determinada mitjançant índexs.

A diferència de les llistes, les matrius de NumPy **només poden contenir elements del mateix tipus**, cosa que les fa molt més eficients.

---

### **Creació de matrius d'una dimensió** (Vectors)

```python
import numpy as np

vector = np.array([10, 20, 30, 40])
print(vector)
```

#### Característiques dels vectors
- Només tenen una dimensió.
- Poden representar magnituds com temperatures, notes d’exàmens, etc.
- Es poden manipular de forma vectorial: sumar, restar, multiplicar...

#### Funcions útils
```python
np.zeros(5)      # vector de 5 zeros
np.ones(4)       # vector de 4 uns
np.arange(0,10)  # valors del 0 al 9
np.linspace(0,1,5) # 5 valors entre 0 i 1
```

---

### **Creació de matrius de dues dimensions**

```python
matriu = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matriu)
```

#### Dimensions i forma
```python
matriu.shape  # (2, 3) → 2 files, 3 columnes
matriu.ndim   # 2 → dues dimensions
matriu.size   # 6 → total d'elements
```

---

### **Creació de matrius de tres o més dimensions**
Aquestes matrius s’utilitzen en camps avançats com:
- tractament d’imatges (RGB → 3 dimensions),
- models 3D,
- dades temporals o seqüències.

```python
matriu3D = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
```

Forma: `(2, 2, 2)` → 2 blocs, 2 files per bloc, 2 columnes.

---

### **Accés i manipulació en matrius multidimensionals**

```python
M = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

M[0, 1]      # 20
M[1, 2] = 99 # substitueix 60 per 99
```

#### Accedir a files i columnes
```python
M[0, :]  # Primera fila
M[:, 1]  # Segona columna
```

#### Slicing en matrius
```python
submatriu = M[0:2, 1:3]  # agafa un bloc
```

---

## 2.2 Operacions bàsiques amb matrius

NumPy està optimitzat per realitzar càlcul vectorial i matricial de manera eficient. Les operacions es fan **element a element** de forma automàtica.

### 🔹 Operacions elementals
```python
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(A + B)  # [5 7 9]
print(A - B)  # [-3 -3 -3]
print(A * 2)  # [2 4 6]
print(B / 2)  # [2.  2.5 3. ]
```

---

### 🔹 Operacions amb matrius bidimensionals
NumPy permet fer operacions entre matrius de la mateixa mida de forma immediata.

```python
M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[10, 20], [30, 40]])

print(M1 + M2)
print(M1 * M2)
```

### 🔹 Transposició
```python
M = np.array([[1, 2, 3], [4, 5, 6]])
print(M.T)
```

### 🔹 Producte de matrius (algebra lineal)
Aquest és el producte formal de matrius, no la multiplicació element a element.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

producte = A.dot(B)
print(producte)
```

#### Resultat esperat
```
[[19 22]
 [43 50]]
```

### 🔹 Normes útils
```python
np.sum(M)     # suma total d'elements
np.max(M)     # màxim
np.min(M)     # mínim
np.mean(M)    # mitjana
```

---

## 2.3 Comparativa entre llistes i matrius

### 🔹 Llistes
- Poden contenir tipus diferents.
- Flexibles, fàcils de modificar.
- Operacions matemàtiques manuales i lentes.

### 🔹 Matrius (NumPy)
- Elements sempre del mateix tipus → molt eficient.
- Operacions vectorials instantànies.
- Dissenyades per treball intensiu amb dades.

---

## Quan és més eficient utilitzar una matriu?

### ✔ Quan es treballa amb moltes dades numèriques
Per exemple, un conjunt de 100.000 temperatures.

### ✔ Quan es fan operacions matemàtiques repetitives
Càlcul estadístic, normalitzacions, productes matricials...

### ✔ En ciència de dades, IA i gràfics
- Xarxes neuronals
- Filtrat d’imatges
- Càlcul algebraic

---

### Exemple comparatiu
```python
L = [1, 2, 3, 4]
A = np.array([1, 2, 3, 4])

# Llista
L2 = [x * 2 for x in L]

# Matriu
A2 = A * 2
```

**La versió amb NumPy és molt més ràpida i eficient.**
