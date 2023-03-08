import csv
import os

headers = [
    'nameWithOwner',
    'createdAt',
    'age',
    'updatedAt',
    'timeSinceLastUpdate',
    'primaryLanguage',
    'pullRequests',
    'issues',
    'closedIssues',
    'closedIssuesRate',
    'releases'
]


def generateCSV(json, filename):
    print("Generating " + filename + " CSV...")
    with open(filename + '.csv', 'x') as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for repo in json:
            writer.writerow([
                repo['nameWithOwner'],
                repo['createdAt'],
                repo['age'],
                repo['updatedAt'],
                repo['timeSinceLastUpdate'],
                repo['primaryLanguage'],
                repo['pullRequests'],
                repo['issues'],
                repo['closedIssues'],
                repo['closedIssuesRate'],
                repo['releases']
            ])
