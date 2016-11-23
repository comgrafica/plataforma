import pygame
import json

ANCHO=300
ALTO=200

def Separar(l, ancho):
    con=0
    matriz=[]
    linea=[]
    for i in l:
        linea.append(i)
        con+=1
        if con == ancho:
            matriz.append(linea)
            linea=[]
            con=0
    return matriz



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    with open('mapa.json') as js_ar:
        base=json.load(js_ar)

    al=base['height']
    an=base['width']
    print 'dimensiones: ', al, 'x',an

    lsm=[]
    for v in base['layers']:
        if v['name']=='muros':
            lsm=v['data']

    #print lsm
    m=Separar(lsm,an)
    for f in m:
        print f

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
