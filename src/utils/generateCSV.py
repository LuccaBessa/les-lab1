import csv
import os

headers = [
    'nameWithOwner',
    'createdAt',
    'updatedAt',
    'primaryLanguage',
    'pullRequests',
    'issues',
    'closedIssues',
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
                repo['updatedAt'],
                repo['primaryLanguage'],
                repo['pullRequests'],
                repo['issues'],
                repo['closedIssues'],
                repo['releases']
            ])
