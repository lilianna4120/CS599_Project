import pandas as pd

metadata_file = "MD_extracted.csv"
review_file = "review_extracted.csv"
output_file = "merged_data.csv"

md = pd.read_csv(metadata_file)
review = pd.read_csv(review_file)

merged = pd.merge(review, md, on = "parent_asin", how = "inner") # change how to 'left' if we want all reviews

merged.to_csv(output_file, index = False)
print(f"merged data written to {output_file}")