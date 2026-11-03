import re
import requests

def main():
    print(summary())
    get_user_option()

def option_handling(option):
    if option == 1:
        return check_username_using_official_api(get_username())
    elif option == 2:
        return check_username_using_regex(get_username())
    elif option == 3:
        return get_the_api_url(get_username())
    elif option == 4:
        return get_the_url_of_users_profile(get_username())
    elif option == 5:
        return get_num_of_public_repos(get_username())
    elif option == 6:
        return get_github_id(get_username())



def get_username():
    return (input('Enter the username for github:- '))

def get_user_option():
    while True:
        option = input('Enter your option:- ').strip()
        if option in ['.' , '/' ,]:
            continue
        try:
            option = int(option)
        except ValueError:
            continue
        else:
            if not 1<=option<=10:
                continue
            return option


def check_username_using_regex(username):
    pattern = re.search(r"/^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$/i" , username)
    if pattern:
        return 'Valid - Verified via regex'
    else:
        return 'Invalid - Verified via regex'

def check_username_using_official_api(username):
    url = get_the_api_url(username)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        login = data['login']
        if login == username:
            return f"User named {login} had been found - Verified via github's api"
        else:
            return f"Perhaps, you migth have meant a user named {login}. The user has been found - Verified via Github's api"
    elif response.status_code == 404:
        return "There is no user named {username} - Verified via github's api"
    else:
        return f"API request failed with status code {response.status_code}"

def summary():
    return("""This is a tool made in python, that mainly uses github's official api to give useful information to the user"
    You can use this to-\n1.Search for username availability\n2.Check whether a username is valid using regex\n3.Get the api url for the user's api request to DIY\n4.Get the Url of the user's profile\n5.Get the number of public repos\n6.Get the Github ID\n7.Get the avatar url of the user\n8.Get a detailed summary of the user\n9.Get the real life details of the person if any available\n10.exit"""")

def get_the_api_url(username):
    return f"https://api.github.com/users/{username}"

def get_the_url_of_users_profile(username):
    url = get_the_api_url(username)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        profile = data['html_url']
        return profile
    elif response.status_code == 404:
        return "There is no user named {username} - Verified via github's api"
    else:
        return f"API request failed with status code {response.status_code}. Try Again"

def get_num_of_public_repos(username):
    url = get_the_api_url(username)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            num = data['public_repos']
            return num
        elif response.status_code == 404:
            return "There is no user named {username} - Verified via github's api"
        else:
            return f"API request failed with status code {response.status_code}. Try Again"

def get_github_id(username):
    url = get_the_api_url(username)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if = data['id']
        return id
    elif response.status_code == 404:
        return "There is no user named {username} - Verified via github's api"
    else:
        return f"API request failed with status code {response.status_code}. Try Again"

