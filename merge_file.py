import pandas as pd

baby = pd.read_csv("merged_data_Baby.csv")
health = pd.read_csv("merged_data_Health.csv")

baby["category"] = 0
health["category"] = 1

combined = pd.concat([baby, health], ignore_index=True)

combined.to_csv("combined.csv", index=False)
