# UD4. Dades i operacions bàsiques en Python

## 1. Algunes característiques bàsiques de Python

### Sagnat del codi

En Python, el **sagnat** (espais al principi d’una línia) s’utilitza per a indicar quines instruccions formen part d’un mateix **bloc de codi**.
Les instruccions que tenen el mateix nivell de sagnat pertanyen al mateix bloc i s’executaran juntes quan es complisca la condició corresponent.

```python
edat = int(input("Edat:"))

if edat >= 18:
  print("Eres major d'edat")
  print("Pots votar")
else:
  print("Eres menor")
  print("No pots votar")

print("Fi del programa")
```

Encara no hem vist en detall la instrucció `if`, però podem observar que el **sagnat** ens permet identificar els diferents blocs de codi:

- Un bloc, amb dos *print*, que s’executaria si es compleix la condició.
- Un altre bloc, amb altres *print* que s’executaria en cas contrari.

### Comentaris

Els comentaris permeten afegir anotacions al codi: amb `#` per a una línia i entre `'''` per a diverses línies.

```python
# Comentari d'una línia

nom = "Anna" # Comentari al costat del codi

'''
Comentari de diverses línies.
Pot ocupar tantes línies com necessitem.
'''

print(nom)
```

### Noms de variables en Python

- No han de començar per un número

