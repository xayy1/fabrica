import pyautogui

pyautogui.press('win')
pyautogui.sleep(0.5)
pyautogui.write('Edge',interval=0.1)
pyautogui.press('enter')
pyautogui.sleep(2)

pyautogui.write('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores',interval=0.1)
pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.hotkey('win','shift','s')
pyautogui.mouseDown(10,10)
pyautogui.sleep(0.5)
pyautogui.mouseDown()
pyautogui.sleep(0.5)
pyautogui.moveTo(x=1900,y=1050,duration=1)
pyautogui.sleep(2)
pyautogui.mouseUp()