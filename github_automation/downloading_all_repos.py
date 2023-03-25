import requests
import os

# Replace with your GitHub username and personal access token
username = "your-username"
access_token = "your-access-token"

# Set the base URL for the GitHub API
base_url = "https://api.github.com"

# Create a session with the access token to authenticate requests
session = requests.Session()
session.auth = (username, access_token)

# Get the list of repositories for the authenticated user
repositories_url = f"{base_url}/user/repos"
response = session.get(repositories_url)
repositories = response.json()

# Loop over the repositories and clone them to a local directory
for repository in repositories:
    name = repository["name"]
    clone_url = repository["clone_url"]
    print(f"Cloning {name} from {clone_url}")
    os.system(f"git clone {clone_url}")
