<h1 style="display:none;"># Inici</h1>

# 6. La manera de pensar d’un programador

Aprendre a programar no és sols dominar un llenguatge de programació, sinó **aprendre a pensar d’una forma estructurada i lògica** per a trobar solucions eficients a problemes complexos.

## Característiques d’aquesta forma de pensar

Sobretot en problemes extensos caldria aplicar:

- **Descomposició**: dividir un problema gran en parts més xicotetes i manejables.  
- **Abstracció**: ignorar els detalls innecessaris i centrar-se en allò essencial.  
- **Pensament lògic**: utilitzar raonaments clars i precisos per prendre decisions.  
- **Creativitat**: trobar diferents camins per arribar a una solució.  
- **Precisió**: expressar instruccions d’una manera que l’ordinador puga entendre sense ambigüitats.

## Exemple 
Imaginem que volem fer un programa que indique quin és el nombre més gran d'una llista.
Abans d'escriure codi, hem de pensar com ho faria qualsevol persona encara que no sabera programar, a partir d'una llista de números d'exemple:

![Algorisme major llista](img/algMajorLlista.png)

Una vegada hem pensat la solució, el següent pas és **transformar eixa idea en un algoritme**. 

En la solució que hem plantejat podem identificar:

- Un pas inicial: obtindre la llista i guardar el primer com a major.
- Uns passos que es repeteixen per a cada element de la llista:
    - Comparar-lo amb el major actual.
    - Si és més gran, actualitzar el major.
- Un pas final: mostrar eixe major.
  
Per tant, podem expressar aquestos passos en pseudocodi. Més avant vorem en detall instruccions d'assignació, bifurcació, repetició...

```text
INICI
    llista ← [7, 12, 3, 20, 5]

    major ← llista[0]

    Per cada nombre de llista fer
        Si nombre > major llavors
            major ← nombre
        FiSi
    FiPer

    Escriu "El nombre major és: ", major
FI
```

Això és el que fa un programador: **analitzar un problema i organitzar una seqüència de passos per a arribar a una solució**.

Una vegada tenim l'algoritme, passar-lo a un programa consisteix principalment a expressar eixos mateixos passos amb la sintaxi del llenguatge de programació que utilitzem.

---

!!! question "Rreflexió final"
    Donat un determinat problema, què creus que és més difícil: dissenyar l’algoritme o traduir-lo a un programa?  

**Recorda**: La millor forma d'aprendre a programar és programant.
