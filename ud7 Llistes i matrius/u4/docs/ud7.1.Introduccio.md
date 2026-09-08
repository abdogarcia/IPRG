<h1 style="display:none;"># Inici</h1>

# 1. Introducció a les Matrius i Operacions Avançades

## Què són les Matrius?

Les **matrius** són estructures de dades utilitzades per emmagatzemar col·leccions d’elements, com ara nombres o textos, en un format bidimensional o multidimensional. A diferència de les **llistes**, que són estructures unidimensionals, les matrius poden emmagatzemar dades en diverses dimensions, cosa que les fa ideals per representar taules, imatges o qualsevol conjunt de dades que requereixi més d'una coordenada per identificar els seus elements.

En Python, les matrius es poden representar com a **llistes de llistes** o utilitzant biblioteques especialitzades com **NumPy** per obtenir funcionalitats més avançades. Aquestes matrius poden ser **unidimensionals** (també conegudes com a vectors) o **multidimensionals**, amb diverses dimensions (com les matrius 2D, 3D, etc.).

---

## Diferència entre Matrius i Altres Estructures de Dades

Una de les grans diferències entre les **matrius** i les **llistes** és com s’organitzen les dades:

- **Llistes**: Les llistes són estructures de dades **unidimensionals**, és a dir, una sèrie de valors organitzats en una sola fila. Per exemple, una llista de 5 elements es veuria així: `[1, 2, 3, 4, 5]`.

  Exemple de llista:
  ```python
  llista = [1, 2, 3, 4, 5]
  ```
  Les llistes són molt útils quan necessitem emmagatzemar dades en un únic conjunt lineal, però poden ser menys eficients per a representacions més complexes com les matrius.

- **Matrius**: Les matrius són estructures de dades **multidimensionals**, la qual cosa vol dir que els elements es poden organitzar en diverses dimensions. Una matriu de 2 dimensions (2D) seria com una taula amb files i columnes. Les matrius són útils per representar dades més complexes que requereixen més d’una coordenada per accedir a un element.

  Exemple de matriu 2D:
  ```python
  matriu_2D = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  ```
  Les matrius es poden fer servir per representar taules, imatges o altres tipus de dades on la relació entre elements depèn de més d’una coordenada.

### Quan utilitzar una matriu i quan utilitzar una llista?
- **Utilitza llistes** quan tens una **seqüència lineal de dades**, on cada element té un índex únic i no necessites organitzar els elements en diverses dimensions.
- **Utilitza matrius** quan tens **dades que s’han de representar en una taula o en una estructura multidimensional**, com en el cas de taules de dades, imatges, o matrices matemàtiques.

---

## Operacions bàsiques amb Matrius

Les matrius permeten realitzar una sèrie d’**operacions bàsiques**, com ara:

- **Suma i resta**: Podem sumar o restar matrius element per element.
- **Multiplicació**: La multiplicació d’una matriu per un escalar o entre matrius de dimensions compatibles.
- **Transposició**: La **transposició** d’una matriu és una operació que canvia les seves files per les seves columnes.

Aquestes operacions són molt útils quan treballem amb grans quantitats de dades estructurades, com en el processament d’imatges, bases de dades i càlculs científics.

### Exemple de creació d'una matriu unidimensional:
```python
matriu_1D = [1, 2, 3, 4, 5]
```

### Exemple de matriu bidimensional:
```python
matriu_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

## Expressions Regulars per a la Manipulació de Cadenes de Text

Les **expressions regulars** són patrons que ens permeten cercar, reemplaçar i validar cadenes de text. Aquestes són molt útils per a la manipulació avançada de dades textuals, com cercar termes específics dins d’un conjunt de textos o validar formats com adreces de correu electrònic, números de telèfon o codis postals.

En Python, podem utilitzar el mòdul **`re`** per treballar amb expressions regulars. Per exemple, per cercar totes les adreces de correu electrònic en un text, utilitzem una expressió regular per identificar-les i extreure-les.

### Exemple d'expressió regular per cercar un correu electrònic:
```python
import re

text = "Contacta'ns a info@exemple.com o suport@exemple.org."
correus = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', text)

print(correus)
```

---

## Operacions Agregades: Filtració, Reducció i Recol·lecció

Les **operacions agregades** són tècniques per manipular col·leccions de dades, com llistes o matrius. Aquestes operacions inclouen:

- **Filtració**: Seleccionar elements que compleixen una condició específica.
- **Reducció**: Aplicar una operació sobre tots els elements d'una col·lecció, com sumar-los o calcular la mitjana.
- **Recol·lecció**: Transformar els elements d'una col·lecció, com multiplicar-los per un factor o canviar el seu format.

En Python, aquestes operacions es poden realitzar fàcilment utilitzant funcions com `filter()`, `reduce()` i `map()`.

### Exemple de filtració d'una llista de números:
```python
numeros = [1, 2, 3, 4, 5, 6]
numeros_parells = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_parells)
```

---

## Conclusions

Les matrius i les operacions avançades de manipulació de dades són eines potents per treballar amb dades estructurades. En aquesta unitat, hem explorat com utilitzar matrius unidimensionals i multidimensionals, així com les tècniques de manipulació de cadenes de text mitjançant expressions regulars. A més, hem après a aplicar operacions agregades per transformar i analitzar dades de manera eficient.