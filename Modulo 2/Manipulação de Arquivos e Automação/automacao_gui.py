import pyautogui as at

at.hotkey("win","r")
programa = at.prompt("Digite o nome do programa que deseja abrir: ")
at.write(programa, 0.2)
at.press("enter")