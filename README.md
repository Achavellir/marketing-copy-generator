# Marketing Copy Generator

This project provides a command‑line tool for generating marketing copy for product catalogs using a large language model (OpenAI GPT‑3.5).

## Features
* Reads a CSV file containing product information (name, description, features, tone) and uses the OpenAI API to generate persuasive marketing copy.
* Supports batch processing of multiple products and writes results to an output CSV.
* Tracks usage cost and latency per product when the OpenAI API key is provided.

## Usage
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the CLI:
```bash
python main.py --input sample_products.csv --output generated_copy.csv --api-key YOUR_OPENAI_API_KEY
```

3. Check `generated_copy.csv` for the generated copy.

## Files
* `main.py` – Entry point for the CLI.
* `utils.py` – Helper functions for generating prompts and calling the OpenAI API.
* `requirements.txt` – Python dependencies.
* `sample_products.csv` – Example input file with product data.

## Extensibility
This project is designed to run as a batch job on platforms such as AWS Batch.  You can containerize it with Docker and schedule it to process new product catalogs periodically.  Consider integrating MLflow for experiment tracking or adding support for other generative AI providers.
