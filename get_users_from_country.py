import json
def get_users_from_country(data:dict, country:str)->list:
    """Gets all users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:
        list: A list of users
    """
    user_list=[]
    for user in data['users']:
        
        if country==user.get('country'):

            user_list.append(user)

    return user_list

with open('users.json') as f:
    data=json.load(f)
    country="USA" 
    get_users_from_country(data=data,country=country)