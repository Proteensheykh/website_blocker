import time
from datetime import datetime as dt

#host_path = r'C:\Windows\System32\drivers\etc\hosts'
temp_path = r'C:\Users\USER\Documents\PROJECT\website_blocker\hosts'
redirect = '127.0.0.1'
website_list = ['facebook.com', 'www.facebook.com', 'spankbang.com', 'www.spankbang.com']

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        
        with open(temp_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + '    ' + website + '\n')
    else:
        print('Parry Time')

        with open(temp_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
    
    
    #https://1drv.ms/v/s!ApGeml7ftlUdhQvKVK46vtwB6EIn?e=ciRzvN
