import requests
def login():
    ur = 'https://www.instagram.com/'
    with requests.session() as c  :
        c.get(ur)
        token =  c.cookies['csrftoken']
        payload = { 'password':'@ir_pycon','username':'@ir_pycon','access_token':token}
        post = c.post(ur,data=payload,allow_redirects=True)
        edit = c.get('https://www.instagram.com/accounts/edit/')
        print(edit.url)
        try:
            print(' is succes to connect')
        except KeyError:
            pass


login()
