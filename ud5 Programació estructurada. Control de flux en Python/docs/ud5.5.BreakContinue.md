<h1 style="display:none;"># Inici</h1>

# 5. Alteració del flux en els bucles

El funcionament d’un bucle és executar totes les instruccions del seu interior i repetir-les fins que finalitza. No obstant això, en determinades situacions podem **alterar aquest flux normal d’execució** amb les ordres `break` i `continue`.

- `break` **abandona el bucle**.
- `continue` **abandona la iteració actual i passa a la següent**. Les instruccions que queden per davall dins del bucle no s'executen en eixa iteració.

![Cadena trencada](img/image24.jpg){ width="160" }

```python
# Inici del bucle
for i in range(1, 10):
    ...

    if ...:
        continue

    ...

    if ...:
        break

    ...
# Fi del bucle
```

## Exemple de `break`

Suposem que volem preguntar l’edat de tot l’alumnat només per comprovar si **hi ha algun menor d’edat**. En el moment en què trobem un menor, **no cal continuar preguntant les edats dels altres**. En eixe moment podem eixir directament del bucle utilitzant `break`.

```python
menors = False

for alu in range(24):
    edat = int(input("Edat:"))

    if edat < 18:
        menors = True
        break

if menors:
    print("Hi ha menors")
else:
    print("Tots majors")
```

## Exemple de `continue`

Suposem que, dins d’un bucle, volem demanar les notes de tot l’alumnat i fer diverses operacions amb cadascuna. Però, si s’introdueix una nota que **no és significativa**, volem descartar-la i passar directament a la següent iteració.

```python
for alu in range(24):
    nota = float(input("Introdueix la nota (-1 si no s'ha presentat): "))

    if nota == -1:
        print("Alumne no presentat")
        continue

    print("Nota:", nota)

    if nota >= 5:
        print("Aprovat")
    else:
        print("Suspés")

    print("Nota sobre 100:", nota * 10)
    print("----------------")
```

El `continue` permet **descartar casos especials al principi de la iteració** i evita haver de niuar tot el codi restant dins d’un `else`.

!!! note
    Si estes instruccions apareixen dins de **bucles niuats**, només afecten el bucle en què es troben directament. Per exemple, si un `break` està dins d’un bucle interior, eixirà d’eixe bucle, però el bucle exterior continuarà executant-se.

## Exercici resolt de bucles amb `break` i `continue`

!!! example
    Programa en Python que demane les notes dels alumnes (números enters i positius entre 0 i 10) i que després mostre quantes notes s'han introduït i la nota mitjana. Per a parar d'introduir notes caldrà posar la nota 11, que no es tindrà en compte per als càlculs.

    **Nota:** el programa es podria fer sense `break` ni `continue`, però ho farem així per a vore el seu funcionament.

```python
# Inicialització de comptador i acumulador
notes = 0
suma = 0

# Demanar dades i fer càlculs
while True:
    # Introducció de la nota per teclat
    nota = input("Dis-me una nota (11 per a eixir):")

    # Comprovacions de nota OK
    if not nota.isnumeric():
        print("Han de ser números enters positius. Torna a provar.")
        continue

    nota = int(nota)

    if nota > 11:
        print("La nota màxima és 10. Torna a provar.")
        continue

    # Si volem acabar
    if nota == 11:
        print("Ja no et demane més notes. Vaig a eixir del bucle.")
        break

    # Si tot ha anat bé, farem els càlculs
    print("Nota introduïda ok:", nota)
    notes += 1
    suma += nota

# Fi del bucle

# Mostrem els resultats
print(notes, "notes introduïdes.")
print("Nota mitja:", suma / notes)
```

!!! note
    - Amb `while True` aconseguim fer un bucle **infinit**. Només podrem eixir si fem un `break`.
    - `isnumeric()` és `True` si tots els caràcters són numèrics.
    - Si el programa executa un `continue`, torna a l'inici del bucle.
    - Si executa un `break`, ix completament del bucle.

## Exercicis: alteració de flux en els bucles

28. Fes un programa que demane una contrasenya fins que siga correcta (`"1234"`) però només hi ha 5 intents. Finalment ha de dir si la contrasenya és correcta o si ha esgotat els intents, i en quants intents s’ha fet.

    **Nota:** es pot fer de múltiples formes però, com volem practicar el `break`, fes-ho amb un bucle de 5 intents i, si s’encerta la contrasenya, força l’eixida.
