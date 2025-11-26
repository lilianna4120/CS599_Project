loadMD.py: Python file to load metadata
loadReview.py: Python file to load user reviews
extractMD.py: Python file to extract metadata
extractReview.py: Python file to extract user reviews
merge_data.py: Python file to join the review and metadata files
buildGraph.py: Python file to build the graph of average rating by year, where the x-axis is the year and the y-axis is the average rating

to run the Python files - Baby indicates the file for baby products and Health indicates Health and Household products
loadMD.py:
python loadMD.py meta_Baby_Products.jsonl MD_output_Baby.jsonl
python loadMD.py meta_Health_and_Household.jsonl MD_output_Health.jsonl

loadReview.py:
python loadReview.py Baby_Products.jsonl review_output_Baby.jsonl
python loadReview.py Health_and_Household.jsonl review_output_Health.jsonl

extractMD.py:
python extractMD.py MD_output_Baby.jsonl MD_extracted_Baby.csv
python extractMD.py MD_output_Health.jsonl MD_extracted_Health.csv

extractReview.py:
python extractReview.py review_output_Baby.jsonl review_extracted_Baby.csv      
python extractReview.py review_output_Health.jsonl review_extracted_Health.csv  

merge_data.py
python merge_data.py MD_extracted_Baby.csv review_extracted_Baby.csv merged_data_Baby.csv
python merge_data.py MD_extracted_Health.csv review_extracted_Health.csv merged_data_Health.csv

buildGraph.py
python buildGraph.py merged_data_Baby.csv 
python buildGraph.py merged_data_Health.csv 
