Task 1: User Overview Analysis

Overview

This module is designed to analyze the user behavior data provided by the telecom dataset. The goal is to identify key user patterns, clean the data for insights, and aggregate meaningful metrics for further exploration. The processed results can guide business decisions, such as marketing strategies or product offerings.

Workflow

Data Loading:

Connects to a MongoDB database to fetch user data from the telecom database's user_data collection.

Data Preprocessing:

Cleans the data by handling missing values and outliers.

Ensures the dataset is ready for analysis.

User Behavior Analysis:

Aggregates metrics such as session count, session duration, and total data usage (download + upload).

Prepares the dataset for visualizations and further statistical analysis.

Scripts and Modules

1. task1_user_analysis.ipynb

A Jupyter Notebook for loading, cleaning, and analyzing user behavior data.

Steps:

Connects to MongoDB.

Cleans the data using the preprocessing module.

Aggregates user behavior metrics.

Saves processed data to a CSV file for further analysis.

2. Supporting Python Scripts

src/preprocessing.py: Contains the logic for cleaning data.

src/user_analysis.py: Aggregates user behavior metrics.

src/mongodb_connector.py: Handles MongoDB connection and data retrieval.

File Structure

week2_challenge/
├── data/
│   ├── raw/               # Raw input files
│   ├── processed/         # Processed output files
├── notebooks/
│   ├── task1_user_analysis.ipynb
├── src/
│   ├── preprocessing.py
│   ├── mongodb_connector.py
│   ├── user_analysis.py
├── README.md

Usage

Prerequisites

MongoDB installed and running on localhost (port 27017).

Python environment with dependencies installed:

pip install -r requirements.txt

Steps to Execute

Run the Notebook:

Open task1_user_analysis.ipynb in Jupyter Notebook.

Execute the cells step-by-step to load, clean, and analyze data.

Inspect the Results:

Cleaned data is saved to data/processed/user_behavior.csv.

Use this file for additional visualizations or reporting.

Outputs

Aggregated user behavior metrics:

Total sessions, session duration, download/upload data, and total data.

Processed data saved as CSV.

Future Work

Visualize aggregated metrics.

Perform advanced statistical analysis.

Integrate with the final dashboard.

Author

Olana Kenea

