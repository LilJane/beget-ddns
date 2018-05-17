#!/usr/bin/env python3

import urllib.request
my_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
login = 'YOUR LOGIN on Beget.ru'
password = 'YOUR PASSWORD on Beget.ru'
domain = 'YOUR DOMAIN to create a DDNS'

req = urllib.request.urlopen('https://api.beget.com/api/dns/changeRecords?login=' + login + '&passwd=' + password + '&input_format=json&output_format=json&input_format=json&output_format=json&input_data=%7B%22fqdn%22%3A%22' + domain + '%22%2C%22records%22%3A%7B%22A%22%3A%5B%7B%0D%0A%22priority%22%3A10%2C%22value%22%3A%22' + my_ip + '%22%7D%5D%7D%7D').read().decode('utf8')
print ('ваш текущий IP ' + my_ip)
if req == '{"status":"success","answer":{"status":"success","result":true}}':
  print ('Успешно')
else:
  print ('Ошибка')

  

