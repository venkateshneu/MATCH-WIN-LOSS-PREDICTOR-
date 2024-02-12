import streamlit as st
import pickle
import pandas as pd

# Load the teams and cities data
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

# Load the pipeline model
pipe = pickle.load(open('pipe.pkl','rb'))

# Define the Streamlit app
st.title('IPL Win Predictor')

# Define the columns for layout
col1, col2 = st.columns(2)

# Dropdown for selecting batting and bowling teams
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# Dropdown for selecting the host city
selected_city = st.selectbox('Select host city', sorted(cities))

# Number input for target score
target = st.number_input('Target')

# Number inputs for current score, overs, and wickets
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

# Button to predict probability
if st.button('Predict Probability'):
    try:
        # Calculate remaining runs, balls, and required run rate
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets = 10 - wickets
        crr = score / overs if overs != 0 else 0  # Avoid division by zero
        rrr = (runs_left * 6) / balls_left if balls_left != 0 else 0  # Avoid division by zero

        # Create input DataFrame
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'remaining_score': [runs_left],
            'balls_remaining': [balls_left],
            'wickets_rem': [wickets],
            'final_score': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Predict probabilities
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display results
        st.header(f"{batting_team} - {round(win * 100)}%")
        st.header(f"{bowling_team} - {round(loss * 100)}%")

    except Exception as e:
        # Display error message if an exception occurs
        st.error(f"An error occurred: {str(e)}")
