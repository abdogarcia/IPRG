<h1 style="display:none;"># Inici</h1>

# 6. Tractament de Documents i Intercanvi de Dades

En aquest apartat es tractaran els documents en formats com JSON, XML i CSV, així com les operacions per manipular i intercanviar dades entre programes. El tractament adequat d'aquests formats és fonamental per desenvolupar aplicacions que interaccionen amb fitxers i serveis web.

---

## 6.1 Manipulació de documents JSON

### 🔹 Què és JSON?

JSON (JavaScript Object Notation) és un format de text lleuger per emmagatzemar i intercanviar dades. És fàcil de llegir per les persones i fàcil d'analitzar i generar per les màquines. Es fa servir principalment per a intercanvis de dades entre aplicacions, especialment en entorns web.

### 🔹 Lectura i escriptura de JSON

Python proporciona el mòdul integrat `json` per treballar amb dades JSON. El mòdul permet convertir objectes Python en cadenes JSON i viceversa.

```python
import json

# Crear un diccionari Python
dades = {"nom": "Laura", "edat": 25, "ciutat": "València"}

# Convertir el diccionari a una cadena JSON
json_dades = json.dumps(dades, indent=4)
print(json_dades)

# Convertir una cadena JSON a diccionari Python
dades_parsejades = json.loads(json_dades)
print(dades_parsejades)
```

### 🔹 Escrivint JSON en un fitxer

```python
import json

# Escrivim un diccionari a un fitxer JSON
dades = {"nom": "Marta", "edat": 30, "ciutat": "Barcelona"}
with open("dades.json", "w") as fitxer:
    json.dump(dades, fitxer, indent=4)
```

### 🔹 Llegeix JSON des d'un fitxer

```python
import json

# Llegim dades JSON des d'un fitxer
with open("dades.json", "r") as fitxer:
    dades_llegides = json.load(fitxer)
    print(dades_llegides)
```

---

## 6.2 Manipulació de documents XML

### 🔹 Què és XML?

XML (Extensible Markup Language) és un llenguatge de marques utilitzat per emmagatzemar i intercanviar dades en un format estructurat i llegible per les màquines. A diferència de JSON, XML utilitza etiquetes per emmarcar les dades.

### 🔹 Lectura i escriptura de XML

Python proporciona la llibreria `xml.etree.ElementTree` per treballar amb fitxers XML. Aquesta llibreria permet crear, modificar i analitzar arbres XML.

```python
import xml.etree.ElementTree as ET

# Crear un element XML
root = ET.Element("persones")
persona1 = ET.SubElement(root, "persona", id="1")
ET.SubElement(persona1, "nom").text = "Joan"
ET.SubElement(persona1, "edat").text = "28"

# Convertir a arbre XML i escriure'l a un fitxer
tree = ET.ElementTree(root)
tree.write("persones.xml")
```

### 🔹 Parseig d'un fitxer XML existent

```python
import xml.etree.ElementTree as ET

# Parseig del fitxer XML
tree = ET.parse("persones.xml")
root = tree.getroot()

# Accedir a les dades
for persona in root.findall("persona"):
    nom = persona.find("nom").text
    edat = persona.find("edat").text
    print(f"Nom: {nom}, Edat: {edat}")
```

### 🔹 Modificar un fitxer XML existent

```python
import xml.etree.ElementTree as ET

# Parseig del fitxer XML existent
tree = ET.parse("persones.xml")
root = tree.getroot()

# Modificar un element
persona2 = root.find("persona[@id='1']")
persona2.find("edat").text = "29"

# Guardar els canvis
tree.write("persones_modificades.xml")
```

---

## 6.3 Manipulació de fitxers CSV

### 🔹 Què és CSV?

CSV (Comma Separated Values) és un format de fitxer simple utilitzat per emmagatzemar dades en taules, on cada línia representa una fila i cada valor dins de la línia està separat per comes (o altres delimitadors com punts i coma). És àmpliament utilitzat en bases de dades i fulls de càlcul.

### 🔹 Lectura i escriptura de CSV

Python proporciona el mòdul `csv` per treballar amb fitxers CSV. Aquest mòdul facilita tant la lectura com l'escriptura de dades en aquest format.

```python
import csv

# Escriure dades en un fitxer CSV
with open("dades.csv", mode="w", newline="") as fitxer:
    writer = csv.writer(fitxer)
    writer.writerow(["Nom", "Edat", "Ciutat"])
    writer.writerow(["Joan", 28, "València"])
    writer.writerow(["Marta", 30, "Barcelona"])

# Llegir dades des d'un fitxer CSV
with open("dades.csv", mode="r") as fitxer:
    reader = csv.reader(fitxer)
    for fila in reader:
        print(fila)
```

### 🔹 Filtrar dades CSV

```python
import csv

# Llegir dades i filtrar
with open("dades.csv", mode="r") as fitxer:
    reader = csv.DictReader(fitxer)
    for fila in reader:
        if int(fila["Edat"]) > 30:
            print(fila["Nom"], fila["Edat"])
```

---
