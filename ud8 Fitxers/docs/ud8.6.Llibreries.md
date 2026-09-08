
# 6. Eines i Llibreries per a E/S i Gestió de Dades

## 6.1. Llibreries estàndard per a la gestió de fitxers en el llenguatge

En Python, la llibreria estàndard proporciona diverses eines útils per gestionar fitxers i dades d'entrada/sortida (E/S). A continuació, revisarem algunes de les llibreries més importants per a la gestió de fitxers i la manipulació de dades en diversos formats.

### Mòdul `os` i `pathlib`
Els mòduls `os` i `pathlib` permeten gestionar fitxers i directoris dins del sistema de fitxers. Amb aquests mòduls, podem crear, eliminar, moure fitxers i directoris, llistar el contingut dels directoris i molt més.

#### Exemple amb `os`:
```python
import os

# Crear un directori
os.mkdir('nou_directori')

# Llistar fitxers en un directori
fitxers = os.listdir('.')
print(fitxers)

# Eliminar un fitxer
os.remove('document.txt')
```

#### Exemple amb `pathlib`:
```python
from pathlib import Path

# Crear un directori
Path('nou_directori').mkdir(parents=True, exist_ok=True)

# Llistar fitxers en un directori
fitxers = list(Path('.').iterdir())
print(fitxers)
```

### Mòdul `json`
El mòdul `json` permet gestionar fitxers JSON, un format comú per a la serialització i deserialització de dades. Aquest mòdul facilita la conversió entre les estructures de dades de Python (com diccionaris i llistes) i el format JSON.

#### Exemple de lectura i escriptura de JSON:
```python
import json

# Llegir dades des d'un fitxer JSON
with open('dades.json', 'r') as fitxer:
    dades = json.load(fitxer)

# Escriure dades a un fitxer JSON
dades_noves = {"nom": "Joan", "edat": 25}
with open('dades_noves.json', 'w') as fitxer:
    json.dump(dades_noves, fitxer, indent=4)
```

### Mòdul `csv`
El mòdul `csv` és útil per llegir i escriure arxius en format CSV (Comma Separated Values). Aquest format és comú per a la manipulació de dades tabulars, com les fulles de càlcul.

#### Exemple de lectura i escriptura de fitxers CSV:
```python
import csv

# Llegir un fitxer CSV
with open('dades.csv', 'r') as fitxer:
    lector_csv = csv.reader(fitxer)
    for fila in lector_csv:
        print(fila)

# Escriure en un fitxer CSV
dades = [["Nom", "Edat"], ["Joan", 25], ["Maria", 30]]
with open('dades_noves.csv', 'w', newline='') as fitxer:
    escriptor_csv = csv.writer(fitxer)
    escriptor_csv.writerows(dades)
```

### Mòdul `shutil`
El mòdul `shutil` proporciona una manera fàcil de treballar amb fitxers i directoris, permetent copiar, moure o eliminar fitxers i directoris.

#### Exemple de còpia de fitxers:
```python
import shutil

# Copiar un fitxer
shutil.copy('document.txt', 'document_copia.txt')

# Moure un fitxer
shutil.move('document.txt', 'nou_directori/document.txt')

# Eliminar un directori
shutil.rmtree('nou_directori')
```

---

## 6.2. Reproducció d'un fitxer d'àudio amb `pygame`

En Python, podem utilitzar la llibreria `pygame` per treballar amb àudio. Aquesta llibreria permet carregar i reproduir fitxers d'àudio com `.mp3` o `.wav`. A continuació, veurem com podem gestionar fitxers d'àudio de manera senzilla.

### Instal·lació de la llibreria `pygame`

Abans de començar, cal instal·lar la llibreria `pygame`. Per fer-ho, només has de fer servir pip:

```bash
pip install pygame
```

### Exemple de codi per reproduir un fitxer d'àudio:

```python
import pygame
import os

# Inicialització de pygame per treballar amb àudio
pygame.mixer.init()

def reproduir_audio():
    try:
        # Demanem el nom del fitxer d'àudio a l'usuari
        fitxer_audio = input("Introdueix el camí del fitxer d'àudio (.mp3 o .wav): ")

        # Comprovem si el fitxer existeix
        if not os.path.exists(fitxer_audio):
            raise FileNotFoundError("El fitxer d'àudio no existeix. Verifica el camí i torna-ho a intentar.")
        
        # Reproduïm el fitxer d'àudio
        pygame.mixer.music.load(fitxer_audio)
        pygame.mixer.music.play()

        # Esperem a que es completi la reproducció
        while pygame.mixer.music.get_busy():  # Mentre el fitxer estigui sonant
            pygame.time.Clock().tick(10)  # Evitar que el programa es tanqui immediatament

    except FileNotFoundError as e:
        print(e)  # Imprimir l'error si el fitxer no es troba
    except pygame.error as e:
        print(f"Error en la reproducció de l'àudio: {e}")
    except Exception as e:
        print(f"Ha ocorregut un error inesperat: {e}")

# Cridem la funció per reproduir un fitxer d'àudio
reproduir_audio()
```

### Explicació del codi:
1. **Inicialització de `pygame.mixer`**: Utilitzem `pygame.mixer.init()` per preparar el sistema d'àudio de `pygame`.
2. **Comprovació de l'existència del fitxer**: Comprovem que el fitxer existeix amb `os.path.exists()`. Si no es troba, llencem una excepció `FileNotFoundError`.
3. **Reproducció de l'àudio**: El fitxer s'afegeix al sistema de reproducció i es fa servir `pygame.mixer.music.play()` per iniciar la reproducció.
4. **Gestió d'errors**: El codi captura errors comuns com que el fitxer no existeixi o si hi ha un error amb el sistema de reproducció.

---

Amb aquestes llibreries de la llibreria estàndard de Python, així com amb llibreries externes com `pygame`, podem gestionar eficientment les operacions d'entrada/sortida i treballar amb diversos formats de fitxers i dades multimèdia. Aquestes eines ens permeten llegir, escriure, modificar i organitzar dades de manera robusta i eficient.