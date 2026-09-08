<h1 style="display:none;"># Inici</h1>
<style>
    .md-typeset h2{
        font-weight: bold!important;
    }
</style>


# Exercici 10: Creació, escriptura i lectura de JSON amb operacions agregades

1. Crea una **llista de diccionaris** anomenada `persones` amb **exactament tres elements**, amb les dades següents:

   - Persona 1: Nom = "Anna", Edat = 28, Ciutat = "València"
   - Persona 2: Nom = "Marc", Edat = 35, Ciutat = "Alacant"
   - Persona 3: Nom = "Laura", Edat = 42, Ciutat = "Castelló"

2. Utilitza la funció `map()` per obtenir una **llista amb només les edats** de totes les persones.

3. Utilitza la funció `reduce()` per calcular la **suma total de les edats**.

4. Crea un diccionari anomenat `dades` amb les claus:
   - `"persones"` → contindrà la llista original de diccionaris
   - `"edat_total"` → contindrà la suma total de les edats

5. Escriu el diccionari `dades` en un fitxer anomenat `persones.json`.

6. Llegeix el fitxer `persones.json` i imprimeix:
   - La llista de persones
   - El valor de l’edat total

---

# Exercici 11: Manipulació d’XML amb llistes i map()

1. Crea una **llista de diccionaris** anomenada `registres` amb les dades següents:

   - Nom = "Pere", Edat = 30
   - Nom = "Clara", Edat = 25
   - Nom = "Jordi", Edat = 40

2. A partir de la llista `registres`, crea un **document XML** amb l’estructura següent:

   ```xml
   <persones>
       <persona>
           <nom>...</nom>
           <edat>...</edat>
       </persona>
   </persones>
   ```

3. Escriu el document XML en un fitxer anomenat `persones.xml`.

4. Llegeix el fitxer `persones.xml` i imprimeix per pantalla:
   - El nom i l’edat de cada persona

5. Utilitza la funció `map()` per incrementar **en 1 any l’edat de totes les persones**.

6. Actualitza el document XML amb les noves edats i guarda el resultat en un nou fitxer anomenat `persones_actualitzat.xml`.

---

# Exercici 12: Manipulació de CSV amb filter() i zip()

1. Crea dues llistes:
   - `noms = ["Sergi", "Marta", "Joan", "Elena"]`
   - `edats = [22, 34, 29, 41]`

2. Utilitza la funció `zip()` per combinar les dues llistes i generar una **llista de tuples** `(nom, edat)`.

3. Escriu aquestes dades en un fitxer anomenat `persones.csv` amb el format següent:

   ```text
   nom,edat
   Sergi,22
   Marta,34
   Joan,29
   Elena,41
   ```

4. Llegeix el fitxer `persones.csv` i guarda les dades (excepte la capçalera) en una llista de tuples.

5. Utilitza la funció `filter()` per obtenir només les persones amb **edat superior a 30**.

6. Escriu les files filtrades en un nou fitxer anomenat `persones_mes_30.csv`, mantenint la mateixa capçalera.

---

## Observacions

- Es recomana utilitzar els mòduls `json`, `xml.etree.ElementTree`, `csv` i `functools`.
