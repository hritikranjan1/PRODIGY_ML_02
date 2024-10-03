# Customer Segmentation using K-Means Clustering

## Author
**Hritik Ranjan**

## Project Overview
This project implements customer segmentation using K-Means clustering to analyze customer data based on age, spending score, and annual income. The analysis provides valuable insights for targeted marketing strategies and customer management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [License](#license)
- [Contact](#contact)

## Introduction
Customer segmentation is a key technique in marketing and business strategy, enabling organizations to tailor their approaches to different customer groups. This project utilizes K-Means clustering to identify distinct customer segments based on their demographic and behavioral attributes.

## Features
- Data visualization of customer demographics and behaviors.
- K-Means clustering for customer segmentation.
- 3D visualization of customer segments.

## Installation
To run this project, ensure you have Python installed on your system. Follow the steps below to install the required libraries:

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/hritikranjan1/PRODIGY_ML_02 .git
   cd customer-segmentation
2.Install the necessary libraries using pip:

    pip install pandas numpy matplotlib seaborn scikit-learn
## Dataset

The dataset used for this project is hritik.csv. It contains various customer attributes including:

  1.CustomerID: Unique identifier for each customer (dropped in analysis).
  2.Age: Age of the customer.
  3.Annual Income (k$): Annual income of the customer in thousands of dollars.
  4.Spending Score (1-100): Score assigned by the company based on customer behavior and spending patterns.
  5.Gender: Gender of the customer.

Make sure to place the hritik.csv file in the same directory as your script or update the path accordingly.
Usage

1Follow these steps to run the analysis:

  1.Update the file path in the script to point to your dataset:

    python

     customer_data = pd.read_csv("/path/to/your/hritik.csv")  # Change this to your actual file path

2.Run the script:

    python customer_segmentation.py

3.View the results in the console and generated plots. Various visualizations will provide insights into customer demographics and clustering.

  ## Libraries:
        pandas: Used for data manipulation and analysis.
        numpy: Used for numerical operations.
        matplotlib and seaborn: Used for data visualization.
        scikit-learn: Used for implementing the K-Means clustering algorithm.

  ##  Functions:
        Data visualization functions (violin plots, boxplots, bar plots).
        K-Means clustering algorithm to segment customers into different groups.

## Evaluation Metrics

    Within-cluster sum of squares (WCSS): Measures the compactness of the clusters. Lower values indicate better clustering.
    Silhouette score (not explicitly implemented): Can be used to assess the quality of clustering by measuring how similar an object is to its own cluster compared to other clusters.

## Results

After running the script, you will see several visualizations:

    Age distribution of customers.
    Spending scores and annual income distributions.
    Gender distribution of customers.
    3D scatter plot showing the relationship between age, income, and spending score.
    K-Means clustering results visualized in 3D.
Example Output:

makefile

    Name: Hritik ranjan
    GitHub: https://github.com/hritikranjan1
    LinkedIn: https://www.linkedin.com/in/hritik-ranjan-05a835230/
 ##  Contact

        Name: Hritik ranjan
    GitHub: https://github.com/hritikranjan1
    LinkedIn: https://www.linkedin.com/in/hritik-ranjan-05a835230/

  
