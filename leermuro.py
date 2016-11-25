import pygame
import json

ANCHO=1128
ALTO=480

def Recortar(archivo, anc, alc):
    linea=[]
    imagen=pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto=imagen.get_size()
    print i_ancho, ' ', i_alto
    for y in range(0, i_alto/alc):
        for x in range(0,i_ancho/anc):
            cuadro=(x*anc, y*alc, anc, alc)
            linea.append(imagen.subsurface(cuadro))
    return linea

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    with open('mapae.json') as js_ar:
        base=json.load(js_ar)

    nom_arc=''
    for l in base['tilesets']:
        #print l['image']
        nom_arc=l['image']
        al_c=l['tileheight']
        an_c=l['tilewidth']

    print nom_arc, al_c, an_c
    lm=Recortar(nom_arc, an_c, al_c)
    '''
    xp=0
    for e in lm:
        cuadro=e
        pantalla.blit(e,[xp,0])
        xp+=an_c
    '''

    mapa=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 7, 7, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 6, 7, 7, 7, 7, 8, 0, 0, 7, 7, 7, 7, 7, 7]
    ]

    xy=0
    for f in mapa:
        xp=0
        for c in f:
            if c!=0:
                cuadro=lm[c-1]
                pantalla.blit(cuadro,[xp,xy])
            xp+=an_c
        xy+=al_c


    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
