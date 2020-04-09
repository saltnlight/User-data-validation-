import string
import random

while(True):
    # collect interns data
    firstname = input("First Name: ") 
    intern_data.append(firstname) 
        
    lastname = input("Last Name: ") 
    intern_data.append(lastname)
    
    email = input("Email: ") 
    intern_data.append(email) 
    
    print('\n')

    # declaring the length of the random string used to create password
    n = 5
    rnd_str = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(n))
    # The initial password 
    old_pwd = f'{firstname[:2]}{rnd_str}{lastname[-2:]}'

    
    intern_data.append(old_pwd)
    print("Your Password is: ",old_pwd)

    # Confirming if user is okay with the initial password 
    confirm_pwd = input("Do you wish to change your Password(y/n): ")
    if(confirm_pwd == ('y' or 'Y' or 'yes' or 'Yes')):
        while(True):
            new_pwd = input("Input Your Password: ") 
            if(len(new_pwd) < 7):
                print("Your Password is too short") 
            else:
                intern_data[-1] = new_pwd
                key = f'{firstname[:2]}{new_pwd[2:4]}'
                interns_login_details.update({key:intern_data})
                break 
    
    elif(confirm_pwd == ('n' or 'N' or 'no' or 'No')):
        key = f'{firstname[:2]}{old_pwd[2:4]}'
        interns_login_details.update({key:intern_data})  
        
    print("\n") 
    
    # confirming if user wants to exit program
    Exit = input("Want to record other details? (y/n): ") 
    if(Exit == ('y' or 'Y' or 'yes' or 'Yes')):
        continue 

    if(Exit == ('n' or 'N' or 'no' or 'No')):
        for user in interns_login_details:
            print(interns_login_details[user])
        break
