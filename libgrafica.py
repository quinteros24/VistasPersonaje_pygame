import math

ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
AZUL_FONDO = [115,215,245]
BLANCO = [255,255,255]
GRIS = [245,245,245]
GRIS_CLARO = [225,200,200]
GRIS_CLARO_CLARO = [197,197,197]
NEGRO = [0,0,0]
AMARILLO = [255,255,0]
PURPURA = [128,0,128]
NARANJA = [255,165,0]
NARANJA_CLARO = [255,170,156]
NARANJA_CLARO_CLARO = [255,230,190]
ROSA = [255,40,210]
ROSA_CLARO = [255,108,160]
ROSA_CLARO_CLARO = [255,205,250]


def Pantalla_Cartesiano(p,centro): 
    yp = -p[1] + centro[1] 
    xp =  p[0] + centro[0]
    return [xp,yp]

def Escala(p,S):
    xp=p[0]*S[0]
    yp=p[1]*S[1]
    return [xp,yp]

def Traslacion(p,t):
    xp=p[0]+t[0]
    yp=p[1]+t[1]
    return [xp,yp]

def Rotacion_a(p,r):
    r = math.radians(r)
    xp = (p[0]*math.cos(r))-(p[1]*math.sin(r))
    yp = (p[0]*math.sin(r))+(p[1]*math.cos(r))
    return[int(xp),int(yp)]

def Rotacion_h(p,r):
    r = math.radians(r)
    xp = (p[0]*math.cos(r))-(p[1]*math.sin(r))
    yp = (p[0]*math.sin(r))+(p[1]*math.cos(r))
    return[int(xp),int(yp)]