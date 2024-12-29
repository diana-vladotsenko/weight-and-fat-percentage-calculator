#Ulesanne 6
sugu = str(input("Valige sugu - N(naine) või M(mees)"))
if sugu in ["N", "Naine", "naine", "n"]:
            print("On valitud Naine. Sisesta edasi andmeid ")
            #Ideaalkaal
            pikkus_naine = int(input("Teie pikkus on "))
            vanus_naine = int(input("Teie vanus on "))
            ideaalkaal_naine = (3 * pikkus_naine - 450 + vanus_naine)*0.225+40.5
            print ("Teie ideaalkaal on ", ideaalkaal_naine,"kg")
            #Rasvaprotsent
            kaal_naine = int(input("Teie kaal on "))
            rasvaprotsent_naine = (kaal_naine - ideaalkaal_naine)/kaal_naine * 100+22
            print ("Teie rasvaprotsent on ", rasvaprotsent_naine, "%")
#vanus 10-16
if vanus_naine >=10  and vanus_naine <=16:
    if rasvaprotsent_naine < 10:
        print("Teie rasvaprotsent on alla normi.")
    elif 10 <= rasvaprotsent_naine <=18:
        print ("Teie rasvaprotsent on normis.")
    elif 19 <= rasvaprotsent_naine <=23:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_naine > 23:
        print ("Te olete rasvunud.") 
#vanus 17-39
if vanus_naine >= 17 and vanus_naine <=39:
    if rasvaprotsent_naine < 12:
        print("Teie rasvaprotsent on alla normi.")
    elif 12 <= rasvaprotsent_naine <=20:
        print ("Teie rasvaprotsent on normis.")
    elif 21 <= rasvaprotsent_naine <=25:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_naine > 25:
        print ("Te olete rasvunud.") 
#vanus 40-55
if vanus_naine >= 40 and vanus_naine <=55:
    if rasvaprotsent_naine < 13:
        print("Teie rasvaprotsent on alla normi.")
    elif 13 <= rasvaprotsent_naine <=21:
        print ("Teie rasvaprotsent on normis.")
    elif 22 <= rasvaprotsent_naine <=26:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_naine > 26:
        print ("Te olete rasvunud.") 

            
elif sugu in ["M", "mees", "Mees", "m"]:
            print ("On valitud Mees. Sisesta edasi andmeid ")
            #Ideaalkaal
            pikkus_mees = int(input("Teie pikkus on "))
            vanus_mees = int(input("Teie vanus on "))
            ideaalkaal_mees = (3 * pikkus_mees - 450 + vanus_mees)*0.25+45
            print ("Teie ideaalkaal on ", ideaalkaal_mees,"kg")
            #Rasvaprotsent
            kaal_mees = int(input("Teie kaal on "))
            rasvaprotsent_mees = (kaal_mees - ideaalkaal_mees)/kaal_mees * 100+15
            print ("Teie rasvaprotsent on ", rasvaprotsent_mees, "%")
#vanus 10-16
if vanus_mees >=10  and vanus_mees <=16:
    if rasvaprotsent_mees < 10:
        print("Teie rasvaprotsent on alla normi.")
    elif 10 <= rasvaprotsent_mees <=18:
        print ("Teie rasvaprotsent on normis.")
    elif 19 <= rasvaprotsent_mees <=23:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_mees > 23:
        print ("Te olete rasvunud.") 
#vanus 17-39
if vanus_mees >= 17 and vanus_mees <=39:
    if rasvaprotsent_mees < 12:
        print("Teie rasvaprotsent on alla normi.")
    elif 12 <= rasvaprotsent_mees <=20:
        print ("Teie rasvaprotsent on normis.")
    elif 21 <= rasvaprotsent_mees <=25:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_mees > 25:
        print ("Te olete rasvunud.") 
#vanus 40-55
if vanus_mees >= 40 and vanus_mees <=55:
    if rasvaprotsent_mees < 13:
        print("Teie rasvaprotsent on alla normi.")
    elif 13 <= rasvaprotsent_mees <=21:
        print ("Teie rasvaprotsent on normis.")
    elif 22 <= rasvaprotsent_mees <=26:
        print ("Teie rasvaprotsent on ule normi.")
    elif rasvaprotsent_mees > 26:
        print ("Te olete rasvunud.") 
