import requests

def update_repo_description(owner, repo_name, description, token):
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Repository description updated successfully.")
    else:
        print(f"Failed to update repository description. Status code: {response.status_code}")

# Replace these values with your GitHub username, repository name, and desired description
owner = "Dawidexk"
repo_name = "Ge_Scripts"
description = "Gerrit admin scripts"
token = "Token"

update_repo_description(owner, repo_name, description, token)