- No poden haver símbols especials ni operadors: \[, !, @, \#, \$, %, \*, ...

- No poden ser paraules reservades: *import, True, False, if, or, in...*

Python és case-sensitive: *edat* i *Edat* són variables diferents.

## 2. Tipus de dades

Les dades que manegen els programes són de distints **tipus**: lletres, números sense decimals, amb decimals... 
Els tipus de Python són:

- `int`: números enters (sense decimals)
- `float`: números amb decimals
- `str`: text (*string*)
- `bool`: lògic o booleà (únics valors: *True*, *False*)

!!! example "Exemple dels tipus de les variables"
    Les variables seran del tipus del valor que se li assignen:
    ```python

    edat = 30           # int

    pes = 74.5          # float (s'usa és el punt decimal, no la coma)

    nom = "Pep Garcia"  # str (també pot anar entre cometes simples)

    casat = True        # bool 
    ```

!!! example "Veiem com d'important pot ser el tipus"
    ```python
    a = 5
    b = 3
    print(a + b)  # 8, ja que ací el ‘+’ suma números

    a = "5"
    b = "3"
    print(a + b)  # "53", ja que ací el ‘+’ concatena cadenes

    a = "5"
    b = 3
    print(a + b)  # ERROR, ja que no es pot sumar ni concatenar un número amb un text
    ```

Python usa **tipificació dinàmica**: una variable pot canviar de tipus en un programa:

!!! example "Exemple de tipificació dinàmica"
    Veiem com en un programa una variable pot canviar de tipus:
    ```python
    ...

    n = 7     # Primera vegada que ix la variable n. Ara la n val 7 Per tant, és int.

    n = 5.67  # Ara n val 5.67. Per tant, ara és float.

    n = 9     # Ara n val 9. Per tant, continua sent int.

    n = n+2   # Ara n 11. Continua sent int.

    n = n/4   # Ara n val 2.75. Per tant, ara n és float.

    n = "Pep" # Ara n és str (cadena)

    ...
    ```

## 3. Operadors

Operadors de Python ordenats de major a menor prioritat dins d’una expressió.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>

<thead>
<tr style="background-color:#c8eeee">
<th>OPERADORS</th>
<th>OBSERVACIONS</th>
</tr>
</thead>

<tbody>

<tr style="background-color:#e9f0df">
<td style="text-align:center">**</td>
<td>Potència. Exemple: 2 ** 3 —&gt; 8.</td>
</tr>

<tr style="background-color:#e9f0df">
<td style="text-align:center; word-spacing: 12px">+x -x</td>
<td>
<p>Signe positiu o negatiu (operadors unaris).</p>
<p>Exemple: descompte = <strong>-</strong>10</p>
</td>
</tr>

<tr style="background-color:#e9f0df">
<td style="text-align:center; word-spacing: 12px">* / // %</td>

<td>
<p>Exemples:</p>
<p>print(21 * 4) # 84 → multiplicació</p>
<p>print(21 / 4) # 5.25 → divisió amb decimals</p>
<p>print(21 // 4) # 5 → divisió entera (arredoneix cap a baix)</p>
<p>print(21 % 5) # 1 → residu de divisió entera</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp(21 dividit entre 5 és 4... i <strong>en sobra 1</strong>)</p>
</td>
</tr>

<tr style="background-color:#e9f0df">
<td style="text-align:center; word-spacing: 12px">+ -</td>
<td>Suma i resta. El + també pot concatenar cadenes.</td>
</tr>

<tr style="background-color:#dce8f5">
<td style="text-align:center; word-spacing: 12px">&lt; &lt;= &gt; &gt;= == !=</td>

<td>Operadors relacionals: menor, menor o igual, major, major o igual, igual i distint.</td>
</tr>

<tr style="background-color:#fae7d5">
<td style="text-align:center">not</td>
<td>Obtén el valor lògic contrari.</td>
</tr>

<tr style="background-color:#fae7d5">
<td style="text-align:center">and</td>
<td>Només és vertader si les dues condicions són vertaderes.</td>
</tr>

<tr style="background-color:#fae7d5">
<td style="text-align:center">or</td>
<td>És vertader si almenys una de les condicions és vertadera.</td>
</tr>

</tbody>
</table>
Els parèntesis poden utilitzar-se per a modificar l’ordre d’avaluació.

### Operador d'assignació

Este operador ja ha aparegut en molts exemples. S'utilitza quan volem assignar un valor a una variable.

!!! example "Exemples d'assignacions"
    Recordem que a l'esquerra es posa la variable on volem guardar el valor, desrpés el `=` i després el valor que volem guardar.
    ```python
    x = 10        # x ara valdrà 10

    y = 20        # y ara valdrà 20

    x = y/2 + 3   # x ara ja no valdrà 10, sinó 13.0

    y = x + y//2  # y ara ja no valdrà 20, sinó 23.0
    ```

Si volem **assignar el mateix valor a diverses variables**, podem fer-ho
en una sola instrucció:

```python
a = b = c = d = 0
```

### Operadors d'assignació reduïts

Els operadors `+=` i `-=` permeten modificar el valor d'una variable utilitzant el seu valor actual, sense haver de repetir el nom de la variable. És a dir:

| Operador reduït| Equivalència |
|----------|--------------|
| `x += valor` | `x = x + (valor)` |
| `x -= valor` | `x = x - (valor)` |

Així evitem repetir el nom de la variable.

!!! example "Exemple d'ús d'operadors reduïts"

    ```python
    x = 7
    y = 4

    x += 2
    # Equivalent a: x = x + 2
    # x = 7 + 2   →   x = 9

    x -= 2 + y
    # Equivalent a: x = x - (2 + y)
    # x = 9 - (2 + 4)   →   x = 3
    ```


Altres operadors d’assignació reduïts (no tan freqüents): `*=`, `/=`, `//=`, `%=`, `**=`

!!! question "Exercici sobre operadors"

    1\. En el següent programa Python, què valdrà la variable `a` després de cada assignació?
    ```python

    a = 6
    
    b = 3
    
    a = 2 + b         # a =
    
    a += 2            # a =
    
    a -= 2 + b        # a =
    
    a = b // a + 1    # a =
    
    a = 10 % 3        # a =
    ```

## 4. Expressions

Ja veiérem que una **expressió** combina **dades** i **operadors**. I també tractàrem els tipus de dades d'una dada o d'una expressió.
A vegades convindrà canviar el tipus d'una expressió. Veiem per què i com fer-ho en Python.

### Conversió de tipus d’una expressió (*càsting*)

Si ens convé, podem convertir el tipus d’una expressió a un altre tipus:

> int( expressió )
>
> float( expressió )
>
> str( expressió )
>
> bool( expressió)

!!! example "Exemples de càsting"
    El càsting pot afectar a una variable o a una expressió:
    ```python
    x = 4.6

    n = int(x) * 2     # n = int(4.6) * 2   --> n = 4 * 2     --> n = 8

    n = int(x * 2)     # n = int(4.6 * 2)   --> n = int(9.2)  --> n = 9

    euros = 10

    print( int(euros * 166.386) ) # Mostrarà 1663 (lleva la part decimal)

    telefon = 961702294 # Ara telefon és enter. Podríem sumar-li números, etc.

    telefon = str(telefon)  # Ara telefon és una cadena (“961702294”). Podríem concatenar, etc.
    ```

    Una utilitat típica de càsting és poder concatenar text amb números:
    ```python

    num = 20

    domicili = "C/ Sequial, número " + num       # Error: + no uneix text amb números

    domicili = "C/ Sequial, número " + str(num)  # Cal usar càsting
    ```

!!! question "Exercicis sobre expressions i tipus"

    2\. Indica què mostrarà en cada *print*

    ```python
    a = 12
    x = 2.5
    y = 0.6
   
    # a)
    print(x + y)

    # b)
    print(int(x) + int(y))

    # c)
    print(int(x + y))

    # d)
    print(a / 4)

    # e)
    print(a // 4)

    # f)
    print(a % 4)

    # g)
    print(a / a - 2)

    # h)
    print(a-2 ** 2)

    # i)
    print(a < x or y < x)

    # j)
    print(not (a < x))

    # k)
    print(a >= x) and (y <= a))
    ```

## 5. Eixida de dades: *print*

Ja hem vist que el print s’usa per a mostrar dades per pantalla. Ara
entrarem en detall.

Exemples:

nom = "Pep"

cog = "Garcia"

print("Hola,", nom, cog) \# 3 arguments. Mostra: Hola, Pep Garcia

print("Hola," + nom + cog) \# 1 argument (textos units). Mostra:
Hola,PepGarcia

Com podem vore, el print:

- Pot rebre una o més dades com a arguments (separats per comes).

- Mostra els arguments separats per 1 espai.

- Al final posa automàticament un salt de línia (és a dir, el *print*
  següent el mostra en altra línia).



### Altres paràmetres del *print*

*print*(objecte/s, ***sep***=separador, ***end***=finalitzador,
***file***=fitxer)

- **objecte/s** → textos, números, variables o expressions que volem
  mostrar (separats per comes)

dies = 3

print("En", dies, "dies hi ha", dies\*24, "hores") \# en 3 dies hi ha 72
hores

- ***sep***=separador → Ací indicarem amb una cadena de caràcters com
  volem que apareguen separats els objectes que mostrem. Si no posem
  res, el separador és un espai en blanc.

print("LÍNIA", "ARTICLE ", "QUANT.", "PREU", "IMPORT", sep="\t")

print("------- --------------- ------- ------- ------")

print(1, "Tomaques", 3, 2.5, 3\*2.5, sep="\t")

print(2, "Peres ", 12.5, 1.5, 12\*1.5, sep="\t")

print(3, "Plàtans ", 2, 2, 2\*2, sep="\t")

- ***end***=finalitzador → Cadena que es mostrarà al final del text. Si
  no posem res, per defecte és ‘\n’. És a dir, fa un intro o salt de
  línia.

print("Hola") \# Després de mostrar, fa un intro

print("Adéu", end = "...") \# Després de mostrar, mostra 3 punts (sense
intro)

print("Pep", end = "") \# Després de mostrar, no fa res (ni intro)

print("Pepa")

> Mostrarà:
>
> Hola
>
> Adéu...PepPepa

- ***file*=fitxer** → Per a enviar l’eixida a fitxer (no per pantalla):

fitxer=open("nomFitxer.txt", "a")

print("Hola, Pep", file = fitxer)

Amb "a" (append) indiquem que el text que fem amb els print s’afegirà al
final del contingut existent del fitxer. Si volguérem substituir el
contingut anterior, utilitzaríem "w" en lloc de "a".

La "x" no matxaca: crea un fitxer nou i dona error si ja existeix.

### Ús de f-strings (cadenes amb format)

Els **f-strings** formar fàcilment una cadena de text barrejant text,
variables i expressions.<span class="mark"></span>

Per exemple, si tenim:<span class="mark"></span>

nom = "Pep"

edat = 56

<span class="mark"></span>

<span class="mark">I vull mostrar per pantalla un text que diga “Em dic
... i soc de l’any...”, ho puc fer de diverses maneres:</span>

1)  <span class="mark">Passant al print diversos paràmetres (separats
    per coma):</span>

