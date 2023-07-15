import pyautogui
import PIL as pil
from time import sleep
from os import system

img = pil.ImageGrab.grabclipboard() #imagem na área de transferencia
x,y = pyautogui.position() #localização do mouse

def desenhar():
    x_pixel = img.size[0]-2
    y_pixel = img.size[1]-2

    print('Tamanho da imagem: ', x_pixel, y_pixel)
    
    for xpixel in range(0, x_pixel, 4):
        for ypixel in range(0, y_pixel, 4):
            if (img.getpixel((xpixel, ypixel)) < (111,72,67)): #Se o pixel for preto
                pyautogui.click(xpixel+x, ypixel+y)

resp = int(input('Oque deseja fazer?\n\n[1] Desenhar\n[2] Sair\n\n'))
if (resp == 1):
    if isinstance(img, pil.Image.Image):
        print('imagem copiada')
        system.os('start mspaint')
        sleep(2)
        desenhar()
    else:
        print('Imagem não copiada! Encerrando programa...')
