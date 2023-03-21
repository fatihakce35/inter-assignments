from tables import random_Tables
from user_table import user_Table
from user_match_table import match_Tables
#importing functions


game_tables = random_Tables() #generate random 10 table for our game

#main loop
while 1:
    print("Okey masasina hos geldiniz ! Lutfen asagidaki menuden islem yapiniz:")
    #menu
    user_choice = input("[1] Masa Sec\n[2] Masalari goruntule\n[3] Masalari yenile\n[4] Cikis\nSecim: ")

    #user choices and conditions

    #getting game info from user
    if user_choice == "1":
        bahis = input("Lutfen bahis giriniz (200-2500 arasinda): ")
        hizli = input("Masa Hizli olsun mu? (evet veya hayir): ").lower()
        teke_tek = input("Teke-tek olsun mu? (evet veya hayir): ").lower()
        rovans = input("Rovans olsun mu? (evet veya hayir): ").lower()

        user_info = user_Table(bahis, hizli, teke_tek, rovans) #sending to our function to control

        if user_info: #if user entered right info 
            user_matched_tables = match_Tables(user_info, game_tables) #getting match function for user to find table

            if user_matched_tables: #if table exists by info print them
                print("\nUygun masalar:")
                for i in user_matched_tables:
                    print(f"Bahis: {i['bahis']}, Hizli: {i['hizli']}, Teke-tek: {i['teke_tek']}, Rovans: {i['rovans']}\n")

            else: # if not then print message to user
                print("\nUygun masa bulunamadi !\n")
        
        else: #If user entered any wrong info
            print("\nMasa bilgilerini yanlis girdiniz ! Lutfen tekrar deneyin\n")


        
    elif user_choice == "2": #showing to user game tables.
        print("Oyun icindeki su anki masalar: \n\n")
        for i in game_tables:
            
            
            print(f"Bahis: {i['bahis']}, Hizli: {i['hizli']}, Teke-tek: {i['teke_tek']}, Rovans: {i['rovans']}\n")
            
        
    elif user_choice == "3": # refreshing game tables
        game_tables = random_Tables()
        print("\n Masalar yenilendi ! \n")


    elif user_choice == "4": #exit
        exit()


    else: #if user enter any wrong options in menu
        print("\nLutfen dogru secim yapiniz !\n")