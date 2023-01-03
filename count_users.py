from from_json import read_json
import json
def count_users(data:dict)->int:
    """Counts the number of users in the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        int: The number of users
    """
    # Count the number of users
    
    return len(data['users'])

with open('users.json') as f:
    data=json.load(f)
    count_users(data=data)