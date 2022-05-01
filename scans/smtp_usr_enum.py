import os

def smtp_usr_enum(ip):
    try:
        print("SMTP-USR-ENUM is starting")
        with open('25.txt', 'a') as file:
            file.write('\n\n SMTP-USER-ENUM Output \n\n')
            os.system(f"smtp-user-enum -M VRFY -U /usr/share/seclists/Usernames/Names/names.txt -t {ip}  >> 25.txt")
            
    except:
        print("an error occured please check manually wheter the port is open or not or verify the service")
