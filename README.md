![IPL Match Prediction](https://pianalytix.com/wp-content/uploads/2020/12/IPL-Match-Prediction.jpg)

# IPL Match Win Percentage Predictor 🏏📈

A machine learning model for predicting Indian Premier League (IPL) match outcomes. Leveraging historical match data, the model employs various features to forecast the likelihood of team victories. Built using scikit-learn and Python, with a Flask web application for user interaction.

## Workflow 🔄

1. **Data Collection 📊**
   - Utilizing two datasets: `deliveries.csv` containing ball-by-ball information and `matches.csv` containing match-level information.

2. **Data Preprocessing 🛠️**
   - Loading datasets into Pandas DataFrames (df and dp).
   - Importing necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.
   - Performing initial data exploration to understand the structure and content of the datasets.

3. **Data Preparation 📝**
   - Calculating and aggregating the total runs scored in each inning of every match.
   - Filtering the dataset to include only the first inning scores.
   - Merging necessary columns from the match dataset with the total runs dataset.

4. **Feature Engineering 🧪**
   - Standardizing the teams' names to match the defined list of teams.
   - Calculating additional features like remaining score, balls remaining, wickets remaining, CRR, and RRR.
   - Filtering out matches with applied Duckworth-Lewis (DL) method.
   - Engineering a feature indicating the match result.

5. **Data Transformation 🔄**
   - Applying one-hot encoding to categorical features (batting_team, bowling_team, city) using ColumnTransformer.
   - Splitting the data into training and testing sets using train_test_split.

6. **Model Building 🧱**
   - Choosing the Linear Regression model for its simplicity and interpretability.
   - Creating a pipeline with data transformation and linear regression.

7. **Model Training 🎓**
   - Training the pipeline on the training dataset.

8. **Model Evaluation 📈**
   - Evaluating model accuracy using the testing dataset.
   - Calculating the accuracy score to assess the performance of the model.

9. **Model Deployment 🚀**
   - Saving the trained model using pickle for future use.
   - Creating a Streamlit web application to provide a user interface for predicting match outcomes.
   - Allowing users to select batting team, bowling team, city, remaining score, balls remaining, and wickets remaining to predict the match outcome probability.

## Requirements 📋

- Python Libraries: pandas, numpy, scikit-learn, streamlit
- Datasets: `deliveries.csv`, `matches.csv`

## Usage 💻

1. Clone the repository.
2. Install the required Python libraries.
3. Run the Streamlit web application (`streamlit run app.py`).
4. Select the desired input parameters to predict match outcome probability.

## Acknowledgements 🙏

- The project data is sourced from the Indian Premier League (IPL) dataset.
- Thanks to the developers of scikit-learn, Streamlit, and other Python libraries used in this project.