<span class="mark">print("Em dic", nom, "i soc del", 2026 - edat)</span>

<span class="mark">b) Passant al print un paràmetre: una cadena que
concatena text i valors:</span>

<span class="mark">print("Em dic " + nom + " i soc del " + str(2026 -
edat))</span>

<span class="mark">c) Usant els f-strings:</span>

print( f"Em dic {nom} i soc del {2026 - edat}") \# Em dic Pep i soc del
1970

<span class="mark"></span>

<span class="mark">És a dir, la sintaxi és:</span>

> <span class="mark">f</span>"... <span class="mark">{valor} ...</span>"

S’escriu una **f** davant de les cometes; i les variables o expressions
van entre claus **{}**.

També podem indicar (amb : ) el format en què volem mostrar-ho:

> <span class="mark">f</span>"<span class="mark">{valor :
> format}</span>"

<span class="mark">En el format podem indicar:</span>

- <span class="mark">En quants espais volem mostrar-ho:</span>

| <span class="mark">f"{nom:8}"</span> | "Pepa " | En un espai de 8, posa el text a l’esquerra |
|--------------------------------------|---------|---------------------------------------------|
| <span class="mark">f"{x:8}"</span>   | " 7"    | En un espai de 8, posa el núm. a la dreta   |

<span class="mark"></span>

