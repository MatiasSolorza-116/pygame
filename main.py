import pygame
import botones_menu as bm
import otro as o

pygame.init()
pygame.mixer.init()
pygame.font.init()

pantalla = pygame.display.set_mode((bm.ANCHO, bm.ALTO))
pygame.display.set_caption("AREA-Codycross-51 (Santiago Albertavicius, Matias Solorza)")

# fuente
fuente = pygame.font.SysFont("arial", 24)

#boton volver
boton_volver_rect = pygame.Rect(bm.ANCHO - 400, bm.ALTO - 50, 600, 40)


# musica y sonido
pygame.mixer.music.load("marcianos.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.10)

# multipantallas y dibujo lo que quiero q se vea (TEXTO, FONDOS, BOTON VOLVER)

def mostrar_pantalla_juego(texto):
    pantalla.fill(o.BLANCO)
    texto_render = fuente.render(texto, True, o.NEGRO)
    pantalla.blit(texto_play, (bm.rec_play_x / 2, bm.rec_play_y  / 2 ))
    #  "Volver"
    pygame.draw.rect(pantalla, o.BLANCO, boton_volver_rect)
    texto_volver = fuente.render("VOLVER", True, o.NEGRO)
    pantalla.blit(texto_volver, (boton_volver_rect.x + 10, boton_volver_rect.y + 10))

def mostrar_pantalla_creditos(texto):
    pantalla.blit(fondo_credito, (0, 0))
    texto_render = fuente.render(texto, True, o.NEGRO)
    pantalla.blit(texto_render, (50, 50))  
    #  "Volver"
    pygame.draw.rect(pantalla, o.BLANCO, boton_volver_rect)
    texto_volver = fuente.render("VOLVER", True, o.NEGRO)
    pantalla.blit(texto_volver, (boton_volver_rect.x + 10, boton_volver_rect.y + 10))

def mostrar_pantalla_estadisticas(texto):
    pantalla.fill(o.BLANCO)
    texto_render = fuente.render(texto, True, o.NEGRO)
    pantalla.blit(texto_render, (bm.rec_estad_x + 25, bm.rec_estad_y + 155))
    #  "Volver"
    pygame.draw.rect(pantalla, o.BLANCO, boton_volver_rect)
    texto_volver = fuente.render("VOLVER", True, o.NEGRO)
    pantalla.blit(texto_volver, (boton_volver_rect.x + 10, boton_volver_rect.y + 10))



# fondos
fondo_credito = pygame.image.load("credit.png")
fondo_credito = pygame.transform.scale(fondo_credito, (bm.ANCHO, bm.ALTO))

#fondo animado menu

CANT_FONDOS = 69  # <- cantidad fija de imágenes
fondos = []
for i in range(CANT_FONDOS):
    imagen = pygame.image.load(f"lla {i}.jpg")
    imagen = pygame.transform.scale(imagen, (bm.ANCHO, bm.ALTO))
    fondos.append(imagen)

fondo_index = 0
contador = 0
reloj = pygame.time.Clock()
estado = "menu" 


#-------------------------------------------------------------------------
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            SystemExit()
    #  tocar con el mause  
    if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == "menu":
                if pygame.Rect(bm.boton_jugar).collidepoint(evento.pos):
                    estado = "JUGAR"
                elif pygame.Rect(bm.boton_creditos).collidepoint(evento.pos):
                    estado = "CREDITOS"
                elif pygame.Rect(bm.boton_estadisticas).collidepoint(evento.pos):
                    estado = "ESTADISTICA"
                elif pygame.Rect(bm.boton_salir).collidepoint(evento.pos):
                    pygame.quit()
                    exit()
            
            # boton volver funcionalidad mause
            elif estado == "CREDITOS":
                if boton_volver_rect.collidepoint(evento.pos):
                    estado = "menu"
            elif estado == "JUGAR":
                if boton_volver_rect.collidepoint(evento.pos):
                    estado = "menu"
            elif estado == "ESTADISTICA":
                if boton_volver_rect.collidepoint(evento.pos):
                    estado = "menu"
    
    # mostrar todo (la pantalla de menu esta antes q los botones para q no tape)

    if estado == "menu": 
    # Mostrar fondo animado
        pantalla.blit(fondos[fondo_index], (0, 0))
        contador += 1
        if contador >= 69:
            contador = 0
        fondo_index += 1
        if fondo_index >= CANT_FONDOS:
            fondo_index = 0

        # play (funcion de rectangulo, y texto)
        pygame.draw.rect(pantalla, o.BLANCO,(bm.rec_play_x + 10, bm.rec_play_y + 50, bm.rec_play_ancho, bm.rec_play_alto))
        texto_play = fuente.render("JUGAR", True, o.NEGRO)
        pantalla.blit(texto_play, (bm.rec_play_x + 65, bm.rec_play_y + 55 )) 

        # creditos (funcion de rectangulo, y texto)
        pygame.draw.rect(pantalla, o.BLANCO, (bm.rec_creditos_x - 90, bm.rec_creditos_y + 200  , bm.rec_creditos_ancho, bm.rec_creditos_alto))
        texto_creditos = fuente.render("CRÉDITOS", True, o.NEGRO)
        pantalla.blit(texto_creditos, (bm.rec_creditos_x - 55, bm.rec_creditos_y + 205))

        # estadisticas (funcion de rectangulo, y texto)
        pygame.draw.rect(pantalla, o.BLANCO,(bm.rec_estad_x + 10, bm.rec_estad_y + 150, bm.rec_estad_ancho, bm.rec_estad_alto))
        texto_estadistica = fuente.render("ESTADÍSTICAS", True, o.NEGRO)
        pantalla.blit(texto_estadistica, (bm.rec_estad_x + 25, bm.rec_estad_y + 155))

        # salir (funcion de rectangulo, y texto)
        pygame.draw.rect(pantalla, o.AZUL,(bm.rec_salir_x + 10, bm.rec_salir_y + 200, bm.rec_salir_ancho, bm.rec_salir_alto))
        texto_salir = fuente.render("SALIR", True, o.BLANCO)
        pantalla.blit(texto_salir, (bm.rec_salir_x + 75, bm.rec_salir_y + 205))


    elif estado == "JUGAR": #hace que funcione el boton y me dirija a la pantalla
       mostrar_pantalla_juego("ACA VA EL JUEGO") #osea esta pantalla
    elif estado == "CREDITOS":
        mostrar_pantalla_creditos("") #tiene q x lo menos tener comillas
    elif estado == "ESTADISTICA":
        mostrar_pantalla_estadisticas ("nashe")
        
    pygame.display.update()
    reloj.tick(30)
          


