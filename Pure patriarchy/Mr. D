import time
import webbrowser
import smtplib
import os
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

clear = lambda: os.system('cls||clear')
clear()

print('Здравствуйте, Дмитрий Андреевич!')
time.sleep(1.0)
a = input('Что бы Вы хотели?\n')

clear()
time.sleep(0.5)


#приветствие

clear()
print('Я приняла Ваш запрос, господин!')
time.sleep(1.5)
clear()
for f in range(100):
	clear()
	print('Обработка Вашего ответа - ', f + 1, '%', sep = '')
	time.sleep(0.03)
clear()
for i in range(2):
	for s in range(3):
		print('Загрузка', '.' *(s + 1), sep = '')
		time.sleep(0.5)
		clear()


#запуск сайта

if (a.lower() == 'расслабиться'):
	webbrowser.open('https://rt.pornhub.com', new=1)
	time.sleep(1)


#отправка текстового сообщения

elif (a.lower() == 'массаж'):
	def send_email(message):
		sender = "gospodin.nda@gmail.com"
		password = "gospodind"
		devochka = "bakanova2001ksysha@gmail.com"

		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()

		try:
			server.login(sender, password)
			msg = MIMEText(message)
			msg["Subject"] = "СРОЧНО!"
			server.sendmail(sender, devochka, msg.as_string())

			# server.sendmail(sender, sender, f"Subject: СРОЧНО!\n{message}")

			print("Ваша просьба передана Вашей девочке! Ожидайте выполнения в ближайшее время!")
			time.sleep(2.0)
			clear()
			return " "
		except Exception as _ex:
			return f"{_ex}\nCheck your login or password please!"

	def main():
		message = 'Господин хочет массаж'
		print(send_email(message=message))

	if __name__ == "__main__":
		main()


#отправка текстового сообщения

elif (a.lower() == 'поесть'):
	def send_email(message):
		sender = "gospodin.nda@gmail.com"
		password = "gospodind"
		devochka = "bakanova2001ksysha@gmail.com"

		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()

		try:
			server.login(sender, password)
			msg = MIMEMultipart()
			msg["Subject"] = "СРОЧНО!"

			msg.attach(MIMEText('Приготовь мне '))
			msg.attach(MIMEText(message))

			server.sendmail(sender, devochka, msg.as_string())

			print("Ваша просьба передана Вашей девочке! Ожидайте выполнения в ближайшее время!")
			time.sleep(2.0)
			clear()
			return " "
		except Exception as _ex:
			return f"{_ex}\nCheck your login or password please!"

	def main():
		message = input("Что бы Вы хотели поесть? ")
		print(send_email(message=message))

	if __name__ == "__main__":
		main()


elif (a.lower() == 'погулять'):
	print('Пожалуйста, ознакомьтесь со списком по ссылке и выберите места для прогулки:')
	time.sleep(2.0)
	webbrowser.open('https://docs.google.com/spreadsheets/d/1Izmq33VMaW-tGQRGhj5dGs-x3RM_uhQQX_1bhHwcayc/edit?usp=sharing', new=1)
	time.sleep(1)
	clear()
	def send_email(message):
		sender = "gospodin.nda@gmail.com"
		password = "gospodind"
		devochka = "bakanova2001ksysha@gmail.com"

		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()

		try:
			server.login(sender, password)
			msg = MIMEMultipart()
			msg["Subject"] = "СРОЧНО!"

			msg.attach(MIMEText('Хочу погулять, вот выбранные места: '))
			msg.attach(MIMEText(message))

			server.sendmail(sender, devochka, msg.as_string())

			print("Ваша просьба передана Вашей девочке! Ожидайте выполнения в ближайшее время!")
			time.sleep(2.0)
			clear()
			return " "
		except Exception as _ex:
			return f"{_ex}\nCheck your login or password please!"

	def main():
		message = input("Какие места Вы выбрали? ")
		print(send_email(message=message))

	if __name__ == "__main__":
		main()


#любовь-морковь

elif (a.lower() == 'любви'):
	clear()
	print('Мой дорогой Димочка!')
	print('Я тебя очень-очень-очень сильно люблю')
	print('Спасибо тебе за все, что ты делаешь для меня')
	time.sleep(2.0)
	print('      ')
	print('            $$$$$$$$      $$$$$$$$$')
	time.sleep(0.5)
	print('          $$$$$$$$$$$$  $$$$$$$  $$$$')
	time.sleep(0.5)
	print('         $$$$$$$$$$$$$$$$$$$$$$$$  $$$')
	time.sleep(0.5)
	print('         $$$$$$$$$$$$$$$$$$$$$$$$  $$$')
	time.sleep(0.5)
	print('         $$$$$$$$$$$$$$$$$$$$$$$$  $$$')
	time.sleep(0.5)
	print('          $$$$$$$$$$$$$$$$$$$$$$  $$$')
	time.sleep(0.5)
	print('           $$$$$$$$$$$$$$$$$$$$$$$')
	time.sleep(0.5)
	print('              $$$$$$$$$$$$$$$$$')
	time.sleep(0.5)
	print('                $$$$$$$$$$$$$')
	time.sleep(0.5)
	print('                   $$$$$$$')
	time.sleep(0.5)
	print('                     $$$')
	time.sleep(0.5)
	print('                      $')
	print('      ')
	print('      ')
	print('      ')
	time.sleep(2.0)


#отправка текстового сообщения при незаданном варианте ответа

else:
	def send_email(message):
		sender = "gospodin.nda@gmail.com"
		password = "gospodind"
		devochka = "bakanova2001ksysha@gmail.com"

		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()

		try:
			server.login(sender, password)
			msg = MIMEMultipart()
			msg["Subject"] = "СРОЧНО!"

			msg.attach(MIMEText('Хочу '))
			msg.attach(MIMEText(message))

			server.sendmail(sender, devochka, msg.as_string())

			print("Ваша просьба передана Вашей девочке! Ожидайте выполнения в ближайшее время!")
			time.sleep(2.0)
			clear()
			return " "
		except Exception as _ex:
			return f"{_ex}\nCheck your login or password please!"

	def main():
		message = a
		print(send_email(message=message))

	if __name__ == "__main__":
		main()
