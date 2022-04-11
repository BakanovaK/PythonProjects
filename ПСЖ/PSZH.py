import os

clear = lambda: os.system('cls||clear')
clear()
a = str(input('Почему ты плачешь?\n'))
clear()
import time
time.sleep(0.5)
for i in range(2):
	for s in range(3):
		print('Загрузка', '.' *(s + 1), sep = '')
		time.sleep(0.5)
		clear()
import webbrowser
webbrowser.open('https://docs.google.com/document/d/10SL--6MHD22JXdYRCDgEBptB_v76Kx6j7ESvmal6Tcg/edit?usp=sharing', new=1)
time.sleep(1)
