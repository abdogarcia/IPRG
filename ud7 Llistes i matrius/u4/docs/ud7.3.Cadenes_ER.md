<h1 style="display:none;"># Inici</h1>

# 3. Manipulació de Cadenes de Text i Expressions Regulars

Les cadenes de text són un dels tipus de dades més utilitzats en Python. Aquest apartat explica com crear-les, manipular-les i com utilitzar **expressions regulars** per detectar patrons dins de textos.

---

## 3.1 Cadenes de caràcters

### 🔹 Creació i manipulació de cadenes en Python (C6.5)

Les cadenes es poden definir amb cometes simples, dobles o triples.

```python
text1 = "Hola món"
text2 = 'Python és genial'
text3 = """Cadena
multilínia"""
```

Python tracta les cadenes com **seqüències**, per tant es poden indexar i recórrer.

```python
paraula = "Python"
print(paraula[0])   # P
print(paraula[-1])  # n
```

### 🔹 Operacions comunes

#### 1. **Concatenació**

```python
nom = "Inés"
cognom = "García"
print(nom + " " + cognom)
```

#### 2. **Repetició**

```python
print("ha" * 3)   # haha
```

#### 3. **Slicing (tallades)**

Permet obtindre parts d’una cadena.

```python
text = "Programació"
print(text[0:7])   # Program
print(text[5:])    # mació
print(text[:4])    # Prog
```

#### 4. **Cerca de subcadenes**

```python
text = "Avui estudiarem Python"

"Python" in text        # True
text.find("Python")      # retorna la posició
text.startswith("Avui")  # True
text.endswith("Java")    # False
```

#### 5. **Mètodes útils**

```python
text.lower()
text.upper()
text.replace("Python", "Java")
text.split(" ")   # separa per espais
```

---

## 3.2 Expressions Regulars (regex)

### 🔹 Introducció a les expressions regulars (C6.6)

Les **expressions regulars** són patrons que descriuen formes concretes dins d'un text. Són molt útils per a validacions, extracció d’informació o detecció de formats.

En Python utilitzem el mòdul integrat `re`.

```python
import re
```

---

### 🔹 Sintaxi bàsica

| Patró   | Significat               |
| ------- | ------------------------ |
| `.`     | Qualsevol caràcter       |
| `\d`    | Dígit (0–9)              |
| `\D`    | No dígit                 |
| `\w`    | Caràcter alfanumèric     |
| `\s`    | Espai en blanc           |
| `+`     | Una o més repeticions    |
| `*`     | Zero o més repeticions   |
| `{n}`   | Exactament n repeticions |
| `^`     | Inici de línia           |
| `$`     | Final de línia           |
| `[...]` | Conjunt de caràcters     |

---

### 🔹 Coincidència de patrons

```python
import re
text = "El meu telèfon és 678-123-456"

patro = r"\d{3}-\d{3}-\d{3}"
resultat = re.search(patro, text)

print(resultat.group())
```

---

### 🔹 Agrupaments

Permeten capturar parts del patró.

```python
text = "Data: 23/11/2025"
patro = r"(\d{2})/(\d{2})/(\d{4})"
match = re.search(patro, text)

print(match.group(1))  # dia
print(match.group(2))  # mes
print(match.group(3))  # any
```

---

## Exercicis pràctics

### 📝 Exercici 1: Validar que un text és un correu electrònic

**Entrada:** "[prova@gmail.com](mailto:prova@gmail.com)"

Crea una expressió regular que comprove:

* text alfanumèric
* símbol `@`
* domini amb `.`

### 📝 Exercici 2: Buscar tots els números dins d’un text

```python
text = "Tinc 3 gats, 1 gos i 12 peixos"
```

Extraure `[3, 1, 12]`.

### 📝 Exercici 3: Validar un número de telèfon espanyol

Format esperat: `600-123-456`

### 📝 Exercici 4: Detectar paraules que comencen per majúscula

---

