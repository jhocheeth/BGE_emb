# BGE Model Fine-tuning Configuration

This directory contains the files needed to run the fine-tuning process for the BGE (BAAI General Embedding) model on clinical trial data.

## Files Overview

### `git_train_V5.py`
Python script that configures and runs the model fine-tuning process using the FlagEmbedding framework.

Key configurations:
- Uses BAAI/bge-large-en-v1.5 as the base model
- Distributed training across 4 GPUs
- Training parameters:
  - Learning rate: 1e-5
  - Epochs: 3
  - Batch size: 8 per device
  - Max sequence length: 128 for both queries and passages
  - Temperature: 0.1
  - Training group size: 8
  - FP16 precision
  - Cross-device negative sampling enabled

### `train_V5.sh`
SLURM batch script for submitting the training job to a GPU cluster.

Configuration details:
- Resources:
  - 16 CPU cores
  - 4 GPUs (gpu_quad partition)
  - 4-day runtime limit
- Environment:
  - Loads required modules:
    - gcc/9.2.0
    - cuda/12.1
    - miniconda3
  - Activates custom conda environment: train_env

## Usage

1. Ensure all dependencies are installed in the conda environment
2. Submit the training job using:
   ```bash
   sbatch train_V5.sh
   ```

## Output
- Log files are stored in `log_file/` directory:
  - Standard output: `[jobname]_[jobid].out`
  - Error logs: `[jobname]_[jobid].err`

## Model Output
The fine-tuned model will be saved to:
`/n/data1/hsph/biostat/celehs/lab/jh537/Models/Flarge_V5` 