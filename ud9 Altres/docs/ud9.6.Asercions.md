# 6. Assercions en Python (C3.5)

## **Què són les assercions?**

Les **assercions** són una eina de depuració que es poden utilitzar per verificar que les condicions que es suposa que són certes al llarg de l'execució del programa realment ho siguin.  
Si la condició de l'assert no es compleix, es generarà una excepció, el que ajudarà a identificar el problema abans que es produïsca un comportament inesperat.

Les assercions són especialment útils durant la fase de desenvolupament per garantir que el codi es comporte tal com s'espera.

---

## **Sintaxi d’asserció**

```python
assert expressió, "Missatge d'error"
```

- **`expressió`**: És la condició que s'ha de comprovar.  
- **`Missatge d'error`**: És un missatge opcional que es mostrarà si l'expressió falla.

Si l'**expressió** és falsa, es llançarà una excepció **`AssertionError`** amb el missatge d'error proporcionat.

---

## ⚙️ **Exemple d'asserció**

```python
x = 5
assert x > 0, "El valor de x ha de ser positiu"
```

En aquest exemple, es verifica que `x` siga positiu.  
Si `x` fos negatiu o zero, es llançaria una excepció amb el missatge `"El valor de x ha de ser positiu"`.

---

## **Les assercions llancen excepcions**

Quan una *asser­ció* falla, **Python llança una excepció del tipus `AssertionError`**.  

Això significa que pots capturar-la igual que qualsevol altra excepció amb un bloc `try...except`:

```python
try:
    x = int(input("Introdueix un número positiu: "))
    assert x > 0, "El número ha de ser positiu"
    print("Perfecte!")
except AssertionError as e:
    print(f" Error: {e}")
```

Eixida si l’usuari posa `-3`:
```
Error: El número ha de ser positiu
```

---

## **Quan utilitzar assercions?**

Les assercions són útils per garantir que **les condicions internes del programa** siguen correctes mentre el desenvolupes.  
No estan pensades per validar dades d’usuari finals, sinó per comprovar que el codi funciona com esperes.

- Serveixen per comprovar **invariants** (condicions que sempre han de complir-se).  
- Ajuda a trobar errors lògics durant el desenvolupament.  
- Es poden **desactivar** en mode optimitzat (`python -O`), així que **no s’han d’utilitzar per a validació de seguretat o entrades externes**.

---

## **Diferència entre `assert` i `if` + `raise`**

| Aspecte | `assert` | `if` + `raise` |
|----------|-----------|----------------|
| Ús principal | Depuració i proves internes | Control d'errors i validació d'usuari |
| Pot desactivar-se amb `python -O` | ✅ Sí | ❌ No |
| Tipus d’excepció | `AssertionError` | Qualsevol (`ValueError`, `TypeError`...) |
| Missatge d’error | Opcional, curt | Personalitzat i complet |
| Exemple | `assert x > 0, "x ha de ser positiu"` | `if x <= 0: raise ValueError("x ha de ser positiu")` |

---

## **Ús de les assercions per verificar condicions durant el desenvolupament**

Les assercions són útils per garantir que les condicions siguen certes durant l'execució del codi.  
Es poden utilitzar per a diverses comprovacions:

- **Verificar valors interns** del programa.  
- **Comprovar variables** en certs punts del codi.  
- **Garantir condicions prèvies** abans d'executar codi addicional.

---

## **Exemple de verificació amb assert**

```python
age = int(input("Introdueix la teva edat: "))
assert age > 0, "L'edat ha de ser un número positiu"
print("Edat vàlida:", age)
```

Si l’usuari introdueix `-5`, es mostrarà:

```
AssertionError: L'edat ha de ser un número positiu
```

---

## **Exemples pràctics**

1. **Verificar l'entrada d'usuari**

   ```python
   num = int(input("Introdueix un nombre positiu: "))
   assert num > 0, "El número ha de ser positiu."
   print("El número introduït és:", num)
   ```

2. **Garantir que una llista no està buida**

   ```python
   llista = [1, 2, 3]
   assert len(llista) > 0, "La llista no pot estar buida"
   print("La llista té elements:", llista)
   ```

3. **Capturar l'error d'assert**

   ```python
   try:
       valor = int(input("Introdueix un valor entre 1 i 10: "))
       assert 1 <= valor <= 10, "El valor ha d'estar entre 1 i 10."
       print("Valor correcte!")
   except AssertionError as e:
       print(" Error:", e)
   ```

---

##  Activitats d'exemple

1. **Verificació d'edat amb assert**  
   - Crea un programa que demane una edat i utilitze una asserció per assegurar que siga positiva.

2. **Comprovació de llista buida**  
   - Escriu un programa que utilitze una asserció per garantir que una llista tinga almenys un element abans de processar-la.

3. **Accés segur amb assert**  
   - Fes un programa que demane una posició i mostre un element d’una llista predefinida.  
     Utilitza `assert` per comprovar que la posició siga vàlida (similar a l’**Activitat 10**).

---

## 🧾 Criteris d'Avaluació Coberts

- **i)** S’han utilitzat assercions per a la detecció i la correcció d’errors durant la fase de desenvolupament.