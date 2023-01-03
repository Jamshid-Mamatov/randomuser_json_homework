import json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    male_list=[]
    for user in data['users']:
        if user['gender']=='male':
            male_list.append(user)

    return male_list

with open("users.json") as f:
    data=json.load(f)
    get_male_users(data=data)