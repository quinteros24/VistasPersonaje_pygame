import pygame
from libgrafica import *

CENTRO_LATERAL = [100,300]
CENTRO_FRONTAL = [300,300]
CENTRO_SUPERIOR = [300,100]

ANCHO_VENTANA=1400
ALTO_VENTANA=800

pxl = 20 #PIXELES PARA MODIFICAR EL TAMAÑO

def vistas_isometricas():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA]) 
    pantalla.fill(AZUL_FONDO)
    #----------------------------------------------------- VISTA LATERAL ------------------------------------------------
    #Cuerpo
    cuerpo_1 = CENTRO_LATERAL
    cuerpo_2 = [cuerpo_1[0]+(5*pxl), cuerpo_1[1]]
    cuerpo_3 = [cuerpo_2[0], cuerpo_2[1]+(9*pxl)]
    cuerpo_4 = [cuerpo_1[0], cuerpo_3[1]]
    cuerpo = [cuerpo_1,cuerpo_2,cuerpo_3,cuerpo_4]
    pygame.draw.polygon(pantalla, BLANCO, cuerpo)

    #Cresta (A partir de Cuerpo)
    cresta_1 = [cuerpo_1[0]+(2*pxl), cuerpo_1[1]]
    cresta_2 = [cresta_1[0]+(1*pxl), cresta_1[1]]
    cresta_3 = [cresta_2[0], cresta_2[1]-(1*pxl)]
    cresta_4 = [cresta_1[0], cresta_3[1]]
    cresta = [cresta_1,cresta_2,cresta_3,cresta_4]
    pygame.draw.polygon(pantalla, ROSA_CLARO, cresta)

    #Ojo1 (A partir de Cresta)
    ojo = []
    ojo.extend(cresta)
    t = [-(1*pxl),2*pxl]
    for i in range(len(ojo)):
        ojo[i] = Traslacion(ojo[i],t)
    pygame.draw.polygon(pantalla, NEGRO, ojo)

    #Ojo2 (A partir del Ojo1)
    t = [2*pxl,0]
    for i in range(len(ojo)):
        ojo[i] = Traslacion(ojo[i],t)
    pygame.draw.polygon(pantalla, NEGRO, ojo)

    #Pico (A partir de Cresta)
    pico_1 = [cresta_1[0], cresta_1[1]+(2*pxl)]
    pico_2 = [pico_1[0]+(1*pxl), pico_1[1]]
    pico_3 = [pico_2[0], pico_2[1]+(2*pxl)]
    pico_4 = [pico_1[0], pico_3[1]]
    pico = [pico_1,pico_2,pico_3,pico_4]
    pygame.draw.polygon(pantalla, NARANJA, pico)

    #Barbilla (A partir de Pico)
    barbilla = []
    barbilla.extend(pico)
    t = [0, 2*pxl]
    for i in range(len(barbilla)):
        barbilla[i] = Traslacion(barbilla[i],t)
    pygame.draw.polygon(pantalla, ROSA_CLARO, barbilla)

    #Ala 1
    ala = []
    ala.extend(barbilla)
    t = [-3*pxl, 2*pxl]
    for i in range(len(ala)):
        ala[i] = Traslacion(ala[i],t)
    pygame.draw.polygon(pantalla, GRIS_CLARO, ala)
    
    #Ala 2 (A partir de Ala 1)
    t = [6*pxl,0]
    for i in range(len(ala)):
        ala[i] = Traslacion(ala[i],t)
    pygame.draw.polygon(pantalla, GRIS_CLARO, ala)

    #Pata 1
    pata_1 = [cuerpo_4[0]+(1*pxl), cuerpo_4[1]]
    pata_2 = [pata_1[0]+(1*pxl), pata_1[1]]
    pata_3 = [pata_2[0], pata_2[1]+(2*pxl)]
    pata_4 = [pata_3[0]+(0.33*pxl), pata_3[1]]
    pata_5 = [pata_4[0], pata_4[1]+(1*pxl)]
    pata_6 = [pata_5[0]-(1.66*pxl), pata_5[1]]
    pata_7 = [pata_6[0], pata_6[1]-(1*pxl)]
    pata_8 = [pata_7[0]+(0.33*pxl), pata_7[1]]
    pata = [pata_1, pata_2, pata_3, pata_4, pata_5, pata_6, pata_7, pata_8]
    pygame.draw.polygon(pantalla, NARANJA, pata)

    #Pata 2
    t = [2*pxl,0]
    for i in range(len(pata)):
        pata[i] = Traslacion(pata[i],t)
    pygame.draw.polygon(pantalla, NARANJA, pata)

    
    #----------------------------------------------------- VISTA FRONTAL ------------------------------------------------
    #Cuerpo
    cuerpo_1 = CENTRO_FRONTAL
    cuerpo_2 = [cuerpo_1[0]+(5*pxl), cuerpo_1[1]]
    cuerpo_3 = [cuerpo_2[0], cuerpo_2[1]+(5*pxl)]
    cuerpo_4 = [cuerpo_3[0]+(3*pxl), cuerpo_3[1]]
    cuerpo_5 = [cuerpo_4[0], cuerpo_4[1]+(4*pxl)]
    cuerpo_6 = [cuerpo_1[0], cuerpo_5[1]]
    cuerpo = [cuerpo_1,cuerpo_2,cuerpo_3,cuerpo_4, cuerpo_5, cuerpo_6]
    pygame.draw.polygon(pantalla, BLANCO, cuerpo)

    #Cresta
    cresta_1 = [cuerpo_1[0]+(1*pxl), cuerpo_1[1]]
    cresta_2 = [cresta_1[0]+(3*pxl), cresta_1[1]]
    cresta_3 = [cresta_2[0], cresta_2[1]-(1*pxl)]
    cresta_4 = [cresta_1[0], cresta_3[1]]
    cresta = [cresta_1,cresta_2,cresta_3,cresta_4]
    pygame.draw.polygon(pantalla, ROSA_CLARO, cresta)

    #Pico
    pico_1 = [cuerpo_1[0], cuerpo_1[1]+(2*pxl)]
    pico_2 = [pico_1[0]-(2*pxl), pico_1[1]]
    pico_3 = [pico_2[0], pico_2[1]+(2*pxl)]
    pico_4 = [pico_1[0], pico_3[1]]
    pico = [pico_1,pico_2,pico_3,pico_4]
    pygame.draw.polygon(pantalla, NARANJA, pico)

    #Barbilla (A partir de Pico)
    barbilla_1 = [pico_4[0],pico_4[1]]
    barbilla_2 = [barbilla_1[0]-(1*pxl), barbilla_1[1]]
    barbilla_3 = [barbilla_2[0], barbilla_2[1]+(2*pxl)]
    barbilla_4 = [barbilla_1[0], barbilla_3[1]]
    barbilla = [barbilla_1,barbilla_2,barbilla_3,barbilla_4]
    pygame.draw.polygon(pantalla, ROSA_CLARO, barbilla)

    #Ala (A partir de barbilla)
    ala_1 = [barbilla_4[0]+(1*pxl), barbilla_4[1]]
    ala_2 = [ala_1[0]+(5*pxl), ala_1[1]]
    ala_3 = [ala_2[0], ala_2[1]+(2*pxl)]
    ala_4 = [ala_1[0], ala_3[1]]
    ala = [ala_1, ala_2, ala_3, ala_4]
    pygame.draw.polygon(pantalla, GRIS_CLARO, ala)

    #Pata
    pata_1 = [cuerpo_6[0]+(3*pxl), cuerpo_6[1]]
    pata_2 = [pata_1[0]+(1*pxl), pata_1[1]]
    pata_3 = [pata_2[0], pata_2[1]+(2*pxl)]
    pata_4 = [pata_3[0]+(1*pxl), pata_3[1]]
    pata_5 = [pata_4[0], pata_4[1]+(1*pxl)]
    pata_6 = [pata_5[0]-(4*pxl), pata_5[1]]
    pata_7 = [pata_6[0], pata_6[1]-(1*pxl)]
    pata_8 = [pata_7[0]+(2*pxl), pata_7[1]]
    pata = [pata_1, pata_2, pata_3, pata_4, pata_5, pata_6, pata_7, pata_8]
    pygame.draw.polygon(pantalla, NARANJA, pata)
    
    #----------------------------------------------------- VISTA SUPERIOR ------------------------------------------------
    #Cuerpo
    cuerpo_1 = CENTRO_SUPERIOR
    cuerpo_2 = [cuerpo_1[0]+(8*pxl), cuerpo_1[1]]
    cuerpo_3 = [cuerpo_2[0], cuerpo_2[1]+(5*pxl)]
    cuerpo_4 = [cuerpo_1[0], cuerpo_3[1]]
    cuerpo = [cuerpo_1,cuerpo_2,cuerpo_3,cuerpo_4]
    pygame.draw.polygon(pantalla, BLANCO, cuerpo)

    #Cresta
    cresta_1 = [cuerpo_1[0]+(1*pxl), cuerpo_1[1]+(3*pxl)]
    cresta_2 = [cresta_1[0]+(3*pxl), cresta_1[1]]
    cresta_3 = [cresta_2[0], cresta_2[1]-(1*pxl)]
    cresta_4 = [cresta_1[0], cresta_3[1]]
    cresta = [cresta_1,cresta_2,cresta_3,cresta_4]
    pygame.draw.polygon(pantalla, ROSA_CLARO, cresta)

    #Pico
    pico_1 = [cuerpo_1[0], cuerpo_1[1]+(2*pxl)]
    pico_2 = [pico_1[0]-(2*pxl), pico_1[1]]
    pico_3 = [pico_2[0], pico_2[1]+(1*pxl)]
    pico_4 = [pico_1[0], pico_3[1]]
    pico = [pico_1,pico_2,pico_3,pico_4]
    pygame.draw.polygon(pantalla, NARANJA, pico)

    #Ala 1
    ala_1 = [cuerpo_1[0]+(1*pxl), cuerpo_1[1]]
    ala_2 = [ala_1[0]+(5*pxl), ala_1[1]]
    ala_3 = [ala_2[0], ala_2[1]-(1*pxl)]
    ala_4 = [ala_1[0], ala_3[1]]
    ala = [ala_1,ala_2,ala_3,ala_4]
    pygame.draw.polygon(pantalla, GRIS_CLARO, ala)
    
    #Ala 2 (A partir de Ala 1)
    t = [0,6*pxl]
    for i in range(len(ala)):
        ala[i] = Traslacion(ala[i],t)
    pygame.draw.polygon(pantalla, GRIS_CLARO, ala)

