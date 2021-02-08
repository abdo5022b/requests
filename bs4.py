import requests
s = requests.Session()
url = 'https://www.facebook.com/login'

res = s.get(url)
Email = input('Email >>')
password = input("Password >>")
list = [ Email ,password]
form_data = {
'email' : list[0] ,
'password' : list[1]
}
s.post(url, data=form_data)