- <span class="mark">Si ho volem centrat (^) alineat a esquerra (\>) o a
  dreta(\<), i en quants espais.</span>

| f"{x:\>8}" | " 7"  | Alinea a la dreta, en una amplària de 8   |
|------------|-------|-------------------------------------------|
| f"{x:\<8}" | "7 "  | Alinea a l’esquerra, en una amplària de 8 |
| f"{x:^8}"  | " 7 " | Centra, en una amplària de 8              |

- Quants decimals volem en un float:<span class="mark"></span>

| f"{pi:.2f}" | 3.14 | En un espai de 8, mostra 2 decimals |
|-------------|------|-------------------------------------|

<span class="mark"></span>

- <span class="mark">I podem combinar eixos formats. Per exemple, podem
  centrar en un espai de 10, un número float, amb 3 decimals:</span>

| f"{pi:^8.2f}" | " 3.14 " | En un espai de 8, mostra 2 decimals |
|---------------|----------|-------------------------------------|

<span class="mark"></span>

nom = "Pep"

edat = 30

pi = 3.14159265359

print(f"El meu nom és {nom} i tinc {edat} anys")

print(f"Tinc {edat:\<10} anys") \# Posa el número a l'esquerra dins de
10 caràcters

print(f"Tinc {edat:\>10} anys") \# Posa el número a la dreta dins de 10
caràcters

print(f"Tinc {edat:^10} anys") \# Posa el número centrat dins de 10
caràcters

print(f"Pi és {pi:.2f} aprox") \# Mostra 2 decimals

print(f"Pi és {pi:\>10.2f} aprox") \# Mostra 2 decimals, a la dreta dins
de 10 car.

El resultat seria:

<span class="mark"></span>

Realment, els *f-strings* no estan lligats necessàriament al *print()*.
S’utilitzen per a crear cadenes de text que incorporen dades amb el
format desitjat. Per exemple:

nom = "Pep"

missatge = f"Hola, {nom}!" \# La variable missatge valdrà: “Hola, Pep!”

print(missatge)

### Operacions amb les cadenes (*str*)

<span class="mark">Python disposa de moltes **operacions pròpies de les
cadenes**: convertir-les a minúscules o majúscules, obtindre subcadenes,
eliminar espais, substituir text, alinear el contingut, etc.
Exemples:</span>

<span class="mark">nom = " Pep Garcia "</span>

<span class="mark">nom = nom.strip() \# nom = "Pep Garcia"</span>

<span class="mark">print(nom.upper()) \# PEP GARCIA</span>

<span class="mark">print(nom.lower()) \# pep garcia</span>

<span class="mark">print(nom.count('a')) \# 2</span>

<span class="mark">print(nom.ljust(15, '\_')) \# Pep
Garcia\_\_\_\_\_</span>

<span class="mark">print(nom.rjust(15, '\_')) \# \_\_\_\_\_Pep
Garcia</span>

<span class="mark">print(nom.center(15, '\_'))</span> \# \_\_\_Pep
Garcia\_\_

<span class="mark"></span>

