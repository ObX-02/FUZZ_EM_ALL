import requests
from colorama import Fore, Style
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
print("          Checking Target Reponse.......")
print("========================================")
count = 0
with open("common.txt","r")as f:
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36" 
}
    found = 0
    not_found = 0
    errors = 0
    ok = 0
    forbidden = 0
    redirect = 0
    total_requests = 0
    for data in f:
        count+=1
        full_url = Target + data.strip().lstrip("/")
        total_requests+=1
        try:
            response = requests.get(full_url, headers= headers, timeout = 3)
            size = len(response.content)
            if response.status_code == 200:
                ok+= 1
                print(Fore.GREEN + f"{count:2} {full_url}        {response.status_code}        {size} Bytes")
            elif response.status_code == 304:
                forbiddent+=1
                print(Fore.YELLOW + f"{count:2} {full_url}        {response.status_code}        {size} Bytes")
            elif response.status_code == 301:
                redirect+=1
                print(f"{count:2} {full_url}        {response.status_code}        {size} Bytes") 
            else:
                not_found+=1  
                 

        except requests.exceptions.RequestException:
            print(Fore.RED + f"Connection Failed: {full_url}")
            errors+=1
            

print("========================================")
print("             Scan Finished              ")
print("========================================")
print(f"Total Requests: {total_requests}")
print(f"200 OK: {ok}")
print(f"304 forbidden: {forbidden}")
print(f"301 Redirect: {redirect}")
print(f"404 not found: {not_found}") 
print(f"Errors: {errors}" )
print("========================================")


  

    

        