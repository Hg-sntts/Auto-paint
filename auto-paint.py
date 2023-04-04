import pyautogui
import PIL as pil
from time import sleep

sleep(3)

img = pil.ImageGrab.grabclipboard()
cor_desejada = (0,0,0) #preto

x,y = pyautogui.position()

if isinstance(img, pil.Image.Image):
    print('imagem copiada')

    x_pixel = img.size[0]-2
    y_pixel = img.size[1]-2
    #img = img.convert('L')

    cor_pixel = img.getpixel((x_pixel, y_pixel))
    print(type(cor_pixel))
    print('Cor do pixel: ', cor_pixel)
    print('Tamanho da imagem: ', y_pixel, x_pixel)

    for xpixel in range(0, x_pixel, 3):
        for ypixel in range(0, y_pixel, 3):
            if (img.getpixel((xpixel, ypixel)) < (50,50,50)):
                pyautogui.click(xpixel+x, ypixel+y)
