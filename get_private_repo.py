import os
from getpass import getpass
import urllib.parse

user = input('User name: ')
token = getpass('Git Token: ')
token = urllib.parse.quote(token) # your token is converted into url format
repo_name = input('Repo name: ')
branch_name = input('Branch name: ')

if branch_name == "master":
  #cmd_string = 'git clone https://{password}/{user}/{repo_name}.git'.format(user=user, password=token, repo_name=repo_name)
  cmd_string = 'git clone https://{git_token}@github.com/{user}/{repo_name}.git'.format(user=user, git_token=token, repo_name=repo_name)
else:
  cmd_string = 'git clone -b {branch_name} https://{git_token}@github.com/{user}/{repo_name}.git'.format(user=user, git_token=token, repo_name=repo_name, branch_name=branch_name)

os.system(cmd_string)
cmd_string, token = "","" # removing the token from the variable

#git clone https://username:password@github.com/path_to/myRepo.git
#https://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@github.com/blackscomber/mldl4twithpyincolab.git