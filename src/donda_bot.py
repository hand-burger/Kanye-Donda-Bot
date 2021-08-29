import requests, smtplib, time
from bs4 import BeautifulSoup

url = "https://music.apple.com/ca/artist/kanye-west/2715720/see-all?section=full-albums"

sender_email = input(str('Enter your sending email: '))
password = input(str('Enter your sending email password: '))
rec_email = input(str('Enter your receiving email: '))
interval = input(str('Enter your checking interval in seconds, I reccomend no quicker than two minutes: '))
message = 'Donda by Kanye West has officialy dropped on apple music'

"""
You will most likely have to change your email account security preferences to allow less secure apps
Here's the link for Google accounts: https://www.google.com/settings/security/lesssecureapps
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

while True:
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "lxml")

    albums = soup.find("div", attrs={"aria-label": "Donda, 2021"})
    if albums == None:
        print('No luck this time, checking again. . . ')
    elif albums != None:
        server.sendmail(sender_email, rec_email, message)
        print('Finally he droppped & Email successfuly sent')
        break
    time.sleep(int(interval))