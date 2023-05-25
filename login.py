d={'admin': "Sam@123"}
def login():
    userId =input('enter your name:').lower()
    if userId in d :
        st1=3
        while st1:
            passIn =input(f'enter your passwaord for{userId}:')
            if d[userId]== passIn:
                return 'successful'
            else :
                print("password does not match please try again")
                st1 -=1
        return 'failed'
    else :
        print("""username doesn't exist please try again 
        press 0 to exit
        or """)
    # check()
# login()