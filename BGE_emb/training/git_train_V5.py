import subprocess

def run_finetuning():
    command = [
        "torchrun",
        "--nproc_per_node=4",
        "-m",
        "FlagEmbedding.baai_general_embedding.finetune.run",
        "--output_dir", "/n/data1/hsph/biostat/celehs/lab/jh537/Models/Flarge_V5",
        "--model_name_or_path", "BAAI/bge-large-en-v1.5",
        "--train_data", "/home/jh537/Clinical_Trial_Embending/Clinical_Trial_data/Clinical_Trial_Triplet_v3/Train/all_triplets_4types_7neg.jsonl",
        "--learning_rate", "1e-5",
        "--fp16",
        "--num_train_epochs", "3",
        "--per_device_train_batch_size", "8",
        "--dataloader_drop_last", "True",
        "--normlized", "True",
        "--temperature", "0.1",
        "--query_max_len", "128",
        "--passage_max_len", "128",
        "--train_group_size", "8",
        "--negatives_cross_device",
        "--logging_steps", "10000000",
        "--save_steps", "100000000000",
        "--query_instruction_for_retrieval", ""
    ]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running finetuning: {e}")
        
if __name__ == "__main__":
    run_finetuning()
