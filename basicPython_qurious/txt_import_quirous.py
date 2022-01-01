with open("abc.txt") as account_reader:
    lines = account_reader.readlines()
    api_key = lines[0].strip() 
    secret = lines[1].strip()

print(api_key)