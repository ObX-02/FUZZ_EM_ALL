print("========================================")
print("            FUZZ 'EM  ALL !!            ")
print("========================================")
Target = input("Enter Target's URL: ").strip()
if not Target.startswith(("http://","https://")):
    Target = "https://" + Target
    
print(f"Target Selected: {Target}")
count = 0
with open("common.txt","r")as f:
    print("========================================")
    print("Reading Wordlist......")
    print("========================================")


    for data in f:
        count+=1
        print(f"{count:2} {Target}{data.strip()}")
    

        