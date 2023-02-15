import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.environ.get('ACCESS_TOKEN')

query = """
{
  search (query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        updatedAt
        primaryLanguage {
          name
        }
        pullRequests(states:MERGED) {
          totalCount
        }
        issues {
          totalCount
        }
        releases{
          totalCount
        }
        closedIssues: issues(states:CLOSED) {
          totalCount
        }
      }
    }
  }
}
"""

url = 'https://api.github.com/graphql'
json = {'query': query}
headers = {'Authorization': 'Bearer %s' % token}

r = requests.post(url=url, json=json, headers=headers)
print(r.text)
