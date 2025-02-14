# Model Performance Evaluation and Metrics

This directory contains scripts for evaluating the performance of embedding models on similarity tasks using various metrics.

## Overview

The evaluation pipeline (`Triplets_AUC_NPV_PPV.ipynb`) assesses model performance using both threshold-independent and threshold-dependent metrics.

### Threshold-Independent Metrics
We prioritize these metrics as they provide a more robust comparison between base and fine-tuned models:

1. **AUC-ROC (Area Under the Receiver Operating Characteristic Curve)**
   - Measures the model's ability to distinguish between positive and negative pairs across all possible thresholds
   - Range: 0 to 1 (1 being perfect classification)
   - Advantage: Not affected by similarity score distribution shifts

2. **PR-AUC (Area Under the Precision-Recall Curve)**
   - Focuses on the trade-off between precision and recall
   - More informative than ROC-AUC for imbalanced datasets
   - Computed using trapezoidal integration

3. **Average Precision (AP)**
   - Summarizes the precision-recall curve as a weighted mean of precision at each threshold
   - Provides a single score that captures the shape of the precision-recall curve

### Threshold-Dependent Metrics
For these metrics, we use an optimal threshold determined by Youden's J statistic rather than a fixed threshold:

- **Why Optimal Threshold?**
  - Fine-tuning can shift the distribution of cosine similarities
  - Using the same fixed threshold (e.g., 0.5) for both base and fine-tuned models may not be meaningful
  - Optimal threshold adapts to each model's similarity distribution

Metrics computed at optimal threshold:
- F1-Score
- Precision
- Recall

## Implementation Details

### Data Processing
- Handles both positive and negative pairs
- Removes NaN values
- Uses batch processing for memory efficiency
- GPU acceleration for embedding computation

### Key Features
1. Batched computation of embeddings
2. Efficient cosine similarity calculation
3. Comprehensive evaluation metrics
4. Visualization of ROC and PR curves

### False Positive Analysis
Includes a separate script for analyzing false positives:
- Identifies pairs incorrectly classified as similar
- Helps in understanding model limitations
- Useful for improving negative sampling strategies

## Usage

```python
# Load required libraries
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics import roc_auc_score, precision_recall_curve

# Load your evaluation data
positive_pairs_df = pd.read_csv('path_to_positive_pairs.csv')
negative_pairs_df = pd.read_csv('path_to_negative_pairs.csv')

# Run evaluation
# See Triplets_AUC_NPV_PPV.ipynb for complete implementation
```

## Output
- Numerical metrics (AUC-ROC, PR-AUC, AP, F1, etc.)
- ROC curve visualization
- Precision-Recall curve visualization
- False positive analysis results (optional)

## Notes
- Always use threshold-independent metrics (AUC-ROC, PR-AUC, AP) for primary model comparison
- When threshold-dependent metrics are needed, use model-specific optimal thresholds
- Consider the balance of your test set when interpreting results 