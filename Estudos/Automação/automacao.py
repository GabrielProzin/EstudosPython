import pyautogui
import time
#https://pyautogui.readthedocs.io/en/latest/mouse.html

pyautogui.PAUSE = 0.3

while True:
    pyautogui.click(x=917, y=762)
    pyautogui.write('Louco?')
    pyautogui.press("enter")
    pyautogui.write('Eu ja fui louco uma vez')
    pyautogui.press("enter")
    pyautogui.write('Me trancaram num quarto apertado com ratos')
    pyautogui.press("enter")
    pyautogui.write('Isso me deixou louco')
    pyautogui.press("enter")






#teste = True
#x = 0
#try:
#    while x < 10:
#        pyautogui.write('Vai trabalhar!')
#        pyautogui.press("enter")
#        x+=1
#except KeyboardInterrupt:
#    print('voce conseguiu')