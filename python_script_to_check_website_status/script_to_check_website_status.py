import requests
import bs4
import smtplib
import os

email_add = os.environ.get('EMAIL_ADD')
password = os.environ.get('EMAIL_PASS')

def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "!!!!!! 100 days of devops site is down"
    body = "Check the status of 100 days of devops"
    message = f'Subject: {subject}\n\n {body}'
    s.sendmail(email_add, email_add, message)
    s.quit()


producturl="http://100daysofdevops.com/contact-us/"

res = requests.get(producturl, timeout=5)
if res.status_code != 200:
    send_email()

soup = bs4.BeautifulSoup(res.text,'html.parser')

elems = soup.select('#post-67 > div > div > header > h2')
try:
    if elems[0].text != "Welcome":
        send_email()
except Exception as e:
    send_email()
