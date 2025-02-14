# Clinical Trial and UMLS Embedding Project

This project focuses on fine-tuning embedding models for clinical trial and medical terminology data using the BGE (BAAI General Embedding) model. The goal is to improve semantic similarity matching for medical terms, conditions, and trial descriptions.

## Project Structure

### `/parsing`
Data processing and preparation pipeline:
- Processes raw clinical trial data from clinicaltrials.gov
- Handles UMLS (Unified Medical Language System) data
- Creates training triplets (query, positive, negative examples)
- Implements sophisticated negative sampling strategies
- Generates test datasets for evaluation

### `/training`
Model fine-tuning configuration and scripts:
- Fine-tunes BGE model on medical data
- Uses distributed training across multiple GPUs
- Implements contrastive learning with triplet loss
- Handles SLURM cluster job submission
- Manages training checkpoints and logging

### `/evaluating`
Model evaluation and analysis tools:
- Implements comprehensive evaluation metrics
- Focuses on threshold-independent metrics (AUC-ROC, PR-AUC)
- Provides false positive analysis
- Generates performance visualizations
- Compares base and fine-tuned models

## Getting Started

1. Data Preparation:
   ```bash
   # Process clinical trials data
   cd parsing
   jupyter notebook Parse_clinicaltrial.gov.ipynb
   ```

2. Model Training:
   ```bash
   cd training
   sbatch train_V5.sh
   ```

3. Evaluation:
   ```bash
   cd evaluating
   jupyter notebook Triplets_AUC_NPV_PPV.ipynb
   ```

## Dependencies
- Python 3.12+
- PyTorch
- Transformers
- FlagEmbedding
- CUDA 12.1
- See individual directory READMEs for specific requirements

## Data Sources
- ClinicalTrials.gov JSON data
- UMLS Metathesaurus (MRCONSO.RRF, MRREL.RRF)

## Output
The project produces:
- Fine-tuned embedding model for medical text similarity
- Evaluation metrics and visualizations
- Analysis of model performance on medical terminology

Each directory contains its own detailed README with specific information about the components and their usage. 