import json
import sys

# input_file = "Baby_Products.jsonl"
# output_file = "review_output.jsonl"
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as fp, open(output_file, 'w', encoding='utf-8') as out_fp:
    for line in fp:
        data = json.loads(line)
        json.dump(data, out_fp, ensure_ascii=False)
        out_fp.write('\n')  # write one JSON object per line

print(f"All output written safely to {output_file}")