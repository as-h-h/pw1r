import json

def check_data(data):
    corr_keys = ["id", "name", "surname", "age", "city", "knows",]
    #a    
    if not isinstance(data, dict):
        return False
    
    #b
    if "cities" not in data or "people" not in data:
        return False
    
    #c
    if not isinstance(data["cities"], list):
        return False

    #d
    if not isinstance(data["people"], list):
        return False
    
    for city in data["cities"]:
        #e
        if not isinstance(city, dict):
            return False
        #f
        if "name" not in city and "population" not in city:
            return False
        #if not isinstance(city["name"], str)

    for person in data["people"]:
        #e
        if not isinstance(person, dict):
            return False
        #g
        keys = list(person.keys())
        if not set(corr_keys).issubset(keys):
            return False
    return True



def load_data(file_name): 
    with open(file_name, encoding='utf8') as f:
        data = json.load(f)
    if check_data(data):
        return data
    else:
        return None