import pygame
import json

ANCHO=800
ALTO=660

def Separar(l, ancho):
    con=0
    matriz=[]
    linea=[]
    for i in l:
        linea.append(i)
        con+=1
        if con==ancho:
            matriz.append(linea)
            linea=[]
            con=0
    return matriz

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

    lm=[]
    for l in base['layers']:
        print l['name']
        if l['name']=='muros':
            lm=l['data']

    #print lm
    an_fondo=base["width"]
    mapa=Separar(lm, an_fondo)
    for f in mapa:
        print f
    #print m

    nom_arc=''
    for l in base['tilesets']:
        nom_arc=l['image']
        al_c=l['tileheight']
        an_c=l['tilewidth']

    print nom_arc, al_c, an_c
    lin=Recortar(nom_arc, an_c, al_c)

    fondo=pygame.image.load('mapa.png').convert()
    pantalla.blit(fondo,[0,0])
    xy=0
    for f in mapa:
        xp=0
        for c in f:
            if c!=0:
                cuadro=lin[c-1]
                print c, [xp,xy], an_c
                pantalla.blit(cuadro,[xp,xy])
            xp+=an_c
        xy+=al_c

    pygame.display.flip()
    fin=False
    reloj=pygame.time.Clock()
    var_x=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        var_x+=-2
        pantalla.fill((0,0,0))
        pantalla.blit(fondo,[var_x,0])
        
        pygame.display.flip()
        reloj.tick(60)
