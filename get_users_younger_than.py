import json
def get_users_yonger_than(data:dict, age:int)->list:
    """Gets all users younger than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    user_list=[]
    for user in data['users']:
        
        if user['age']<age:

            user_list.append(user)

    return user_list

with open('users.json') as f:
    data=json.load(f)
    age=25
    get_users_yonger_than(data=data,age=age)