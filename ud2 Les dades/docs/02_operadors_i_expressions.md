# 2.3 Operadors i expressions

Podem fer operacions amb les dades d’un programa: sumar-les, comparar-les, combinar condicions, treballar amb text, etc.

Una **expressió** és una combinació de **valors o variables** (operands) i **operadors** que produeix un resultat.

Alguns exemples:

```python
base * altura
edat < 18
(edat >= 18) and (edat < 65)
"Sr. " + nom
```

Els **operadors** són els símbols o paraules que indiquen l’operació que volem realitzar. En este tema vorem principalment operadors **aritmètics**, **relacionals** i **lògics**.

## 2.3.1 Operadors aritmètics

S’utilitzen per a fer operacions matemàtiques amb dades numèriques.

| Operador | Significat | Exemple |
|---|---|---|
| `+` | Suma | `totalFactura + iva` |
| `-` | Resta | `total - descompte` |
| `*` | Producte | `quantitat * preu` |
| `/` | Divisió | `minuts / 60` |

### Prioritat de les operacions

En una expressió amb diversos operadors, Python no executa necessàriament les operacions d’esquerra a dreta.

Per exemple:

```python
print(2 + 3 * 5)
```

mostra:

```text
17
```

Primer es calcula `3 * 5` i després se suma `2`. 

!!! note "Per què s'avalua en eixe ordre?"
    Perquè els llenguatges de programació en general avaluen primer productes i divisions; després, sumes i restes. 
    I si en una expressió hi ha diversos operadors de la mateixa prioritat (per exemple, tot sumes i restes), s'avalua d'esquerra a dreta.

Si volem canviar l’ordre d’avaluació, utilitzem parèntesis:

```python
print((2 + 3) * 5)
```

Ara el resultat és:

```text
25
```

!!! tip
    Davant del dubte, utilitzar parèntesis fa que l’expressió siga més clara i evita errors.

## 2.3.2. Operadors de cadenes

En les cadenes de text podem usar alguns operadors específics:

```python
"Hola " + "Pep"   # "Hola Pep"
"Ha" * 3          # "HaHaHa"
```

## 2.3.3 Operadors relacionals

Serveixen per **comparar dos valors o expressions**. El resultat d’una comparació sempre és un valor lògic: `True` o `False`.

| Operador | Significat |
|---|---|
| `<` | Menor que |
| `>` | Major que |
| `==` | Igual que |
| `!=` | Distint de |
| `<=` | Menor o igual que |
| `>=` | Major o igual que |

Si tenim:

```python
x = 10
y = 20
```

aleshores:

```python
(x + y) < 20    # False
(y - x) <= x    # True
(y - x) >= x    # True
x == y          # False
x != y          # True
```

També podem comparar caràcters i cadenes de text:

```python
'c' < 'f'      # True
'a' == 'A'     # False
```

## 2.3.4 Operadors lògics

Els principals operadors lògics de Python són `not`, `and` i `or`. Treballen amb expressions lògiques i produeixen com a resultat `True` o `False`.

### Operador `not`

`not` nega el valor lògic d’una expressió:

| `x` | `not x` |
|---|---|
| `False` | `True` |
| `True` | `False` |

Exemple:

```python
not (3 < 5)    # False
```

### Operador `and`

El resultat només és `True` quan **les dues expressions són `True`**.

| `x` | `y` | `x and y` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

Exemple:

```python
(3 < 5) and (4 < 2)    # False
```

### Operador `or`

El resultat és `True` quan **almenys una de les dues expressions és `True`**.

| `x` | `y` | `x or y` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

Exemple:

```python
(3 < 5) or (4 < 2)    # True
```

## Negació de comparacions

Algunes expressions amb `not` es poden escriure d’una manera més simple:

| Expressió | Equivalent |
|---|---|
| `not (a < b)` | `a >= b` |
| `not (a <= b)` | `a > b` |
| `not (a == b)` | `a != b` |
| `not (a != b)` | `a == b` |

!!! warning
    Exta expressió:
    ```python
    not (a + b == 0)
    ```
    és equivalent a:
    ```python
    a + b != 0
    ```
    És a dir: quan neguem una comparació, canvia l’**operador relacional**, però NO les operacions aritmètiques que hi haja dins.

## 2.3.5 Lleis de De Morgan

Les **lleis de De Morgan** permeten transformar expressions lògiques, especialment quan un `not` afecta una expressió formada amb `and` o `or`.

### Primera llei

```text
not (A and B)  →  (not A) or (not B)
```

Suposem que la condició per estar en edat laboral és:

```python
edat >= 18 and edat < 65
```

La condició contrària és:

```python
not (edat >= 18 and edat < 65)
```

Aplicant De Morgan:

```python
not (edat >= 18) or not (edat < 65)
```

I simplificant les comparacions:

```python
edat < 18 or edat >= 65
```

### Segona llei

```text
not (A or B)  →  (not A) and (not B)
```

### Doble negació

```text
not (not A)  →  A
```

Per exemple, dir *«no és cert que no plou»* equival a dir *«plou»*.

### Quan hi ha més de dues expressions

Suposem que `plou`, `fred`, `sol` i `humitat` són variables lògiques (guarden valors True o False). 
Esta expressió indicaria la condició de que plou, no fa fred, fa sol i humitat:

```python
plou and not fred and sol and humitat
```

Si volguérem la condició contrària, simplement seria posar un *not* a tot:

```python
not (plou and not fred and sol and humitat)
```

I ara com apliquem De Morgan a tot això? És a dir: com obtenim una expressió equivalent sense el *not* que abarca tota l'expressió?

!!! tip "Regla pràctica per a aplicar De Morgan a tota una expressió"
    Quan un `not` afecta a tota una expressió:
    1. llevem el `not`que abarca tota l'expressió
    2. neguem cadascuna de les parts;
    3. canviem `and` per `or`; i `or` per `and`;
    4. simplifiquem les dobles negacions si n’hi ha.

Per tant, aplicant De Morgan a l'expressió anterior, tindríem::

```python
not(plou) or not(not fred) or not(sol) or not(humitat)
```

I eliminant la doble negació:

```python
not(plou) or (fred) or not(sol) or not(humitat)
```

I ja estaria, encara que podem llevar parèntesis innecessaris:

```python
not plou or fred or not sol or not humitat
```

## 2.3.6 Prioritat dels operadors

Quan en una mateixa expressió apareixen operadors aritmètics, relacionals i lògics, Python els avalua segons una prioritat.

De major a menor prioritat, per als operadors que hem vist:

1. Parèntesis `()`
2. Potència `**`
3. Producte i divisió `*`, `/`
4. Suma i resta `+`, `-`
5. Comparacions `<`, `>`, `<=`, `>=`, `==`, `!=`
6. `not`
7. `and`
8. `or`

!!! tip "Ús de parèntesis"
    Si una expressió és complexa, els parèntesis ajuden a deixar clar l’ordre en què volem que s’avalue, encara que no calguera posar-los.
