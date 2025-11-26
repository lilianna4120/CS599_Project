import json
import csv
import sys

# input_file = "review_output.jsonl"
# output_file = "review_extracted.csv"
input_file = sys.argv[1]
output_file = sys.argv[2]

extract_fields = ["rating", "parent_asin", "timestamp", "helpful_vote"]

count = 0

with open(input_file, 'r', encoding = 'utf-8') as input, open(output_file, 'w', newline = '', encoding = 'utf-8') as output:
    writer = csv.DictWriter(output, fieldnames=extract_fields)
    writer.writeheader()

    for line in input:
        try:
            data = json.loads(line.strip())
            row = {field: data.get(field, None) for field in extract_fields}
            writer.writerow(row)
        except json.JSONDecodeError:
            count += 1
            continue # skip any malformed JSON lines

print(f"extracted fields written to output file name {output_file}")
# print(count)