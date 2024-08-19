try:
    # --------------------Librarys--------------------
    from colorama import Fore, init
    import os
    import shutil
    from random import randint
    # --------------------Colors--------------------
    yellow = Fore.YELLOW
    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED
    blue = Fore.BLUE
    black = Fore.BLACK
    purpel = Fore.MAGENTA
    # --------------------Banner--------------------
    # banner = text2art("                                     USB HACKING !!")
    def banner():
        print(blue+f'''
                                        {red} _____ ______  __ {blue}  __  _______ ____ 
                                        {red}/ ___// __ \ \/ / {blue} / / / / ___// __ )
                                        {red}\__ \/ /_/ /\  /  {blue}/ / / /\__ \/ __  |
                                        {red}___// ____/  /  {blue} / /_/ /___/ / /_/ / 
                                       {red}/___/_/   /__/   {blue} \____//____/_____/  
                                                    '''+green) 
    # --------------------Body--------------------
    while True:
        os.system("cls")
        banner()
        opt_num = f"""{red}[1] {white}Create Folders
{red}[2] {white}Create Files
{red}[3] {white}Copy Folder
{red}[4] {white}Copy Files
{red}[5] {white}Delete Folder
{red}[6] {white}Delete Files
{red}[7] {white}Exit"""
        print(opt_num)

        opt_input = input(blue+"Enter One Of The Options : "+green)
        # --------------------Folders--------------------
        # 1
        if opt_input == '1':
            os.system("cls")
            many_folder = 0
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)
            how_many = input(yellow+"How Many Folders ??   "+green)
            
            if how_many == '005':
                os.system("cls")
                break
            elif how_many == '002':
                os.system("cls")
                continue

            how_many = int(how_many)
            where_folder = input(purpel+"Where We Make It(Drive/folder/...) ??   "+green)
            names_folder = input(white+"Name Of Folders ??   "+green)
            
            while many_folder < how_many:
                last_name_folder = names_folder+str(randint(0, 1000000))
                address_folder = os.path.join(where_folder, last_name_folder)
                os.mkdir(address_folder)
                many_folder += 1
            else:
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_folder = input("").title()
                if user_con_folder == "":
                    os.system("cls")
                    continue
                else:
                    break
        # --------------------Files--------------------
        # 2
        elif opt_input == '2':
            os.system("cls")
            many_file = 0
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)
            how_many_file = input(yellow+"How Many Files ??   "+green)

            if how_many_file == '005':
                os.system("cls")
                break
            elif how_many_file == '002':
                os.system("cls")
                continue

            how_many_file = int(how_many_file)
            where_file = input(purpel+"Where We Make It(Drive/folder/...) ??   "+green)
            names_file = input(white+"Name Of Files ??   "+green)
            # extension = input(blue+"Please Write The File Extension(txt Or py) ??   "+green).lower()
            extension = input(blue+"Please Write The File Model(txt Or py) ??   "+green).lower()

            while many_file < how_many_file:
                last_name_file = names_file+str(randint(0, 1000000))
                file_creating = open(f"{where_file}/{last_name_file}.{extension}", "x")
                many_file += 1
                # address_file = os.path.join(where_file, last_name_file)
                # os.mknod(f"{last_name_file}.{extension}")
            else:
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_file = input("").title()
                if user_con_file == "":
                    os.system("cls")
                    continue
                else:
                    break
        # --------------------Copy Folders--------------------
        # 3
        elif opt_input == '3':
            os.system("cls")
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)
            
            where_copy_folder = input(purpel+"Folder Addresss To Copy(Drive/folder/...) ??   "+green)
            if where_copy_folder == '005':
                os.system("cls")
                break
            elif where_copy_folder == '002':
                os.system("cls")
                continue
            print(red+f"\n[!]{yellow} For pasting, please enter the name of a folder that does not exist,\nso that it will be created for you and download the files\n")
            where_paste_folder = input(purpel+"Folder Addresss To Paste(Drive/folder/...) ??   "+green)
            try:
                shutil.copytree(where_copy_folder, where_paste_folder)
                # os.copy(where_copy_folder, where_paste_folder)
                
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_file = input("").title()
                if user_con_file == "":
                    os.system("cls")
                    continue
                else:
                    break
    
            except:
                print(red+"\nERROR !!\nThis Folder Already Exists\n"+green)
                if input(white+"Do You Want To Exit ??   "+green) == "yes":
                    break
                else:
                    continue
        # --------------------Copy Files--------------------
        # 4
        elif opt_input == '4':
            os.system("cls")
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)
            
            where_copy_file = input(purpel+"File Addresss To Copy(Drive/folder/...) ??   "+green)
            if where_copy_file == '005':
                os.system("cls")
                break
            elif where_copy_file == '002':
                os.system("cls")
                continue
            where_paste_file = input(purpel+"File Addresss To Paste(Drive/folder/...) ??   "+green)
            try:
                for ff in os.listdir(where_copy_file):
                    if os.path.isfile(os.path.join(where_copy_file, ff)):
                        shutil.copy(os.path.join(where_copy_file, ff), where_paste_file)
                # shutil.copy(where_copy_file, where_paste_file)
                
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_file = input("").title()
                if user_con_file == "":
                    os.system("cls")
                    continue
                else:
                    break
            except:
                print(red+"ERROR !!"+green)
                if input(white+"Do You Want To Exit ??   "+green) == "yes":
                    break
                else:
                    continue
        # --------------------Del Folder--------------------
        # 5
        elif opt_input == '5':
            os.system("cls")
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)            

            where_del_folder = input(purpel+"Witch One(Drive/folder/...) ??   "+green)
            if where_del_folder == '005':
                os.system("cls")
                break
            elif where_del_folder == '002':
                os.system("cls")
                continue
            
            # for ff in os.listdir(where_del_folder):
            #     if os.path.isfile(os.path.join(where_del_folder, ff)):
            #         os.remove(os.path.join(where_del_folder, ff))

            try:
                # os.rmdir(where_del_folder)
                shutil.rmtree(where_del_folder)
                
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_file = input("").title()
                if user_con_file == "":
                    os.system("cls")
                    continue
                else:
                    break
            
            except:
                print(red+"\nERROR !!\nThe Folder Was Not Empty"+green)
                if input(white+"Do You Want To Exit ??   "+green) == "yes":
                    break
                else:
                    continue
        # --------------------Del Files--------------------   
        # 6             
        elif opt_input == '6':
            os.system("cls")
            print(red+"[-] Enter 005 To Exit"+green)
            print(red+"[-] Enter 002 To Back\n"+green)

            where_del_all_file = input(purpel+"Witch One(Drive/folder/...) ??   "+green)
            if where_del_all_file == '005':
                os.system("cls")
                break
            elif where_del_all_file== '002':
                os.system("cls")
                continue
            try:
                for filename in os.listdir(where_del_all_file):
                    if os.path.isfile(os.path.join(where_del_all_file, filename)):
                        os.remove(os.path.join(where_del_all_file, filename))

                
                print(blue+"\nEND Successfully !! \n"+green)
                print(f"{red}[+] {purpel}Enter To Continue ..."+green)
                user_con_file = input("").title()
                if user_con_file == "":
                    os.system("cls")
                    continue
                else:
                    break
            
            except:
                print(red+"\nERROR !!"+green)
                if input(white+"Do You Want To Exit ??   "+green) == "yes":
                    break
                else:
                    continue
        # --------------------Show Folders--------------------   
        elif opt_input == '7':
            break

        else:
            os.system("cls")
            continue
    else:
        os.system("cls")
except:
    print(red+"\nERROR !!"+green)