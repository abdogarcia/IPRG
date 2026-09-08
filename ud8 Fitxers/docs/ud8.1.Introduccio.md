
<h1 style="display:none;"># Inici</h1>

# 1. Introducció a l'Entrada/Sortida (E/S)

## Què és l'Entrada/Sortida (E/S)?

Les operacions d'**Entrada/Sortida (E/S)** són fonamentals per a qualsevol programa, ja que permeten la **interacció** amb l'usuari i la **persistència de les dades**. La E/S es refereix a la transferència de dades entre el programa i el món exterior (com el teclat, la pantalla o fitxers en disc).

La **E/S** pot ser:

- **Entrada**: Quan el programa rep dades de l'usuari o d'un dispositiu extern, com el teclat, el ratolí, o fitxers.
- **Sortida**: Quan el programa envia dades a l'usuari o a un dispositiu extern, com la pantalla o fitxers de text.

Les operacions d'E/S són imprescindibles perquè permeten que el programa pugui interactuar amb l'entorn de manera dinàmica. Per exemple, quan un usuari introdueix dades a través del teclat o quan un programa escriu resultats en un fitxer.

---

## La Consola com a Mecanisme d'E/S

Una de les formes més bàsiques d'interactuar amb el programa és a través de la **consola**. Aquesta interactua amb l'usuari mitjançant **entrada per teclat** i **sortida per pantalla**. Aquest mecanisme és molt utilitzat perquè és senzill i directe.

### Entrada per Teclat

La **entrada per teclat** es fa mitjançant funcions que permeten llegir dades introduïdes pel **usuari**. Per exemple, en Python, utilitzem la funció `input()` per llegir dades des del teclat. El valor que l'usuari introdueix es guarda com una **cadena de caràcters**.

Exemple:
```python
nom = input("Introdueix el teu nom: ")
print("Hola, " + nom)
```
- En aquest exemple, el programa sol·licita al usuari que introdueixi el seu nom i després el mostra per pantalla.

#### Coses importants sobre `input()`:
- `input()` **sempre retorna una cadena de caràcters**, fins i tot si l'usuari introdueix un número. Si necessitem convertir aquesta entrada en un altre tipus de dada (per exemple, un número), hem de fer servir funcions com `int()` o `float()`.

Exemple de conversió:
```python
edat = int(input("Quants anys tens? "))
```

### Sortida a la Pantalla

La **sortida a la pantalla** és el mecanisme més habitual per mostrar dades a l'usuari. En Python, utilitzem la funció `print()` per mostrar informació al terminal o pantalla. Aquesta funció pot mostrar qualsevol tipus de dada (text, números, llistes, etc.).

Exemple:
```python
print("Benvingut al curs de programació!")
```
- Aquesta instrucció imprimeix el missatge "Benvingut al curs de programació!" a la pantalla.

## Fluxos (Streams) i Tipus de Dades

Els **fluxos** són canals mitjançant els quals les dades poden fluir entre el programa i els dispositius d'E/S. Els fluxos es poden dividir en dues categories principals: fluxos de **bytes** i fluxos de **caràcters**.

### Fluxos de Bytes

Els **fluxos de bytes** gestionen dades en format binari. Aquest tipus de flux s'utilitza quan es treballa amb fitxers binaris, com imatges, àudios o altres arxius que no són de text.

Exemple de lectura d'un fitxer binari:
```python
with open('imatge.png', 'rb') as fitxer:
    contingut = fitxer.read()
```
- `rb` indica que el fitxer s'obre en mode binari per llegir-lo.

### Fluxos de Caràcters

Els **fluxos de caràcters** gestionen dades textuals, com cadenes de caràcters o fitxers de text. Aquest tipus de flux és el més comú per a la sortida a la pantalla i per a llegir/escriure fitxers de text.

Exemple de lectura d'un fitxer de text:
```python
with open('document.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
```
- `r` indica que obrim el fitxer en mode de lectura.

---

## Gestió de Fitxers

El treball amb **fitxers** és una part essencial de la E/S. Un fitxer és un conjunt de dades emmagatzemades en un dispositiu de memòria, com un disc dur. Els fitxers poden ser de text (com arxius `.txt`) o binaris (com imatges o documents en format `.pdf`).

### Obrir i Tancar Fitxers

Per treballar amb fitxers, primer hem d'**obrir** el fitxer. Un cop hem acabat de llegir o escriure, cal **tancar** el fitxer per alliberar els recursos. Utilitzant el context de `with`, Python tancarà automàticament el fitxer quan el bloc de codi hagi acabat.

```python
# Obrir un fitxer en mode lectura
with open('exemple.txt', 'r') as fitxer:
    contingut = fitxer.read()

# El fitxer es tanca automàticament quan sortim del bloc 'with'
```

### Lectura i Escriptura de Fitxers

La **lectura** i **escriptura** de fitxers es fa mitjançant mètodes específics com `read()`, `write()`, i `writelines()`.

### Exemple d'escriptura a un fitxer:
```python
with open('exemple.txt', 'w') as fitxer:
    fitxer.write("Hola món!")
```
- `w` obre el fitxer en mode escriptura, creant el fitxer si no existeix o esborrant-lo si ja existeix.

### Exemple de lectura d'un fitxer:
```python
with open('exemple.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
```

---

## Criteris de Format en la Sortida

La **sortida de dades** no només es limita a mostrar informació simple. Sovint, cal formatar les dades per millorar la presentació o per adaptar-les a un format específic.

### Exemple de Format de Cadenes

En Python, podem utilitzar mètodes com `.format()` o f-strings per controlar com es mostren les dades:

```python
nom = "Joan"
edat = 25

# Utilitzant .format()
print("El meu nom és {} i tinc {} anys.".format(nom, edat))

# Utilitzant f-string
print(f"El meu nom és {nom} i tinc {edat} anys.")
```
- Els **f-strings** (disponibles a partir de Python 3.6) permeten inserir variables directament dins de la cadena de text, fent el codi més net i fàcil de llegir.

---

## Conclusions

La consola és un mitjà senzill i efectiu per a realitzar operacions d'E/S, i els fluxos proporcionen un mètode potent per gestionar la transferència de dades entre el programa i altres dispositius. També hem cobert tècniques bàsiques per la gestió de fitxers i formats de visualització, essencials per fer programes més funcionals i comprensibles.