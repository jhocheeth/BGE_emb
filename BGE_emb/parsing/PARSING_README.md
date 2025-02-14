# Data Processing and Triplet Generation Pipeline

This directory contains a collection of Jupyter notebooks that form a data processing pipeline for creating training and testing datasets from clinical trial data and UMLS (Unified Medical Language System) data.

## Pipeline Overview

### 1. Data Extraction and Initial Processing
- `Parse_clinicaltrial.gov.ipynb`: Parses raw JSON data from clinicaltrials.gov into a structured format
  - Extracts key information like trial IDs, titles, summaries, conditions, keywords, interventions
  - Creates initial triplets with conditions, interventions, and keywords
  - Cleans and formats the data

### 2. Data Merging and Deduplication
- `MERGE.ipynb`: Handles the merging of different data sources and dataset organization
  - Merges triplets from clinical trials and UMLS data
  - Removes duplicates while preserving unique query-pos pairs
  - Creates separate training and testing datasets
  - Extracts SY (synonym) category entries for testing
  - Provides utilities for data analysis (e.g., category counts)

### 3. Negative Sample Generation
- `Similar_neg_3.2.ipynb`: Generates high-quality negative samples for training
  - Creates pseudo-random negatives based on prefix and suffix similarity
  - Implements sophisticated negative sampling strategies:
    - Suffix-based negative sampling (2 samples)
    - Prefix-based negative sampling (2 samples)
    - Random sampling for remaining negatives
  - Ensures total of 8 negative samples per entry
  - Uses multiprocessing for efficient processing

### 4. Test Set Creation
- `Create_test_file.ipynb`: Prepares test datasets for model evaluation
  - Processes SY (synonym) triplets for testing
  - Adds random negative samples
  - Creates CSV files for:
    - Positive pairs
    - Negative pairs
    - Unique terms
  - Formats data for AUC evaluation

## Data Flow
1. Raw clinical trial data → Structured JSON → Initial triplets
2. Merge with UMLS data → Deduplicated dataset
3. Generate negative samples → Complete training triplets
4. Extract test set → Format for evaluation

## Output Files
- Training data: Triplets with query, positive, and negative samples
- Testing data: 
  - Positive pairs (CSV)
  - Negative pairs (CSV)
  - Unique terms (CSV)
  - SY triplets for synonym evaluation

## Usage
Each notebook can be run independently, but they are designed to be executed in sequence:
1. Run `Parse_clinicaltrial.gov.ipynb` first to process raw data
2. Use `MERGE.ipynb` to combine and organize datasets
3. Execute `Similar_neg_3.2.ipynb` to generate negative samples
4. Finally, run `Create_test_file.ipynb` to prepare test datasets 