import requests
from pprint import pprint
import os
import json
import argparse


VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--reponame","--r", dest="reponame",
                        help='Please enter the repository name')
my_parser.add_argument("--deleterepo","--d",dest="deleterepo",
                        help='To delete a repository')
my_parser.add_argument("--listrepo","--l",dest="listrepo",
                        help='To list a repository owned by "all, owner, public, private, member" default value is all', default='all', choices = VALID_TYPES)


args = my_parser.parse_args()

token = os.environ.get("GITHUB_TOKEN")

# https://advanced-python.readthedocs.io/en/latest/rest/list_repos.html

reponame = args.reponame
deleterepo = args.deleterepo
listrepo = args.listrepo


GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

if reponame:
    r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)

if deleterepo:
    username = input("Please enter your GitHub username: ")
    r = requests.delete("https://api.github.com/repos/{}/{}".format(username,deleterepo), headers=headers)
    print(r)

if listrepo:
    username = input("Please enter your GitHub username: ")
    output = requests.get("https://api.github.com/users/{}/repos".format(username))
    output = json.loads(output.text)
    for repo in output:
        pprint(repo["name"])
