# IPl MATCH-WIN-LOSS-PREDICTOR-
A machine learning model for predicting Indian Premier League (IPL) match outcomes. Leveraging historical match data, the model employs various features to forecast the likelihood of team victories. Built using scikit-learn and Python, with a Flask web application for user interaction
WORK FLOW

Overview:
This project aims to predict the outcome of Indian Premier League (IPL) cricket matches based on various factors such as remaining score, balls remaining, wickets remaining, current run rate (CRR), and required run rate (RRR).

Workflow Steps:
Data Collection

The project uses two datasets: deliveries.csv containing ball-by-ball information and matches.csv containing match-level information.
Data Preprocessing

The datasets are loaded into Pandas DataFrames (df and dp).
Necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit are imported.
Initial data exploration is performed to understand the structure and content of the datasets.
Data Preparation

The total runs scored in each inning of every match are calculated and aggregated.
The dataset is filtered to include only the first inning scores.
The necessary columns from the match dataset are merged with the total runs dataset.
Feature Engineering

The teams' names are standardized to match the defined list of teams.
Additional features like remaining score, balls remaining, wickets remaining, CRR, and RRR are calculated.
Matches with applied Duckworth-Lewis (DL) method are filtered out.
The feature indicating the match result is engineered.
Data Transformation

One-hot encoding is applied to categorical features (batting_team, bowling_team, city) using ColumnTransformer.
The data is split into training and testing sets using train_test_split.
Model Building

Logistic Regression model is chosen for its simplicity and interpretability.
A pipeline is created with data transformation and logistic regression.
Model Training

The pipeline is trained on the training dataset.
Model Evaluation

Model accuracy is evaluated using the testing dataset.
Accuracy score is calculated to assess the performance of the model.
Model Deployment

The trained model is saved using pickle for future use.
The Streamlit web application is created to provide a user interface for predicting match outcomes.
The user interface allows users to select batting team, bowling team, city, remaining score, balls remaining, and wickets remaining to predict the match outcome probability.
