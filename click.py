import sys
import time
import pyautogui

if len(sys.argv) < 3:
    print("Por favor, forneça as coordenadas x e y como argumentos. Exemplo: click.py 500 250")
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])

print(f"Clicando em x: {x} y: {y}")

time.sleep(5)
pyautogui.click(x=x, y=y)

print(f"Clique efetuado com sucesso em x: {x} y: {y}")
