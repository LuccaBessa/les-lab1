import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas dataframe
df = pd.read_csv('../repos.csv')

# Create a boxplot of the 'age' column
plt.boxplot(df['age'])
plt.title('Boxplot of Age')
plt.ylabel('Age (in months)')
plt.savefig('../graphs/age_boxplot.png')
plt.clf()

# Create a boxplot of the 'pullRequests' column
plt.boxplot(df['pullRequests'])
plt.title('Boxplot of Pull Requests')
plt.ylabel('Number of Pull Requests')
plt.savefig('../graphs/pullrequests_boxplot.png')
plt.clf()

# Create a boxplot of the 'releases' column
plt.boxplot(df['releases'])
plt.title('Boxplot of Releases')
plt.ylabel('Number of Releases')
plt.savefig('../graphs/releases_boxplot.png')
plt.clf()

# Create a boxplot of the 'timeSinceLastUpdate' column
plt.boxplot(df['timeSinceLastUpdate'])
plt.title('Boxplot of Time Since Last Update')
plt.ylabel('Time Since Last Update (in hours)')
plt.savefig('../graphs/time_boxplot.png')
plt.clf()

# Create a histogram of the 'primaryLanguage' column
plt.hist(df['primaryLanguage'].dropna())
plt.title('Histogram of Primary Language')
plt.xlabel('Language')
plt.ylabel('Frequency')
plt.savefig('../graphs/language_hist.png')
plt.clf()

# Calculate the rate between closed and total issues
df['closed_rate'] = df['closedIssues'] / df['issues']

# Create a boxplot of the 'closed_rate' column
plt.boxplot(df['closed_rate'])
plt.title('Boxplot of Closed Rate')
plt.ylabel('Closed Rate')
plt.savefig('../graphs/closedrate_boxplot.png')
plt.clf()
