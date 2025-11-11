thonimport requests
from config.settings import SETTINGS

def parse_instagram_data(profile_url, session_id):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': f'sessionid={session_id}'
    }

    response = requests.get(profile_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data: {response.status_code}")

    # Simulating Instagram data parsing
    # (In reality, this would parse the actual HTML/JSON of the page)
    parsed_data = {
        "followers": [
            {"id": "user_id_1", "full_name": "User One", "username": "userone", "is_verified": True},
            {"id": "user_id_2", "full_name": "User Two", "username": "usertwo", "is_verified": False}
        ]
    }

    return parsed_data