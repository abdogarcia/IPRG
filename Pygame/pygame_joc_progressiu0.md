# Pygame: creació progressiva d'un videojoc

## 1. Introducció

Durant el primer trimestre hem treballat els elements fonamentals de Python: variables, condicionals, bucles, funcions i llistes.

En aquest tema els aplicarem per a crear un videojoc senzill amb **Pygame**, una biblioteca de Python que facilita la creació de jocs en 2D.

No farem el joc complet des del principi. Anirem incorporant conceptes nous de Pygame i, després de cada apartat, els aplicarem al mateix projecte.

### El joc que construirem: *Atrapa la moneda*

El jugador controlarà un personatge amb les fletxes del teclat.

L'objectiu serà:

- moure el jugador per la pantalla;
- impedir que isca de la finestra;
- atrapar monedes per guanyar punts;
- evitar un enemic en moviment;
- jugar durant un temps limitat;
- mostrar la puntuació;
- acabar la partida quan s'esgote el temps.

Més endavant podrem ampliar-lo amb diverses monedes, diversos enemics, imatges, sons o vides.

---

# 2. Instal·lació i importació de Pygame

Pygame no forma part de la biblioteca estàndard de Python, per tant cal instal·lar-lo.

```bash
python3 -m pip install pygame
```

En el programa l'importarem amb:

```python
import pygame
```

Abans d'utilitzar Pygame, inicialitzarem els seus mòduls:

```python
pygame.init()
```

Al final del programa convé tancar-los:

```python
pygame.quit()
```

---

# 3. Crear una finestra

Podem crear una finestra de 600 píxels d'amplària i 400 d'altura:

```python
import pygame

pygame.init()

finestra = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Atrapa la moneda")

pygame.quit()
```

La instrucció:

```python
pygame.display.set_mode((600, 400))
```

crea la finestra i retorna una superfície (`Surface`) sobre la qual podrem dibuixar.

La guardem en la variable:

```python
finestra
```

## 3.1. Sistema de coordenades

En Pygame, el punt `(0, 0)` es troba a la cantonada superior esquerra.

```text
(0,0) --------------------------> X
  |
  |
  |
  |
  v
  Y
```

Per tant:

- augmentar `x` significa anar cap a la dreta;
- disminuir `x` significa anar cap a l'esquerra;
- augmentar `y` significa baixar;
- disminuir `y` significa pujar.

En una finestra de `600 x 400`, el centre és aproximadament:

```text
(300, 200)
```

---

# 4. El bucle principal del joc

Un videojoc necessita comprovar contínuament què fa l'usuari, actualitzar els objectes i tornar a dibuixar la pantalla.

Per això utilitzarem un `while`.

```python
import pygame

pygame.init()

finestra = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Atrapa la moneda")

rellotge = pygame.time.Clock()

executant = True

while executant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executant = False

    finestra.fill("white")

    pygame.display.flip()

    rellotge.tick(60)

pygame.quit()
```

Aquest és l'esquelet bàsic d'un programa amb Pygame.

## 4.1. Els esdeveniments

Pygame va guardant els esdeveniments que es produeixen:

- prémer una tecla;
- soltar una tecla;
- moure el ratolí;
- fer clic;
- tancar la finestra;
- etc.

Els podem consultar amb:

```python
pygame.event.get()
```

I recórrer-los:

```python
for event in pygame.event.get():
```

Per exemple:

```python
if event.type == pygame.QUIT:
    executant = False
```

detecta que l'usuari ha premut el botó de tancar la finestra.

## 4.2. Esborrar la pantalla

```python
finestra.fill("white")
```

pinta tota la finestra de blanc.

Normalment, en cada volta del bucle:

1. esborrem el fotograma anterior;
2. dibuixem els objectes en la seua nova posició;
3. mostrem el nou fotograma.

## 4.3. Mostrar el fotograma

```python
pygame.display.flip()
```

actualitza la pantalla i mostra allò que hem dibuixat.

Per això l'ordre és important:

```python
finestra.fill("white")
# dibuixem ací
pygame.display.flip()
```

## 4.4. Controlar els FPS

```python
rellotge = pygame.time.Clock()
```

crea un rellotge de Pygame.

Després:

```python
rellotge.tick(60)
```

limita el bucle a un màxim aproximat de **60 voltes per segon**, és a dir, 60 FPS (*frames per second*).

A 60 FPS, cada fotograma dura aproximadament:

