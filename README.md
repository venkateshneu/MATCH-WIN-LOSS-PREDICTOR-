


# IPL Match Win Percentage Predictor
This project is a high-quality IPL (Indian Premier League) match win percentage predictor built using machine learning techniques. Leveraging a logistic regression model trained on historical IPL match data, the application accurately predicts the probability of each team winning a match based on various factors such as team performance, venue, and match progress. The user-friendly interface, powered by Streamlit, offers dropdowns and number inputs for easy interaction, providing quick insights into potential match outcomes. The model is meticulously trained and evaluated to ensure reliability, and the trained pipeline is efficiently saved for seamless future predictions.

WORK FLOW:

1. Data Collection

The project uses two datasets: deliveries.csv containing ball-by-ball information and matches.csv containing match-level information.
Data Preprocessing

2. The datasets are loaded into Pandas DataFrames (df and dp).
Necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit are imported.
Initial data exploration is performed to understand the structure and content of the datasets.
Data Preparation

3. The total runs scored in each inning of every match are calculated and aggregated.
The dataset is filtered to include only the first inning scores.
The necessary columns from the match dataset are merged with the total runs dataset.
Feature Engineering

4. The teams' names are standardized to match the defined list of teams.
Additional features like remaining score, balls remaining, wickets remaining, CRR, and RRR are calculated.
Matches with applied Duckworth-Lewis (DL) method are filtered out.
The feature indicating the match result is engineered.
Data Transformation

5. One-hot encoding is applied to categorical features (batting_team, bowling_team, city) using ColumnTransformer.
The data is split into training and testing sets using train_test_split.
Model Building

6. Logistic Regression model is chosen for its simplicity and interpretability.
A pipeline is created with data transformation and logistic regression.
Model Training

7. The pipeline is trained on the training dataset.
Model Evaluation

8. Model accuracy is evaluated using the testing dataset.
Accuracy score is calculated to assess the performance of the model.
Model Deployment

9. The trained model is saved using pickle for future use.
The Streamlit web application is created to provide a user interface for predicting match outcomes.
The user interface allows users to select batting team, bowling team, city, remaining score, balls remaining, and wickets remaining to predict the match outcome probability.



## Venkatesh Guri


- [@octokatherine](https://www.github.com/octokatherine)


## 
Python Libraries
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit 
![Logo](
)


