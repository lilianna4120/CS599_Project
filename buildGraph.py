import pandas as pd
import matplotlib.pyplot as plt
import sys

# load dataset
dataset = sys.argv[1]
# df = pd.read_csv("merged_data.csv")
df = pd.read_csv(dataset)

# convert to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 'ms')

# extract year
df['year'] = df['timestamp'].dt.year

# aggregate average rating by year
yearly = df.groupby('year')['rating'].mean().reset_index()

# to count how many reviews there are by year
year_counts = df.groupby('year').size().reset_index(name='review_count')
# print(year_counts)

plt.figure(figsize = (12,6))
plt.plot(yearly['year'], yearly['rating'], marker = 'o')
plt.title("Average Rating by Year")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.xticks(yearly['year'])
plt.grid(True)
plt.show()

plt.figure(figsize=(12,6))
plt.plot(year_counts['year'], year_counts['review_count'], marker='o')
plt.title("Number of Reviews per Year")
plt.xlabel("Year")
plt.ylabel("Number of Reviews")
plt.xticks(year_counts['year'])
plt.grid(True)
plt.show()


