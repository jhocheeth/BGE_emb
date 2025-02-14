#!/bin/bash
#SBATCH -c 16
#SBATCH -t 4-00:00
#SBATCH -p gpu_quad
#SBATCH -o log_file/%x_%j.out
#SBATCH -e log_file/%x_%j.err
#SBATCH --gres=gpu:4



module load gcc/9.2.0

module load cuda/12.1

module load miniconda3


# === CHANGE THESE ===

source activate /home/jh537/.conda/envs/train_env



python git_train_V5.py


# Example : sbatch slurm_mil_moe.sh leukemia_FLT3_mil_NTU2