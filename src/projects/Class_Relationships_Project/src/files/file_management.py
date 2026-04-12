#PS 1st CP2 This file manages data so that it can be stored across runs
import json


#JSON reader
def JSON_reader():
    with open("Individual_Projects/Class_Relationships_Project/src/files/Characters.json", "r") as info:
        data = json.load(info)
        return data



#JSON file saving func (list of user information)
def JSON_add(new_info):
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
    with open("Individual_Projects/Class_Relationships_Project/src/files/Characters.json", "r+") as info:
        #add new dictionary to previous info
        data = json.load(info)
        data.update(new_info)
        info.truncate(0)
        info.seek(0)
        #upload that new dictionary to the JSON
        json.dump(data,info,indent=4)



#JSON editor - takes in sub second to highest level of the changed dictionary to change
def JSON_edit(changed_dict,name):
    data = JSON_reader()
    data[name] = changed_dict
    with open("Individual_Projects/Class_Relationships_Project/src/files/Characters.json", "w") as old_data:
        json.dump(data,old_data,indent=4)