```text
1 / 60 = 0,0167 segons
```

Sense aquest límit, el programa intentaria executar el bucle tan ràpid com poguera el processador.

---

# 5. Dibuixar formes

Pygame permet dibuixar formes senzilles.

## 5.1. Cercle

```python
pygame.draw.circle(finestra, "yellow", (300, 200), 20)
```

Els paràmetres principals són:

```python
pygame.draw.circle(superficie, color, centre, radi)
```

Per exemple:

```python
pygame.draw.circle(finestra, "yellow", (300, 200), 20)
```

dibuixa un cercle groc amb:

- centre `(300, 200)`;
- radi `20`.

## 5.2. Rectangle

```python
pygame.draw.rect(finestra, "blue", (100, 100, 50, 50))
```

En aquest cas:

```text
100 -> x
100 -> y
50  -> amplària
50  -> altura
```

## 5.3. Línia

```python
pygame.draw.line(finestra, "black", (50, 50), (400, 300), 5)
```

El `5` indica el gruix de la línia.

## 5.4. Colors

Podem utilitzar alguns noms:

```python
"red"
"blue"
"green"
"yellow"
"white"
"black"
```

o valors RGB:

```python
(255, 0, 0)       # roig
(0, 255, 0)       # verd
(0, 0, 255)       # blau
(255, 255, 255)   # blanc
(0, 0, 0)         # negre
```

---

# 6. Primera versió del joc

Dibuixarem:

- el jugador: un rectangle blau;
- la moneda: un cercle groc.

```python
import pygame

pygame.init()

finestra = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Atrapa la moneda")

rellotge = pygame.time.Clock()

executant = True

while executant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executant = False

    finestra.fill("white")

    pygame.draw.rect(finestra, "blue", (100, 100, 50, 50))
    pygame.draw.circle(finestra, "yellow", (400, 200), 20)

    pygame.display.flip()
    rellotge.tick(60)

pygame.quit()
```

### Prova

Modifica les coordenades del jugador i de la moneda i observa què ocorre.

---

# 7. Detectar el teclat

Per saber quines tecles estan premudes en aquest moment podem fer:

```python
tecles = pygame.key.get_pressed()
```

I consultar una tecla:

```python
if tecles[pygame.K_RIGHT]:
    x += 3
```

Algunes constants són:

```python
pygame.K_RIGHT
pygame.K_LEFT
pygame.K_UP
pygame.K_DOWN
pygame.K_ESCAPE
```

## 7.1. Estat del teclat i esdeveniments

No és el mateix:

```python
pygame.key.get_pressed()
```

que:

```python
event.type == pygame.KEYDOWN
```

`get_pressed()` comprova l'**estat actual** del teclat. És apropiat per a una acció contínua, com moure el jugador mentre mantinguem una tecla premuda.

`KEYDOWN` representa un **esdeveniment puntual**: el moment en què una tecla és premuda.

Per exemple, podem tancar el joc en prémer ESC:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        executant = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            executant = False
```

Primer comprovem que l'esdeveniment és `KEYDOWN` i després consultem quina tecla l'ha provocat amb `event.key`.

---

# 8. Moure el jugador

Ara guardarem la posició del jugador en variables:

```python
x = 100
y = 100
velocitat = 4
```

Dins del bucle:

```python
tecles = pygame.key.get_pressed()

if tecles[pygame.K_RIGHT]:
    x += velocitat

if tecles[pygame.K_LEFT]:
    x -= velocitat

if tecles[pygame.K_UP]:
    y -= velocitat

if tecles[pygame.K_DOWN]:
    y += velocitat
```

I el dibuixarem en la nova posició:

```python
pygame.draw.rect(finestra, "blue", (x, y, 50, 50))
```

### Joc: versió 2

Modifica el programa perquè el jugador es puga moure amb les quatre fletxes.

Observa especialment que:

```python
y -= velocitat
```

fa pujar el jugador.

---

# 9. `pygame.Rect`

Treballar amb quatre dades separades:

```text
x, y, amplària, altura
```

és molt habitual. Pygame disposa d'un objecte específic per representar un rectangle:

```python
jugador = pygame.Rect(100, 100, 50, 50)
```

Ara podem consultar:

```python
jugador.x
jugador.y
jugador.width
jugador.height
```

Però també:

```python
jugador.left
jugador.right
jugador.top
jugador.bottom
jugador.center
```

Podem moure'l:

```python
jugador.x += 4
```

o:

```python
jugador.y -= 4
```

I dibuixar-lo:

```python
pygame.draw.rect(finestra, "blue", jugador)
```

## 9.1. Evitar que el jugador isca de la finestra

Amb un `Rect` és molt senzill:

```python
if jugador.left < 0:
    jugador.left = 0

