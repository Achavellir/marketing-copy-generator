import argparse
import csv
import time
from utils import build_prompt, generate_copy


def process_file(input_path: str, output_path: str, api_key: str) -> None:
    with open(input_path, newline='', encoding='utf-8') as infile, open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['generated_copy']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            prompt = build_prompt(row)
            start = time.time()
            try:
                copy = generate_copy(prompt, api_key) if api_key else 'API key not provided'
            except Exception as e:
                copy = f"Error: {e}"
            row['generated_copy'] = copy
            writer.writerow(row)
            duration = time.time() - start
            print(f"Processed {row.get('name', 'item')} in {duration:.2f} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate marketing copy using GPT-3.5')
    parser.add_argument('--input', required=True, help='Path to input CSV file')
    parser.add_argument('--output', required=True, help='Path to output CSV file')
    parser.add_argument('--api-key', default='', help='OpenAI API key')
    args = parser.parse_args()
    process_file(args.input, args.output, args.api_key)
