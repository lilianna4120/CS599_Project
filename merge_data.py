import pandas as pd
import sys

# metadata_file = "MD_extracted.csv"
# review_file = "review_extracted.csv"
# output_file = "merged_data.csv"
metadata_file = sys.argv[1]
review_file = sys.argv[2]
output_file = sys.argv[3]

md = pd.read_csv(metadata_file)
review = pd.read_csv(review_file)

merged = pd.merge(review, md, on = "parent_asin", how = "left") # change how to 'left' if we want all reviews

merged.to_csv(output_file, index = False)
print(f"merged data written to {output_file}")