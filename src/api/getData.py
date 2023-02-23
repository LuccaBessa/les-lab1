import os
import requests
from os.path import join, dirname


def getData():
    token = os.environ.get('ACCESS_TOKEN')
    after = 'null'
    hasNextPage = True
    data = []

    while hasNextPage:
        query = """
        {
            search (query: "stars:>100", type: REPOSITORY, first: 10, after: %s) {
                pageInfo {
                    startCursor
                    hasNextPage
                    endCursor
                }
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
                        closedIssues: issues(states:CLOSED) {
                            totalCount
                        }
                        releases{
                            totalCount
                        }
                    }
                }
            }
        }
        """ % after

        url = 'https://api.github.com/graphql'
        json = {'query': query}
        headers = {'Authorization': 'Bearer %s' % token}

        response = requests.post(url=url, json=json, headers=headers).json()

        hasNextPage = response['data']['search']['pageInfo']['hasNextPage'] if response['data']['search']['pageInfo']['hasNextPage'] else False
        after = '"%s"' % response['data']['search']['pageInfo']['endCursor']

        for repoData in response['data']['search']['nodes']:
            data.append({
                'nameWithOwner': repoData['nameWithOwner'],
                'createdAt': repoData['createdAt'],
                'updatedAt': repoData['updatedAt'],
                'primaryLanguage': repoData['primaryLanguage']['name'] if  repoData['primaryLanguage'] else 'None',
                'pullRequests': repoData['pullRequests']['totalCount'],
                'issues': repoData['issues']['totalCount'],
                'closedIssues': repoData['closedIssues']['totalCount'],
                'releases': repoData['releases']['totalCount']
            })

    return data