<span class="mark">En **VS Code,** si escrivim un punt després d’una
variable o d’un valor de tipus str, apareix una llista amb els mètodes
disponibles per treballar amb eixa cadena.</span>

<span class="mark">En **Thonny**, si volem vore eixes funcions hem de
polsar Ctrl + Espai després d’escriure el punt:</span>

<span class="mark"></span>

<span class="mark"></span>Hem vist que entre els mètodes disponibles per
a les cadenes estan ljust(), center() i rjust(), que permeten alinear el
text dins d’un espai d’amplària determinada. Per tant, són una
alternativa als especificadors d’alineació dels
f-strings.<span class="mark"></span>

nom = "Pep"

print("Hola", nom.upper(), "com va?"). \# Hola PEP com va?

print("Hola", nom.ljust(10, '\_'), "com va?") \# Hola Pep\_\_\_\_\_\_\_
com va?

print("Hola", nom.center(10, '\_'), "com va?") \# Hola \_\_\_Pep\_\_\_\_
com va?

print("Hola", nom.rjust(10, '\_'), "com va?") \# Hola \_\_\_\_\_\_\_Pep
com va?<span class="mark"></span>

Caràcter que volem usar per a emplenar el lloc buit.

Podríem posar l’espai (‘ ‘) o el que siga.

<span class="mark"></span>

<span class="mark"></span>

<span class="mark"></span>

<span class="mark">O bé, usant f-strings però amb el format propi de les
cadenes (no de l’f-string):</span>

nom = "Pep"

print(f"Hola {nom.upper()} com va?") \# Hola PEP com va?

print(f"Hola {nom.ljust(10, '\_')} com va?") \# Hola Pep\_\_\_\_\_\_\_
com va?

print(f"Hola {nom.center(10, '\_')} com va?") \# Hola \_\_\_Pep\_\_\_\_
com va?

print(f"Hola {nom.rjust(10, '\_')} com va?") \# Hola \_\_\_\_\_\_\_Pep
com va?

<span class="mark"></span>

<span class="mark">També podem aplicar diversos mètodes sobre un mateix
text en una sola instrucció:</span>

<span class="mark">text = " Hola Pep "</span>

<span class="mark">resultat = text.strip().lower().replace("pep",
"món").capitalize()</span>

<span class="mark">print(resultat) \# Hola món</span>

<span class="mark"></span>

<span class="mark">  
</span>

## 6. Entrada de dades: *input* <span class="mark"></span>

Serveix per a que un programa puga demanar dades per teclat. Serà un poc
diferent segons el tipus de dades que volem introduir.

Vegem-ho amb exemples:

### Entrada de text

Ací l'execució espera que li posem per teclat un valor i polsem intro.

El valor introduït es guardarà en la variable *nom*.

print("Com et diuen?")

nom = input()

print("Hola, " + nom +"!")

Ara bé, l'*input* de Python també permet indicar el que estem demanant,
sense haver de fer abans el *print*:

Ací mostrarà el text, i farà l'input normal.

nom = input("Com et diuen?")

print("Hola, " + nom +"!")

Veiem que, en este cas, no ha fet intro (salt de línia) després de
preguntar "Com et diuen?". Si el volem, cal posar-lo manual (caràcter
‘\n’):

nom = input("Com et diuen?\n")

print("Hola, " + nom +"!")

### Entrada de números

El problema és si, en compte de demanar un text per teclat, volem
demanar un número, ja que l'agafarà com a text i no podrem fer
operacions aritmètiques amb ell:

num = input("Dis-me un número: ")

print("El següent número és el ", num + 1) \# Error:

Això provoca l'error:

*"TypeError: can only concatenate str (not "int") to str"*

Això és degut a que *input* sempre retorna un *str*. Per això, en
l'expressió *num + 1* intenta concatenar en compte de sumar. I dona
error perquè no es poden concatenar números sinó textos.

Per tant, si volem fer tractar-lo com a enter caldrà fer un *càsting*
(conversió de tipus):

num = input("Dis-me un número: ")

num = int(num) \# Ací fem el càsting o conversió de tipus

print("El següent número és el ", num + 1)

Però és millor fer l'*input* i el càsting en la mateixa instrucció:

num = int( input("Dis-me un número: ") ) \# Es fa càsting sobre
l'entrada de dades

print("El següent número és el ", num + 1)

