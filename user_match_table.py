
def match_Tables(user_table, all_tables):
    matched_tables = [] # match table list.

    for i in all_tables:
        if int(i['bahis']) <= int(user_table['bahis']) and user_table['Total'] == i['Total']:
            matched_tables.append(i)
            #here we made a filter by bahis and total. total can be diffrent for each table options

    if len(matched_tables) == 0: # if we couldn't find any match table then returning false
        return False
    
    return matched_tables

    