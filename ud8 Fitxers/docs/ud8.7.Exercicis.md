<h1 style="display:none;"># Inici</h1>

<style>
    .md-typeset h2{
        font-weight: bold!important;
    }
</style>

# 1. Gestió de Fitxers - Crear, Llegir i Afegir Dades

## Descripció:
Crea un programa que faci el següent:

1. Demana a l'usuari que introdueixi el seu nom i edat.
2. Guarda aquestes dades en un fitxer de text anomenat `dades_usuari.txt`.
3. Llegeix el contingut del fitxer i mostra-ho per pantalla.
4. Després, afegeix una nova línia amb una altra dada introduïda pel mateix usuari (per exemple, una nova afegida de ciutat).

## Requisits:

- Utilitza **excepcions** per gestionar possibles errors com "fitxer no trobat" o "accés denegat".

# 2. Concatenació de Fitxers de Text

## Descripció:
Crea un programa que llegeixi el contingut de diversos fitxers de text i els concatenï en un nou fitxer. El programa també ha de controlar que els fitxers d'origen existeixin abans de copiar-los.

## Requisits:

- Llegeix fitxers de text amb `read()`.
- Crea un nou fitxer de text i escriu-hi el contingut concatenat.
- Utilitza excepcions per verificar l'existència dels fitxers d'origen i gestionar possibles errors.

# 3. Obrir i tancar fitxers

**Objectiu:** Practicar l’obertura, escriptura, afegit i tancament de fitxers en Python.

## Part 1: Creació i escriptura

1. Crea un fitxer anomenat `prueba.txt` utilitzant el mode `'w'` i escriu-hi la frase `"Primera línia"`.
2. Torna a obrir el fitxer amb mode `'w'` i escriu-hi `"Segona línia"`.
3. Observa què passa amb el contingut anterior. Explica-ho amb les teves paraules.

## Part 2: Creació exclusiva

1. Intenta obrir el fitxer `prueba.txt` amb mode `'x'` i escriu-hi `"Tercera línia"`.
2. Observa què passa. Quina excepció et llença Python?
3. Borra el fitxer i torna a fer el mateix pas. Què passa ara?

## Part 3: Afegir al final

1. Obre el fitxer `prueba.txt` amb mode `'a'` i afegeix la línia `"Quarta línia"`.
2. Torna a obrir el fitxer amb mode `'a'` i afegeix dues línies més: `"Cinquena línia"` i `"Sisena línia"`.
3. Obre el fitxer en mode lectura (`'r'`) i mostra tot el contingut per pantalla.

## Part 4: Llegir i tancar fitxers

1. Obre el fitxer amb mode `'r'` i llegeix tot el contingut amb `.read()`.
2. Tanca el fitxer utilitzant `.close()`.
3. Prova d’obrir un fitxer que no existeix amb mode `'r'`. Quin error obtens?


# 4. Organització de Fitxers - Moure Fitxers entre Directoris

## Descripció:
Crea un programa que mogui un fitxer d'un directori a un altre. El programa també ha de llistar els fitxers en el directori de destinació després de moure el fitxer.

## Requisits:

- Utilitza els mòduls `os` o `pathlib` per moure fitxers.
- Gestiona **excepcions** si el fitxer no es pot moure o si el directori no existeix.


# 5. Còpia de Directoris Complets

## Descripció:
Crea un programa que copiï tot el contingut d'un directori (fitxers i subdirectoris) a un altre directori. El programa ha de mantenir la mateixa estructura de directoris.

## Requisits:

- Utilitza `shutil.copytree()` o una combinació de mètodes `os` i `shutil` per copiar els fitxers i subdirectoris.
- Gestiona excepcions per garantir que el directori d'origen existeixi i que el directori de destinació sigui vàlid.

# 6. Lectura i Escritura de Fitxers JSON

## Descripció:
Crea un programa que llegeixi un fitxer JSON que conté un diccionari amb les dades d'un estudiant (nom, edat, nota), el modifiqui per afegir una nova dada (com una nova assignatura), i el guardi en el mateix fitxer.

Pots descarregar el CSV [fent click ací](material/dades_exercici.json)

## Exemple de diccionari d'estudiant
```json
estudiant = {
    "nom": "Joan",
    "edat": 20,
    "nota": 8.5,
    "assignatures": ["Matemàtiques", "Física"]
}
```

## Requisits:
- Utilitza el mòdul `json` per gestionar els fitxers JSON.
- Gestiona **excepcions** per assegurar-te que el fitxer existeix i que el contingut és vàlid.


# 7. Lectura i Escriptura de Fitxers CSV

## Descripció:
Crea un programa que llegeixi un fitxer CSV, n'extregui les dades i les modifiqui (per exemple, afegint una nova fila o modificant una existent). Després, guarda les dades modificades en un nou fitxer CSV.

Pots descarregar el CSV [fent click ací](material/dades_exercici.csv)

## Requisits:

- Utilitza el mòdul `csv` per llegir i escriure fitxers CSV.
- Llegeix les dades d'un fitxer CSV i mostra-les per pantalla.
- Modifica les dades (per exemple, afegint una nova fila amb dades de l'usuari).
- Guarda les dades modificades en un nou fitxer CSV.
- Gestiona excepcions per assegurar-se que el fitxer CSV existeix i és vàlid.

---

# 8. Gestió d'un Sistema de Registre d'Estudiants

## Descripció:
Imagina que treballes en una aplicació per gestionar informació sobre estudiants d'una escola. Cada estudiant té un nom, una edat, una nota i una llista d'assignatures. La informació dels estudiants es guarda en un fitxer **JSON** i **CSV**. L'objectiu és llegir i escriure fitxers amb la informació dels estudiants, moure fitxers entre directoris per organitzar-los millor, i afegir nous estudiants mitjançant l'entrada d'usuari.

### Escenari:

1. El sistema llegeix un fitxer JSON anomenat `estudiants.json` que conté les dades dels estudiants.
2. Després, el sistema ha de:
   - Afegir un nou estudiant amb nom, edat, nota i assignatures.
   - Desar la informació actualitzada en el fitxer `estudiants.json`.
   - Crear un fitxer **CSV** anomenat `estudiants.csv` amb la mateixa informació dels estudiants (nom, edat, nota, assignatures).
   - Si el fitxer CSV ja existeix, el programa haurà de moure'l a un directori de "fitxers antics".
   - Finalment, el sistema ha de gestionar errors en tots els passos per assegurar-se que els fitxers existeixin i que els formats siguin vàlids.

### Requisits:

1. **Lectura i escriptura de fitxers JSON i CSV**.
2. **Gestió d'errors** en la lectura/escriptura de fitxers.
3. **Mou fitxers** entre directoris si el fitxer CSV ja existeix.
4. **Afegir nous estudiants** a les dades existents.