En compte d'*int* també es podria fer el càsting a *float*, si fora el
cas.

### Diverses entrades en un mateix *input*:

En un input podem demanar diverses dades separades per un espai en blanc
(o pel caràcter que vullgam). Ara bé: això no té res a vore amb l'input,
sinó amb el mètode ***split*** del tipus de dades *str*. Veiem uns
exemples:

horaCompleta = input("Dis-me quina hora és (en format h:m:s): ")

hores, minuts, segons = horaCompleta.split(":")

*split* separa una cadena en una llista de cadenes (a partir del
separador ‘:’).

*Si en split* no indiquem el separador, per defecte és l’espai ‘ ‘.

Fem 3 assignacions alhora.

pes, altura = input("Dis-me el pes i altura (separats per blanc):
").split()

Veiem que quan fem *split*, en l'assignació cal posar tantes variables
com dades s'espera que s'introduïsquen. Si no, donarà error.

I, si fora el cas, caldria fer els càstings corresponents a *int* o
*float* de cada variable.

Exercicis sobre entrada i eixida de dades

3\. Fes un programa que pregunte quants anys té algú i que mostre per
pantalla la quantitat d’anys que falten per a la majoria d’edat i per a
jubilar-se.

4\. Programa que pregunte per la base i l’altura d’un triangle i mostre
per pantalla l’àrea d’eixe triangle.

5\. Demana per teclat les dades de 2 llibres: títol, autor i preu
(permet decimals). Després cal mostrar les dades en forma de taula: 30
caràcters per al títol, 20 per a l'autor i 10 per al preu (incloent 2
decimals i alineat a dreta). Per exemple:

> Diccionari per a ociosos Joan Fuster 9.90

L'home manuscrit Manuel Baixauli 21.25

6\. Demana per teclat només un valor: una data (per exemple: 6/9/2024).
Després escriu eixa data però amb el format: "6 del 9 de
2024".<span class="mark"></span>

7\. Exercicis

7.  Escriu el resultat de les següents expressions:

<!-- -->

1)  5 / 2 + 17 % 3

2)  (8 / 2 \* 3) / 2 - int(28.7) // 4 + 29 % 3 \* 4

3)  3 \<= 4

4)  45 \<= 7 or not(5 \>= 7)

5)  (8 \* 2 \< 5 or 7 + 2 \> 9) and 8 - 5 \< 18

6)  (2 \* 7 \> 5 or 7 / 2 == 3) and (7 \> 25 or not True) and True

7)  35 \> 47 and 9 == 9 or 35 != 3 + 2 and 3 \>= 3

8)  9 == 15 or 8 != 5 and 7 == 4

9)  8 \> 8 or 7 == 7 and not(5 \< 5)

10) 4 + 2 \< 8 and 24 + 1 == 25 or True

<!-- -->

8.  Escriu una expressió on s’especifique que una variable numèrica de
    nom *quant* siga menor o igual que 500 i múltiple de 5 però distinta
    de 100.

9.  Troba els errors en el següent programa que calcula l’àrea d’un
    cercle a partir del radi. Després copia'l amb les correccions i
    executa’l per a vore si és correcte.

> print("pi=", pi)
>
> pi = 3,14
>
> print(Programa de càlcul de l’àrea d’un cercle)
>
> radi = input('Dis-me el radi');
>
> '''Calcular i imprimir l’àrea
>
> area = PI \* radio\*\*2;
>
> print('\n\nL'àrea del cercle és: {aera:5.2}\n');

10. Sense executar el programa, digues què mostrarà per pantalla:

> a = 10
>
> b = 3
>
> c = a/b
>
> d = a\<b and c\>2
>
> a -= a + b
>
> b = float(a//b)
>
> print(a, b, c, d)

11. Fes un programa en Python per a calcular el sou d’un treballador:

> \- Demana per teclat el nom del treballador, la quantitat de hores que
> ha treballat i el preu per hora que paga l’empresa.
>
> \- Calcula el sou brut (import que paga l'empresa al treballador)
>
> \- Calcula l'import retingut (import que pagarà el treballador a
> hisenda, sabent que és el 15%).
>
> \- Calcula el sou net (import que s'emporta el treballador).
>
> \- Mostra per pantalla el nom del treballador i les dades calculades
> abans.
