import requests
import os
import json

token = os.environ.get("GITHUB_TOKEN")
reponame = input("Please enter the repo name you want to create : ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r)