if jugador.right > 600:
    jugador.right = 600

if jugador.top < 0:
    jugador.top = 0

if jugador.bottom > 400:
    jugador.bottom = 400
```

### Joc: versió 3

Substitueix les variables `x` i `y` del jugador per un `pygame.Rect` i impedeix que puga eixir de la pantalla.

---

# 10. Límits d'un cercle

Un cercle no té directament propietats com `left` o `right`.

Si el seu centre és:

```python
x = 300
y = 200
radi = 20
```

els seus límits són:

```text
esquerra -> x - radi
dreta    -> x + radi
dalt     -> y - radi
baix      -> y + radi
```

Per exemple:

```python
if x - radi < 0:
    x = radi

if x + radi > 600:
    x = 600 - radi
```

També podem crear un `Rect` que envolte el cercle si necessitem utilitzar les operacions pròpies dels rectangles.

---

# 11. Col·lisions

Un dels avantatges principals de `pygame.Rect` és que facilita la detecció de col·lisions.

Per exemple:

```python
jugador = pygame.Rect(100, 100, 50, 50)
moneda = pygame.Rect(400, 200, 40, 40)
```

Podem comprovar si se solapen:

```python
if jugador.colliderect(moneda):
    print("Has atrapat la moneda!")
```

`colliderect()` retorna `True` quan els dos rectangles se superposen.

Encara que visualment dibuixem la moneda com un cercle, podem utilitzar un rectangle invisible per representar la seua zona de col·lisió:

```python
pygame.draw.circle(finestra, "yellow", moneda.center, 20)
```

### Joc: versió 4

Crea la moneda amb:

```python
moneda = pygame.Rect(400, 200, 40, 40)
```

Dibuixa-la com un cercle i mostra un missatge per terminal quan el jugador la toque.

---

# 12. Posicions aleatòries

Perquè la moneda aparega en un lloc diferent cada vegada necessitarem el mòdul `random`:

```python
import random
```

Quan el jugador toque la moneda:

```python
if jugador.colliderect(moneda):
    moneda.x = random.randint(0, 560)
    moneda.y = random.randint(0, 360)
```

Per què `560` i `360`?

Perquè la moneda ocupa `40 x 40`:

```text
600 - 40 = 560
400 - 40 = 360
```

Així no apareix parcialment fora de la finestra.

### Joc: versió 5

Cada vegada que el jugador toque la moneda, aquesta ha d'aparéixer en una nova posició aleatòria.

---

# 13. Puntuació

Crearem una variable abans del bucle:

```python
punts = 0
```

I quan atrapem una moneda:

```python
if jugador.colliderect(moneda):
    punts += 1

    moneda.x = random.randint(0, 560)
    moneda.y = random.randint(0, 360)
```

Ja tenim una puntuació, però de moment només existeix en una variable. Ens falta mostrar-la en pantalla.

---

# 14. Mostrar text

Primer creem una font:

```python
font = pygame.font.Font(None, 36)
```

El primer paràmetre és el fitxer de font. Amb `None`, Pygame utilitza una font predeterminada.

El segon és la grandària.

Per convertir un text en una superfície que Pygame puga dibuixar:

```python
text_punts = font.render("Punts: 5", True, "black")
```

L'estructura és:

```python
font.render(text, antialiasing, color)
```

El `True` activa l'**antialiasing**, que suavitza les vores de les lletres.

Per mostrar-lo:

```python
finestra.blit(text_punts, (10, 10))
```

`blit()` copia una superfície sobre una altra.

En aquest cas copia `text_punts` sobre `finestra`.

Com que la puntuació canvia, el text s'ha de crear dins del bucle:

```python
text_punts = font.render(f"Punts: {punts}", True, "black")
finestra.blit(text_punts, (10, 10))
```

### Joc: versió 6

Mostra la puntuació a la cantonada superior esquerra.

---

# 15. Mesurar el temps

Pygame pot indicar quants mil·lisegons han passat:

```python
pygame.time.get_ticks()
```

Per exemple:

```python
temps = pygame.time.get_ticks()
```

Si retorna:

```text
5000
```

significa que han passat aproximadament 5 segons.

Podem guardar el moment en què comença la partida:

```python
inici = pygame.time.get_ticks()
```

I després calcular:

```python
transcorregut = pygame.time.get_ticks() - inici
```

Com que el resultat està en mil·lisegons:

```python
segons = transcorregut // 1000
```

---

# 16. Compte arrere

Suposem que una partida dura 30 segons:

```python
duracio = 30
```

Dins del bucle:

```python
transcorregut = (pygame.time.get_ticks() - inici) // 1000
restant = duracio - transcorregut
```

I podem mostrar-lo:

```python
text_temps = font.render(f"Temps: {restant}", True, "black")
finestra.blit(text_temps, (450, 10))
```

Quan s'esgote:

```python
if restant <= 0:
    executant = False
