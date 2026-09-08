<h1 style="display:none;"># Inici</h1>

# 3. Fluxos de Dades (Streams)

## 3.1. Què és un flux?

Un **flux de dades** (o **stream**) és un canal a través del qual les dades poden fluir d'un dispositiu a un altre. Els fluxos són utilitzats per gestionar la transferència de dades entre un programa i altres dispositius, com fitxers, xarxes, i altres recursos d'entrada i sortida.

En el context de la programació, un flux representa una seqüència de dades que es poden llegir o escriure de manera seqüencial. Els fluxos permeten que les dades siguin tractades de manera eficient, especialment quan treballen amb arxius de gran mida o en situacions on les dades no poden ser llegides o escrites d'una sola vegada.

### Tipus de Fluxos
Els fluxos es poden classificar principalment en dues categories:
- **Fluxos de caràcters**: S'utilitzen per gestionar dades textuals.
- **Fluxos de bytes**: S'utilitzen per gestionar dades binàries, com imatges o àudio.

## 3.2. Fluxos de bytes vs. Fluxos de caràcters

### Fluxos de Bytes
Els **fluxos de bytes** gestionen dades en format binari. Aquest tipus de flux és necessari quan es treballa amb fitxers binaris, com ara arxius d'imatge, àudio o qualsevol altre tipus de fitxer no textual.

Els fluxos de bytes poden ser utilitzats per llegir o escriure dades en formats que no es poden convertir fàcilment a cadenes de text. Un exemple seria llegir una imatge o escriure dades en un arxiu binari.

Exemple de lectura d'un fitxer binari:
```python
with open('imatge.png', 'rb') as fitxer:
    contingut = fitxer.read()
```
- En aquest cas, el fitxer `imatge.png` es llegeix en mode binari (`'rb'`).

### Fluxos de Caràcters
Els **fluxos de caràcters** gestionen dades textuals. Quan treballes amb fitxers de text o amb la sortida a la pantalla, estàs treballant amb fluxos de caràcters. Aquest tipus de flux és el més comú i adequat per a la majoria de les operacions d'entrada i sortida.

Exemple de lectura d'un fitxer de text:
```python
with open('document.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
```
- En aquest cas, el fitxer `document.txt` s'obre en mode de lectura (`'r'`), i el contingut es llegeix com a cadenes de caràcters.

## 3.3. Funcionament dels fluxos en la transferència de dades

Els fluxos funcionen mitjançant la transferència seqüencial de dades, on les dades es llegeixen o s'escriuen una a una o en blocs. Això permet treballar amb grans volums de dades de manera més eficient, sense haver de carregar tota la informació a la memòria al mateix temps.

### Lectura d'un Flux
Quan llegim un flux de dades, normalment utilitzem mètodes com `read()` o `readline()` per obtenir les dades. El mètode `read()` llegeix tot el contingut del flux, mentre que `readline()` llegeix les dades línia per línia.

Exemple de lectura seqüencial d'un fitxer:
```python
with open('document.txt', 'r') as fitxer:
    linia = fitxer.readline()
    while linia:
        print(linia.strip())  # Mostra cada línia sense els salts de línia
        linia = fitxer.readline()
```
- Aquest codi llegeix el fitxer línia per línia i imprimeix cada línia a la pantalla.

### Escriptura en un Flux
L'escriptura en un flux de dades es fa mitjançant mètodes com `write()` o `writelines()`. El mètode `write()` escriu una cadena de caràcters, mentre que `writelines()` escriu una sèrie de línies de text.

Exemple d'escriptura a un fitxer:
```python
with open('documente_nou.txt', 'w') as fitxer:
    fitxer.write("Aquesta és la primera línia.")
    fitxer.write("Aquesta és la segona línia.")
```
- En aquest exemple, s'escriuen dues línies en el fitxer `documente_nou.txt`.

### Eficiencia amb Fluxos
Els fluxos permeten gestionar grans volums de dades de manera més eficient, ja que no és necessari carregar tot el contingut en memòria de cop. Per exemple, quan es treballa amb fitxers molt grans o quan les dades es transfereixen per xarxa, es pot llegir o escriure en petites porcions (blocs) en lloc de fer-ho tot de cop.

Aquesta capacitat és especialment útil quan es treballa amb fitxers de gran mida que no poden ser carregats completament en la memòria del sistema, com fitxers de vídeo, àudio, o bases de dades.

---
