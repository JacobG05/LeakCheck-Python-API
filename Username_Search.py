import requests

# Function to search for a username
def search_username(api_key, username):
    url = f'https://leakcheck.io/api/v2/query/{email}'
    headers = {
        'Accept': 'application/json',
        'X-API-Key': api_key
    }
    response = requests.get(url, headers=headers)
    return response

# Your API key (Keep this secret :))
api_key = 'your_api_key_here'

# Prompts for a username to search
username = input('Enter the username to search: ')

# Making the request to API
response = search_username(api_key, username)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    if data['success']:
        print('Query was successful.')
        print('Results found:', data['found'])
        print('Quota remaining:', data['quota'])
        print('Results:')
        for entry in data['result']:
            print('\nEntry:')
            for key, value in entry.items():
                print(f'{key}: {value}')
    else:
        print('Query was not successful.')
else:
    print(f'Error: {response.status_code}')