```

### Joc: versió 7

La partida ha de durar 30 segons.

En pantalla han d'aparéixer:

- punts;
- temps restant.

---

# 17. Un enemic en moviment

Afegirem:

```python
enemic = pygame.Rect(250, 300, 60, 40)
vel_enemic = 3
```

Dins del bucle:

```python
enemic.x += vel_enemic
```

Perquè rebote en els costats:

```python
if enemic.left <= 0 or enemic.right >= 600:
    vel_enemic = -vel_enemic
```

La mateixa variable pot valdre:

```text
 3 -> moviment cap a la dreta
-3 -> moviment cap a l'esquerra
```

Quan arriba a un extrem, canviem el signe.

El dibuixem:

```python
pygame.draw.rect(finestra, "red", enemic)
```

### Joc: versió 8

Afig un enemic roig que es moga automàticament d'esquerra a dreta i rebote contra els límits de la pantalla.

---

# 18. Col·lisió amb l'enemic

Podem detectar-la igual que amb la moneda:

```python
if jugador.colliderect(enemic):
    punts -= 1
```

Per evitar perdre molts punts mentre els dos rectangles continuen superposats, podem també reposicionar el jugador:

```python
if jugador.colliderect(enemic):
    punts -= 1
    jugador.topleft = (20, 60)
```

### Joc: versió 9

Quan el jugador toque l'enemic:

- perd un punt;
- torna a la posició inicial.

Decideix també què ha de passar si la puntuació és `0`. Per exemple, podem impedir que es faça negativa.

---

# 19. Organitzar el programa amb funcions

Quan el programa creix, convé dividir-lo.

Per exemple:

```python
def mou_jugador(jugador, velocitat):
    tecles = pygame.key.get_pressed()

    if tecles[pygame.K_RIGHT]:
        jugador.x += velocitat
    if tecles[pygame.K_LEFT]:
        jugador.x -= velocitat
    if tecles[pygame.K_UP]:
        jugador.y -= velocitat
    if tecles[pygame.K_DOWN]:
        jugador.y += velocitat
```

Una altra funció:

```python
def limita_jugador(jugador):
    if jugador.left < 0:
        jugador.left = 0
    if jugador.right > 600:
        jugador.right = 600
    if jugador.top < 0:
        jugador.top = 0
    if jugador.bottom > 400:
        jugador.bottom = 400
```

I una per dibuixar:

```python
def dibuixa(finestra, jugador, moneda, enemic):
    finestra.fill("white")

    pygame.draw.rect(finestra, "blue", jugador)
    pygame.draw.circle(finestra, "yellow", moneda.center, 20)
    pygame.draw.rect(finestra, "red", enemic)

    pygame.display.flip()
```

Així reutilitzem allò que ja sabem de funcions i el programa principal queda més clar.

---

# 20. Diversos objectes amb llistes

Fins ara tenim un únic enemic. Podem aplicar les llistes del primer trimestre per tindre'n diversos:

```python
enemics = [
    pygame.Rect(100, 100, 50, 40),
    pygame.Rect(300, 200, 50, 40),
    pygame.Rect(450, 300, 50, 40)
]
```

Per dibuixar-los:

```python
for enemic in enemics:
    pygame.draw.rect(finestra, "red", enemic)
```

I per comprovar les col·lisions:

```python
for enemic in enemics:
    if jugador.colliderect(enemic):
        print("Col·lisió")
```

També podem crear diverses monedes:

```python
monedes = [
    pygame.Rect(100, 200, 40, 40),
    pygame.Rect(300, 100, 40, 40),
    pygame.Rect(500, 300, 40, 40)
]
```

I dibuixar-les:

```python
for moneda in monedes:
    pygame.draw.circle(finestra, "yellow", moneda.center, 20)
