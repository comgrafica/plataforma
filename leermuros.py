import pygame
import json

ANCHO=600
ALTO=220

def Cargar_fondo(archivo, ancho_c, alto_c):
    imagen=pygame.image.load(archivo).convert_alpha()
    img_ancho,img_alto =imagen.get_size()
    linea_fondo=[]
    for f_y in range(0, img_alto/alto_c):
        for f_x in range(0, img_ancho/ancho_c):
            cuadro=(f_x*ancho_c, f_y*alto_c, ancho_c, alto_c)
            linea_fondo.append(imagen.subsurface(cuadro))

    return linea_fondo

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    with open('mapa.json') as js_ar:
        base=json.load(js_ar)

    al=base['height']
    an=base['width']
    print 'dimensiones: ', al, 'x',an

    #print base['tilesets']
    for v in base['tilesets']:
        archivo=v['image']
        c_al=v['tileheight']
        c_an=v['tilewidth']


    lt=Cargar_fondo(archivo,c_an, c_al)

    '''
    var_x=0
    for ef in lt:
        pantalla.blit(ef,[var_x,0])
        var_x+=c_an
    pygame.display.flip()
    #print archivo, ' ', c_al, ' ', c_an
    '''

    colision=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
[2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 6, 7, 7, 7, 7, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7]]

    var_y=0
    for f in colision:
        var_x=0
        for c in f:
            indice=c-1
            if indice>=0:
                cuadro=lt[indice]
                if var_x<=ANCHO:
                    pantalla.blit(cuadro, [var_x, var_y])
                print var_x, var_y, indice
            var_x+=c_al
        var_y+=c_an


    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
