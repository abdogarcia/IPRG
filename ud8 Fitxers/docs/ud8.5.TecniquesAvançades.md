<h1 style="display:none;"># Inici</h1>

# 5. Tècniques avançades en la gestió de fitxers

## 5.1. Ús de buffers per a la millora del rendiment en la lectura/escriptura

El **buffering** és una tècnica que millora el rendiment quan llegim o escrivim fitxers. En lloc de llegir o escriure dades línia per línia o byte per byte, utilitzem un buffer per llegir o escriure múltiples bytes de manera més eficient. Els fitxers es poden obrir en mode **bufferitzat** per millorar el rendiment.

### Modes d'obertura amb buffering
Quan obrim un fitxer en mode de lectura o escriptura, podem especificar el buffering. Per defecte, Python utilitza un buffering automàtic. Tanmateix, podem controlar el buffering mitjançant el tercer argument de la funció `open()`.

- **0**: Sense buffering (només en mode binari).
- **1**: Buffering per línies.
- **Qualsevol nombre major que 1**: Buffering en blocs de mida especificada.

Exemple d'obertura amb buffering manual:
```python
# Obrir un fitxer en mode binari amb un buffer de mida específica
with open('document.txt', 'rb', buffering=4096) as fitxer:
    contingut = fitxer.read()
```

### Beneficis del buffering
El buffering millora significativament el rendiment quan treballem amb fitxers grans, ja que redueix la quantitat de lectors/escritors que han d'interaccionar amb el sistema de fitxers.


---