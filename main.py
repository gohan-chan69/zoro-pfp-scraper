import os
import requests
from json import loads
import random

logo = '''
\033[38;5;5m▒███████▒ ▒█████   ██▀███   ▒█████  
\033[38;5;13m▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒
\033[38;5;212m░ ▒ ▄▀▒░ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒
\033[38;5;218m  ▄▀▒   ░▒██   ██░▒██▀▀█▄  ▒██   ██░
\033[38;5;219m▒███████▒░ ████▓▒░░██▓ ▒██▒░ ████▓▒░
\033[38;5;213m░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
\033[38;5;218m░░▒ ▒ ░ ▒  ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ 
░ ░ ░ ░ ░░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒  
\033[38;5;219m  ░ ░        ░ ░     ░         ░ ░  
░                                   '''
class image_scraper:
  def __init__(self, channel_id):
    self.token = "TOKEN HERE!!!!!!" #ToKeN HeRe!!!
    self.headers = {
      "Authorization": f"{self.token}"
    }
    self.channel_id = channel_id
  def get_hash(self, id):
    self.user_id = id
    self.r = requests.get(f'https://discord.com/api/v9/users/{self.user_id}',headers=self.headers)
    self.json = self.r.json()
    self.hash = self.json['avatar']
  def get_image(self):
    self.image_url = f"https://cdn.discordapp.com/avatars/{self.user_id}/{self.hash}.png"
    self.res = requests.get(self.image_url, stream = True)
    self.number = random.randint(1, 12438076032)
    self.num = str(self.number)
    self.file = open(f"{self.num}.png", "wb")
    self.file.write(self.res.content)
    self.file.close()
    print(f'\033[38;5;77m[+] successfully scraped pfp from {self.user_id}')
  def scraper(self):
     self.r = requests.get(f"https://discord.com/api/v8/channels/{self.channel_id}/messages", headers=self.headers)
     jsonnn = loads(self.r.text)
     self.lst = []
     os.remove('users.txt')
     with open("users.txt","a", errors="ignore") as a:  
       for i in jsonnn:
          a.write(i['author']['id'])
          a.write('\n')
  def run(self, id):
    self.get_hash(id)
    self.get_image()
print(logo)
chan = str(input('enter channle id >> '))
run = image_scraper(chan)
run.scraper()
member_ids = open('users.txt', 'r')
txt = member_ids.read().split()
for id in list(txt):
  run.run(id)
