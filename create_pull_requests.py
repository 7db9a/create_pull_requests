import requests
import json
import argparse
import os

# Define command line arguments
parser = argparse.ArgumentParser(description='Create a pull request on GitHub via API.')
parser.add_argument('owner', help='The owner of the repository')
parser.add_argument('repo', help='The name of the repository')
parser.add_argument('base', help='The base branch for the pull request')
parser.add_argument('head', help='The head branch for the pull request')
parser.add_argument('title', help='The title of the pull request')
parser.add_argument('body', help='The body of the pull request')

# Parse command line arguments
args = parser.parse_args()

# Define the repository and branch you want to create a pull request against
repo_owner = args.owner
repo_name = args.repo
base_branch = args.base
head_branch = args.head

# Define your personal access token with the appropriate scopes for making API requests
with open('env.list', 'r') as env_file:
    token = env_file.readline().split('=')[1].strip()

# Define the title and body of the pull request
title = args.title
body = args.body

# Define the URL for the GitHub API endpoint for creating pull requests
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"

# Define the headers for the API request, including the authorization token and content type
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Define the data for the API request, including the base and head branch names, title, and body
data = {
    "title": title,
    "body": body,
    "head": head_branch,
    "base": base_branch
}

# Send the API request to create the pull request and get the response
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check the response status code to see if the pull request was created successfully
if response.status_code == 201:
    print("Pull request created successfully!")
else:
    print("Error creating pull request:", response.status_code)
