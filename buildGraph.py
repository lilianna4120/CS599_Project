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

plt.figure(figsize = (12,6))
plt.plot(yearly['year'], yearly['rating'], marker = 'o')
plt.title("Average Rating by Year")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.xticks(yearly['year'])
plt.grid(True)
plt.show()
