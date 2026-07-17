import requests
print("========================================")
print("            FUZZ 'EM  ALL !!            ")
print("========================================")
Target = input("Enter Target's URL: ").strip()
if not Target.startswith(("http://","https://")):
    Target = "https://" + Target
    
print(f"Target Selected: {Target}")
with open("common.txt","r")as f:
    print("========================================")
    print("Reading Wordlist......")
    print("========================================")

    count = 0
    for data in f:
        count+=1
        full_url = Target + data.strip()
        print(f"{count:2} {full_url}") 
print("========================================")
print("Checking Target Reponse.......")
print("========================================")
f.close()
count = 0
with open("common.txt","r")as f:
    for data in f:
        count+=1
        full_url = Target + data.strip()
        response = requests.get(full_url)
        print(f"{count:2} {full_url}        {response.status_code}") 
        
        
  

    

        