```

Aquesta és una bona oportunitat per aplicar conjuntament:

- llistes;
- `for`;
- objectes `Rect`;
- col·lisions.

---

# 21. Carregar imatges

Una vegada funcione el joc amb formes geomètriques podem substituir-les per imatges.

```python
imatge_jugador = pygame.image.load("jugador.png")
```

Per dibuixar-la:

```python
finestra.blit(imatge_jugador, jugador)
```

Podem redimensionar-la:

```python
imatge_jugador = pygame.transform.scale(imatge_jugador, (50, 50))
```

## 21.1. On ha d'estar la imatge?

Amb:

```python
pygame.image.load("jugador.png")
```

Python busca el fitxer en el directori de treball actual.

Per evitar problemes és convenient construir la ruta a partir de la carpeta on està el programa:

```python
import os

carpeta = os.path.dirname(__file__)
ruta = os.path.join(carpeta, "imatges", "jugador.png")

imatge_jugador = pygame.image.load(ruta)
```

Una estructura possible seria:

```text
joc/
├── joc.py
└── imatges/
    ├── jugador.png
    ├── moneda.png
    └── enemic.png
```

---

# 22. Ratolí

Encara que el nostre joc principal utilitza el teclat, Pygame també permet treballar amb el ratolí.

## 22.1. Posició

```python
x_ratoli, y_ratoli = pygame.mouse.get_pos()
```

## 22.2. Clic

```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos)
```

`event.pos` conté les coordenades del clic.

Podríem utilitzar-lo més endavant per crear botons com:

- Jugar;
- Tornar a començar;
- Eixir.

---

# 23. Estructura típica d'un joc

Ara ja podem veure amb claredat l'estructura habitual:

```python
# Inicialització

while executant:

    # 1. Llegir esdeveniments

    # 2. Llegir teclat o ratolí

    # 3. Actualitzar el joc
    #    - moviment
    #    - temps
    #    - col·lisions
    #    - puntuació

    # 4. Esborrar la pantalla

    # 5. Dibuixar els objectes

    # 6. Mostrar el fotograma

    # 7. Controlar els FPS

# Tancament
```

Aquest esquema és molt més important que memoritzar funcions concretes de Pygame.

---

# 24. Versió completa del joc

Una possible versió final, encara senzilla, és:

```python
import pygame
import random

AMPLARIA = 600
ALTURA = 400

pygame.init()

finestra = pygame.display.set_mode((AMPLARIA, ALTURA))
pygame.display.set_caption("Atrapa la moneda")

rellotge = pygame.time.Clock()
font = pygame.font.Font(None, 36)

jugador = pygame.Rect(20, 60, 50, 50)
moneda = pygame.Rect(400, 200, 40, 40)
enemic = pygame.Rect(250, 300, 60, 40)

velocitat = 4
vel_enemic = 3

punts = 0
duracio = 30
inici = pygame.time.get_ticks()

executant = True

while executant:

    # Esdeveniments
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executant = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                executant = False

    # Moviment del jugador
    tecles = pygame.key.get_pressed()

    if tecles[pygame.K_RIGHT]:
        jugador.x += velocitat
    if tecles[pygame.K_LEFT]:
        jugador.x -= velocitat
    if tecles[pygame.K_UP]:
        jugador.y -= velocitat
    if tecles[pygame.K_DOWN]:
        jugador.y += velocitat

    # Límits del jugador
    if jugador.left < 0:
        jugador.left = 0
    if jugador.right > AMPLARIA:
        jugador.right = AMPLARIA
    if jugador.top < 0:
        jugador.top = 0
    if jugador.bottom > ALTURA:
        jugador.bottom = ALTURA

    # Moviment de l'enemic
    enemic.x += vel_enemic

    if enemic.left <= 0 or enemic.right >= AMPLARIA:
        vel_enemic = -vel_enemic

    # Col·lisió amb la moneda
    if jugador.colliderect(moneda):
        punts += 1
        moneda.x = random.randint(0, AMPLARIA - moneda.width)
        moneda.y = random.randint(50, ALTURA - moneda.height)

    # Col·lisió amb l'enemic
    if jugador.colliderect(enemic):
        if punts > 0:
            punts -= 1
        jugador.topleft = (20, 60)

    # Temps
    transcorregut = (pygame.time.get_ticks() - inici) // 1000
    restant = duracio - transcorregut

    if restant <= 0:
        executant = False

    # Dibuix
    finestra.fill("white")

    pygame.draw.rect(finestra, "blue", jugador)
    pygame.draw.circle(finestra, "yellow", moneda.center, 20)
    pygame.draw.rect(finestra, "red", enemic)

    text_punts = font.render(f"Punts: {punts}", True, "black")
    text_temps = font.render(f"Temps: {restant}", True, "black")

    finestra.blit(text_punts, (10, 10))
    finestra.blit(text_temps, (450, 10))

    pygame.display.flip()

    rellotge.tick(60)

