import time
while True:
    time.sleep(1)
    i = 0
    while True:
        time.sleep(1)
        i += 1 
        print("2nd while looped")      
        if i> 5:
            break
    print("break 2nd while")