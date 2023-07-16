import pyautogui
import PIL as pil
import keyboard

def desenhar():
    x,y = pyautogui.position()

    # Tamanho da imagem, em x e y
    x_pixel = img.size[0]
    y_pixel = img.size[1]

    print(f'Tamanho da imagem:  {x_pixel} por {y_pixel}')
    
    for xpixel in range(0, x_pixel, 4):
        for ypixel in range(0, y_pixel, 4):
            if keyboard.is_pressed('Esc'):
                break
            if (img.getpixel((xpixel, ypixel)) < (111,72,67)): #Se o pixel for preto
                pyautogui.click(xpixel+x, ypixel+y)

#imagem na área de transferencia
img = pil.ImageGrab.grabclipboard()
if isinstance(img, pil.Image.Image) == False:
        print("Nenhuma imagem na área de transferencia. Saindo...")
else:
    img = img.resize((1280, 720))
    print("imagem encontrada! pronto para o desenho.")
    while (True):
        if keyboard.is_pressed('/'):
            desenhar()
            break