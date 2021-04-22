import smtplib
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML

addr_from = "nikser86@gmail.com"
addr_to = 'el.piankova@gmail.com'
body = "text mail from Python"

msg = MIMEMultipart()                    # Создаем сообщение
msg.attach(MIMEText(body, 'plain'))      # Добавляем в сообщение текст
msg['From'] = addr_from                  # Адресат
msg['To'] = addr_to                      # Получатель
msg['Subject'] = 'Тема Python'

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login(addr_from, 'pqsnstipbztmobduo')
# smtp_object.sendmail(from_addr="your_test_login@gmail.com", to_addrs="z_tamara@ukr.net", msg="It's works!")
smtp_object.send_message(msg)
smtp_object.quit()
