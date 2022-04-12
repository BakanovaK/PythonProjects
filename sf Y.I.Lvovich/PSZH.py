import os
import time
import webbrowser


clear = lambda: os.system('cls||clear')
clear()

a = input('Тебе надоела учеба? ты хочешь отдохнуть от неё?\n')

clear()
time.sleep(0.5)

if (a.lower() == 'да'):
	for i in range(2):
		for s in range(3):
			print('Загрузка', '.' *(s + 1), sep = '')
			time.sleep(0.5)
			clear()
	
	webbrowser.open('https://docs.google.com/document/d/10SL--6MHD22JXdYRCDgEBptB_v76Kx6j7ESvmal6Tcg/edit?usp=sharing', new=1)
	time.sleep(1)

else:
	print('ну и ладно....(((')
	time.sleep(2.0)
	clear()
