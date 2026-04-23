# Email Forensics Project

## Overview
This project analyzes emails to determine whether they are legitimate or suspicious using email header analysis and automation.

## Tools Used
- Python
- CSV datasets (Enron + Spam dataset)
- Real email headers

## Dataset
- Public datasets with over 300 emails
- Additional real email headers for authentication analysis (SPF, DKIM, DMARC)

Large dataset used:
https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset

Due to GitHub file size limits, the full dataset is not included in this repository.

## How to Run

1. Open terminal
2. Navigate to project folder:
3. Run the script:

## Output
- results.csv will be generated

## Key Learning
- Email headers contain useful forensic data
- SPF, DKIM, and DMARC help verify emails
- Automation allows large-scale analysis

## Limitations
- Not all datasets include authentication fields
- Some emails cannot be fully verified
