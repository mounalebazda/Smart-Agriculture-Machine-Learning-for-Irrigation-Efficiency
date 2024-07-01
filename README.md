# Integrated Application of MongoDB and Machine Learning for Agricultural Data Analysis

# Project Overview:
This repository contains scripts for an integrated application utilizing MongoDB and Machine Learning techniques to analyze agricultural data. The project focuses on importing data from CSV files into MongoDB, querying the data for insights, and building predictive models to optimize irrigation needs based on environmental factors.

# Technologies Used:

- MongoDB: NoSQL database for flexible storage and efficient querying of agricultural data.
- PyMongo: Python library for interacting with MongoDB, used for data insertion, querying, and manipulation.
- Scikit-Learn: Python library for Machine Learning, employed to create and evaluate predictive models.
- Decision Tree Classifier: Machine Learning model utilized to predict irrigation requirements based on environmental and crop-specific features.
  
# Project Files:

- load.py: Python script to import CSV data into MongoDB. It ensures data integrity through validation and uses PyMongo for efficient data insertion.

- query_data.py: Script for querying MongoDB to extract specific agricultural data. It demonstrates PyMongo's capabilities for data retrieval and manipulation.

- train_and_test.py: Python script for creating, training, and testing Machine Learning models using Scikit-Learn. It includes the implementation of a Decision Tree Classifier to predict irrigation requirements.

