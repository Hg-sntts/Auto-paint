import pyautogui
import PIL as pil
from time import sleep

sleep(3)

pos1 = 0
pos2 = 0

img = pil.ImageGrab.grabclipboard()
cor_desejada = (0,0,0) #preto

tamanho_tela = pyautogui.size()
largura = tamanho_tela.width
altura = tamanho_tela.height

x,y = pyautogui.position()

if isinstance(img, pil.Image.Image):
    print('imagem copiada')

    x_pixel = img.size[0]-2
    y_pixel = img.size[1]-2
    #img = img.convert('L')

    cor_pixel = img.getpixel((x_pixel, y_pixel))
    print(type(cor_pixel))
    print('Cor do pixel: ', cor_pixel)
    print('Tamanho da imagem: ', x_pixel, y_pixel)

    '''if(x_pixel >= 1366):
        x_pixel-= 400
    if(y_pixel >= 768):
        y_pixel-= 300'''
    

    for xpixel in range(0, 500, 4):
        for ypixel in range(0, 500, 4):
            if (img.getpixel((xpixel, ypixel)) < (111,72,67)): #Se o pixel for branco
                pyautogui.click(xpixel+x, ypixel+y)
