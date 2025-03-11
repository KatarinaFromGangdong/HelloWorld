try:
    user = input("Enter command: ")
    while True:
        if "hello" in user:
            print("success")
            break
        else:
            print("error")
            break
except:
    print("Error 404")