import pygame
import os

pygame.init()

#------------------------------------------------
def inicialitza():
    global ALT
    global AMPLE
    global font
    global i_abdo
    ALT = 800
    AMPLE = 1000

    font = pygame.font.Font(None, 36)

    carregaImatges()


#------------------------------------------------
def carregaImatges():
    global i_abdo
    carpeta = os.path.dirname(__file__)
    ruta = os.path.join(carpeta, "imatges", "abdo.jpg")
    i_abdo = pygame.image.load(ruta)
    i_abdo = pygame.transform.scale(i_abdo, (40, 40))
#------------------------------------------------


def controlEvents():
    global executant
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executant = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                executant = False
#------------------------------------------------
def controlLimits(x, y):
    if x < radi:
        x = radi
    if x > AMPLE - radi:
        x = AMPLE - radi
    if y < radi:
        y = radi
    if y > ALT - radi:
        y = ALT - radi
    return x, y
#------------------------------------------------

def posaObjectes(x, y):
    global ultim
    global color
 
    finestra.fill("white")
    # Dibuixem la bola
    pygame.draw.circle(finestra, "red", (x, y), radi)
    # Dibuixem el nom de la bola
    text = font.render("Abdó", True, "black")
    finestra.blit(text, (x - 30, y - 30))

    # Dibuixem la imatge    
    finestra.blit(i_abdo, (x-20, y))

    # Dibuixem un text fix
    text = font.render("Temps", True, "black")
    finestra.blit(text, (20, 10))

    # Mostrem el temps transcorregut en segons
    temps = pygame.time.get_ticks()
    text = font.render(str(temps // 1000), True, "black")
    finestra.blit(text, (20, 30))

    # Mostrar un rectangle que canvia de color cada segon
    if temps // 1000 != ultim:
        ultim = temps // 1000
        color = (ultim * 20 % 256, ultim * 40 % 256, ultim * 60 % 256)
    pygame.draw.rect(finestra, color, (20, 60, 100, 30))    

    # Posa tots els objectes a la pantalla
    pygame.display.flip()


#------------------------------------------------
def controlTecles(x, y):
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_RIGHT]:
        x += 2
    if tecles[pygame.K_LEFT]:
        x -= 2
    if tecles[pygame.K_UP]:
        y -= 2
    if tecles[pygame.K_DOWN]:
        y += 2

    x, y = controlLimits(x, y)
    return x, y

#------------------------------------------------
# Programa principal
 
inicialitza()

finestra = pygame.display.set_mode((AMPLE, ALT))
pygame.display.set_caption("Atrapa la moneda")

rellotge = pygame.time.Clock()


executant = True
x = 100
y = 200
radi = 50
ultim = 0
color = (0, 0, 0)


while executant:
    controlEvents()

    x, y = controlTecles(x, y)

    posaObjectes(x, y)
   
    rellotge.tick(60)



pygame.quit()
