
# IPL Match Win Percentage Predictor 🏏📈

A machine learning model for predicting Indian Premier League (IPL) match outcomes. Leveraging historical match data, the model employs various features to forecast the likelihood of team victories. Built using scikit-learn and Python, with a Flask web application for user interaction.

## Workflow 🔄

1. **Data Collection 📊**
   - Utilize two datasets: `deliveries.csv` containing ball-by-ball information and `matches.csv` containing match-level information.

2. **Data Preprocessing 🛠️**
   - Load datasets into Pandas DataFrames (df and dp).
   - Import necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.
   - Perform initial data exploration to understand the structure and content of the datasets.

3. **Data Preparation 📝**
   - Calculate and aggregate the total runs scored in each inning of every match.
   - Filter the dataset to include only the first inning scores.
   - Merge necessary columns from the match dataset with the total runs dataset.

4. **Feature Engineering 🧪**
   - Standardize the teams' names to match the defined list of teams.
   - Calculate additional features like remaining score, balls remaining, wickets remaining, CRR, and RRR.
   - Filter out matches with applied Duckworth-Lewis (DL) method.
   - Engineer a feature indicating the match result.

5. **Data Transformation 🔄**
   - Apply one-hot encoding to categorical features (batting_team, bowling_team, city) using ColumnTransformer.
   - Split the data into training and testing sets using train_test_split.

6. **Model Building 🧱**
   - Choose the Logistic Regression model for its simplicity and interpretability.
   - Create a pipeline with data transformation and logistic regression.

7. **Model Training 🎓**
   - Train the pipeline on the training dataset.

8. **Model Evaluation 📈**
   - Evaluate model accuracy using the testing dataset.
   - Calculate the accuracy score to assess the performance of the model.

9. **Model Deployment 🚀**
   - Save the trained model using pickle for future use.
   - Create a Streamlit web application to provide a user interface for predicting match outcomes.
   - Allow users to select batting team, bowling team, city, remaining score, balls remaining, and wickets remaining to predict the match outcome probability.

## Requirements 📋

- Python Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit
- Datasets: `deliveries.csv`, `matches.csv`

## Usage 💻

1. Clone the repository.
2. Install the required Python libraries.
3. Run the Streamlit web application (`streamlit run app.py`).
4. Select the desired input parameters to predict match outcome probability.

## Acknowledgements 🙏

- The project data is sourced from the Indian Premier League (IPL).
- Special thanks to the developers of scikit-learn, Streamlit, and other Python libraries used in this project.
=

