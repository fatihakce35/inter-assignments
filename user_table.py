def user_Table(bahis, hizli, teke_tek, rovans):
    #checking user entered info
    if not bahis.isdigit() or not (int(bahis) > 200 and int(bahis) < 2500):
        return False
    if hizli not in ['evet', 'hayır', 'hayir'] or teke_tek not in ['evet', 'hayır', 'hayir'] or rovans not in ['evet', 'hayır', 'hayir']:
        return False
    
    #creating object for user
    user_table = {
        "bahis" : bahis ,
        "hizli" : hizli,
        "teke_tek" : teke_tek,
        "rovans" : rovans,
        "Total" : None
    }
    #calculating the total
    user_table["Total"] = (user_table["rovans"] == "evet") * 4 + (user_table["teke_tek"] == "evet") * 2 + (user_table["hizli"] == "evet") * 1

    return user_table