pygame.quit()

print(f"Partida acabada. Puntuació: {punts}")
```

---

# 25. Millora: pantalla de final

En lloc de tancar immediatament la finestra quan s'acaba el temps, podem treballar amb diferents **estats del joc**.

Per exemple:

```python
estat = "jugant"
```

Quan acaba el temps:

```python
estat = "final"
```

I dins del bucle podem distingir:

```python
if estat == "jugant":
    # actualitzar partida

elif estat == "final":
    # mostrar resultat
```

Això permetria mostrar:

```text
FI DE LA PARTIDA
Punts: 12

Prem R per tornar a jugar
Prem ESC per eixir
```

Aquest pas és interessant perquè reutilitza els condicionals estudiats durant el primer trimestre i introdueix una estructura habitual en videojocs.

---

# 26. Possibles ampliacions

Quan el joc bàsic funcione podem introduir millores gradualment:

1. **Diverses monedes**
   - guardar-les en una llista;
   - recórrer-les amb `for`.

2. **Diversos enemics**
   - velocitats diferents;
   - moviment horitzontal o vertical.

3. **Vides**
   - començar amb 3;
   - perdre'n una en tocar un enemic;
   - acabar si arriben a 0.

4. **Nivells**
   - augmentar la velocitat dels enemics;
   - afegir-ne més quan augmenta la puntuació.

5. **Imatges**
   - substituir rectangles i cercles per sprites.

6. **Sons**
   - so en atrapar una moneda;
   - so en col·lidir;
   - música de fons.

7. **Menú inicial**
   - començar en prémer una tecla o un botó.

8. **Millor puntuació**
   - guardar el rècord en un fitxer.

9. **Objectes especials**
   - moneda que val 5 punts;
   - objecte que congela els enemics;
   - objecte que dona temps extra.

10. **Dificultat progressiva**
    - cada 10 punts augmentar la velocitat dels enemics.

---

# 27. Proposta de seqüència de treball

Una possible distribució de les pràctiques és:

| Sessió | Contingut nou | Evolució del joc |
|---|---|---|
| 1 | Pygame, finestra, bucle, FPS | Finestra del joc |
| 2 | Coordenades, colors i formes | Jugador i moneda |
| 3 | Teclat i moviment | Jugador controlable |
| 4 | `pygame.Rect` i límits | No pot eixir de la pantalla |
| 5 | Col·lisions i `random` | Atrapar moneda |
| 6 | Text | Marcador de punts |
| 7 | Temps | Partida amb compte arrere |
| 8 | Moviment automàtic | Primer enemic |
| 9 | Col·lisions amb enemics | Penalitzacions / vides |
| 10 | Funcions | Reorganització del codi |
| 11 | Llistes i `for` | Diversos objectes |
| 12 | Imatges | Aspecte gràfic |
| 13 | Estats del joc | Menú / final / reinici |
| 14+ | Ampliacions | Projecte propi |

---

# 28. Projecte final

A partir del joc desenvolupat a classe, cada alumne o grup haurà de crear una versió pròpia.

El projecte haurà d'incloure almenys:

- una finestra de joc;
- bucle principal;
- control del teclat o ratolí;
- moviment del jugador;
- límits de pantalla;
- almenys un objecte mòbil;
- detecció de col·lisions;
- puntuació;
- temps o vides;
- ús de funcions;
- ús d'almenys una llista;
- pantalla de final de partida.

A partir d'aquest mínim es podran valorar ampliacions com:

- diferents nivells;
- imatges;
- sons;
- menú;
- rècords;
- enemics amb comportaments diferents;
- objectes especials;
- dificultat progressiva.

L'objectiu no és només aprendre Pygame, sinó **aplicar de forma integrada els conceptes de programació treballats durant el primer trimestre**.
