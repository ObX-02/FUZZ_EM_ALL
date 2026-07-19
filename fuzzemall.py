import requests
from colorama import Fore, Style
def send_request(full_url,headers):
    response = requests.get(full_url,headers=headers, timeout = 10)
    size = len(response.content)
    return response,size
    
def process_response(response,line,result):
    if response.status_code == 200:
        print(Fore.GREEN + line)
        result.write(line +"\n")
        
    if response.status_code == 403:
        print(Fore.YELLOW + line)
        result.write(line +"\n")
    
    if response.status_code == 301:
        print(line)
        result.write(line +"\n")

    if response.status_code == 500:
        print(line)
        result.write(line +"\n")
       

print("========================================")
print("            FUZZ 'EM  ALL !!            ")
print("========================================")
Target = input("Enter Target's URL: ").strip()
if not Target.startswith(("http://","https://")):
    Target = "https://" + Target
if not Target.endswith("/"):
    Target = Target + "/"
    
print(f"Target Selected: {Target}")
with open("common.txt","r")as f:
    print("========================================")
    print("Reading Wordlist......")
    print("========================================")

    count = 0
    for data in f:
        count+=1
        full_url = Target + data.strip().lstrip("/")
        print(f"{count:2} {full_url}") 
print("========================================")
print(" Fuzz 'Em All Scan Report               ")
print("========================================")
count = 0

with open("common.txt","r")as f:
    with open("result.txt","w",encoding = "utf-8")as result:

        headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36" 
        }
        not_found = 0
        errors = 0
        ok = 0
        forbidden = 0
        redirect = 0
        server_error =0
        total_requests = 0
        for data in f:
            count+=1
            full_url = Target + data.strip().lstrip("/")
            total_requests+=1
            try:
                response,size = send_request(full_url,headers)         
                line = f"{count:2} {full_url}        {response.status_code}        {size} Bytes"
                if response.status_code == 200:
                    ok += 1
                    process_response(response,line,result)
                elif response.status_code == 403:
                    forbidden+=1
                    process_response(response,line,result)   
                elif response.status_code == 301:
                    redirect+=1
                    process_response(response,line,result)
                elif response.status_code == 500:
                        server_error+= 1
                        process_response(response,line,result)
                else:
                    not_found+=1  
                        

            except requests.exceptions.RequestException:
                print(Fore.RED + f"Connection Failed: {full_url}")
                errors+=1
                #result.write(line+ "\n")
            

print("========================================")
print("             Summary             ")
print("========================================")
print(f"Total Requests: {total_requests}")
print(f"200 = OK: {ok}")
print(f"403 = Forbidden: {forbidden}")
print(f"301 = Moved Permanently (Redirect): {redirect}")
print(f"404 = Not found: {not_found}")
print(f"500 = Internal Server Error: {server_error}") 
print(f"Errors: {errors}" )
print("========================================")
print("========================================")
print("Also Data is stored in result.txt file")
print("========================================")



  

    

        