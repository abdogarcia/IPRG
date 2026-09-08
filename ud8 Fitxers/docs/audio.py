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
