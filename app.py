import streamlit as st
import pandas as pd
import pickle

# Declaring the teams and their logos
teams = {
    'Sunrisers Hyderabad': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFNUOHxX-5sofC3Iioht3A6_naxWEImhNUKs6eU6xqjxYJjOa1OLc_hxKRkckg_F6bnG2XzSrAsKQpgYpeXPzFkwNLHQwS5xVrYaL7aKn155nR2J0dPCunLn4LrR8d-bLjqfaLhpAG2tGRZF4RuWgblEy_1DhbmszchchOWOs3ZwAZ_Lj-1bT535Ye/s7200/Original%20Sunrisers%20Hyderabad%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Mumbai Indians': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcIHFJONN-c6wVsb8I0TI5u1He8Vh5aUlmZ7vPzd6paraXfCf5r-bNdOoT3rqBA5S8Yu3DwefbB4C_Utu6a4E1XUXtdo28k2ViLDYs2fDS7cG9LO0S6ESd5pEZrE1GvYAf6M0_dTs9OibYMQAwkOQZvALvo-ggMxtTh_4JINiQsYeBWtQ0APFedzCZ/s7200/Original%20Mumbai%20Indians%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Royal Challengers Bangalore': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEMirAmSelGzQqwMqkzMifgCNy9asa4lGjk7tFe7WlVAQ3NU7eGj8nP0c-NRXNY6ZN5FgrDJV0k_UjOLa8rUHJDfEzFsj9qxgL_DxfB0y4RlFli0AnCxNqWXZ9wCATAZ1FBoZafwsUWddYNpVOyBEAxK7yIdLy4OkVjkUMEDErfWKE_54Rt2WW9iXL/s1178/Original%20Royal%20Challengers%20Bangalore%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Kolkata Knight Riders': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw4FPuHDf0g4n2Gaf_prBrTXdS7GO6zGVcS-Lx4ioHzH-HUUGm5gY7Sj2vmy_6HwxtSZ2fojvZrXqCUIljlZy_aenyml7DLwx3mRXTS-qWBHsBFpt85nq8Y7__HB6uK3JystxJDwx0KoLubgsAIWIH6xXoh2nxjLDM2bNV08uHlBj3zy6SQmfSIUuZ/s1024/Original%20Kolkata%20Knight%20Riders%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Kings XI Punjab': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWofXDOj6B3eYR3eBKQaPeJjTsblyohHrqK1JO4BEojD0u_Izr_2kIxmrI7Oli8_EvW9tNxB4Qi_OotqkyIWTkOsg6xIroj5U39vvmbGDPSJJXkSn5mzAF58_Mz5Fg8uIrXfJnXWlWrqSig2uxfuUGCrV3wPlZwuZ1OtWVXZUhWYeIzJyrH7klLVer/s1540/Original%20Punjab%20Kings%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Chennai Super Kings': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn3plcgt5OnAx_VelXAj9Z8TWBiqg6B-xgCJ__kuFeXr1ClntuhvVu0IugURU6TfyHk9qUuECEpos1E5ayEmx0fAupMIvNLQnLOwavDhBYxkIwvRv9cmm7_qHZmlcSwr3Un-hJpy92AooR9Qn77PUcr4yRgAORYwoTBjTYOmyYlHbZ0nDyaL3HWqUk/s2141/Original%20Chennai%20Super%20Fun%20Logo%20PNG%20-%20SVG%20File%20Download%20Free%20Download.png',
    'Rajasthan Royals': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHxGVAL3asVmq-N8vAbTJ0Wk1C7WQNO4yr_O-7dIDgrszmr7L1ODXPuc5IzB8VGr941igDjeEX8OSZ1db2sDpn5uziRk1BVYAVRZBltH4A5FJGhfjmn8PzDLcP7qxCXVyuYQr1uaLktAqoNefxAgjVGXGXIcec8WYXBO4lB-4vtCCmcu2C9RhG5XXm/s1024/Original%20Rajasthan%20Royals%20Logo%20PNG-SVG%20File%20Download%20Free%20Download.png',
    'Delhi Capitals': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixNFCNIFm0aH1xUBTkbrLQdE__aSNP32JP1zsee3iJW5va96W_r3qyl486fHQilJQjaVBJt0Fl0xAawdBD4duYEg6Sj-MgCNvVfWuA3UpO4oXBr4qt8WeaaS2Fhtbac8mfzE_euPhJ9hQUVxAgWQDLG1WgrJaSv1I2L4XgNGvFoxrdWQq_LUi82XIw/s944/Original%20Delhi%20Capitals%20Logo%20PNG-SVG%20File%20Download%20Free%20Download.png'
}

# Declaring the venues
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load model
pipe = pickle.load(open('EdgeQuest.pkl', 'rb'))

st.title('Edge-Quest: IPL Predictor')
st.image('TataIPL.jpg', use_column_width=True)

# Layout for team and city selection
col1, col2 = st.columns(2)

with col1:
    battingteam = st.selectbox('Select the batting team', sorted(teams.keys()))

with col2:
    bowlingteam = st.selectbox('Select the bowling team', sorted(teams.keys()))

city = st.selectbox('Select the city where the match is being played', sorted(cities))

# Layout for match details
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score', min_value=0)

with col4:
    overs = st.number_input('Overs Completed', min_value=0.0)

with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0)

target = st.number_input('Target', min_value=0)

if st.button('Predict Probability'):
    # Calculations
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    current_run_rate = score / (overs + 1e-9)  # Avoid division by zero
    required_run_rate = (runs_left * 6) / (balls_left + 1e-9)  # Avoid division by zero

    # Create DataFrame for prediction
    input_df = pd.DataFrame({
        'batting_team': [battingteam], 'bowling_team': [bowlingteam],
        'city': [city], 'runs_left': [runs_left], 'balls_left': [balls_left],
        'wickets': [wickets_left], 'total_runs_x': [target],
        'cur_run_rate': [current_run_rate], 'req_run_rate': [required_run_rate]
    })

    # Predict
    result = pipe.predict_proba(input_df)
    lossprob = result[0][0]
    winprob = result[0][1]

    # Determine which team is the winner and which is the loser
    if winprob > lossprob:
        winner_team = battingteam
        loser_team = bowlingteam
        winner_prob = winprob
        loser_prob = lossprob
    else:
        winner_team = bowlingteam
        loser_team = battingteam
        winner_prob = lossprob
        loser_prob = winprob

    # Display results using Streamlit's markdown and HTML
    st.markdown(f"""
<style>
.container-card {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    margin: 20px auto;
    background-color: #f0f8ff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 90%; /* Adjusted width for responsiveness */
    max-width: 1200px; /* Max width for larger screens */
}}

.result-card {{
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 90%; /* Adjusted width for responsiveness */
    max-width: 400px; /* Max width for larger screens */
    height: 240px;
    position: relative;
    overflow: hidden;
}}

.result-card img {{
    width: 100px;
    height: 75px;
    margin-bottom: 15px;
}}

.result-card h2 {{
    color: #007bff;
    font-size: 1.25rem;
    margin-bottom: 5px;
}}

.result-card .progress-bar {{
    height: 40px;
    border-radius: 5px;
    text-align: center;
    line-height: 40px;
    color: #fff;
    font-weight: bold;
    position: relative;
    bottom: 10px;
    left: 5px;
    transition: width 2s ease;
    width: 0%;
}}

.winner {{
    box-shadow: 0 4px 12px rgba(40, 167, 69, 0.5);
}}

.winner .progress-bar {{
    background-color: rgba(40, 167, 69, 0.7);
}}

.loser {{
    box-shadow: 0 4px 12px rgba(220, 53, 69, 0.5);
}}

.loser .progress-bar {{
    background-color: rgba(220, 53, 69, 0.7);
}}

.container-card:hover .winner .progress-bar {{
    width: {round(winner_prob * 100)}%;
}}

.container-card:hover .loser .progress-bar {{
    width: {round(loser_prob * 100)}%;
}}

@media (max-width: 768px) {{
    .container-card {{
        flex-direction: column;
    }}
    
    .result-card {{
        width: 100%;
        max-width: 90%; /* Adjusted max-width for mobile screens */
    }}
    
    .result-card img {{
        width: 80px;
        height: 60px;
    }}
}}
</style>
<div class="container-card">
    <div class="result-card winner">
        <img src="{teams[winner_team]}" alt="{winner_team} Logo">
        <h2>{winner_team} Win Probability</h2>
        <div class="progress-bar">
            {round(winner_prob * 100)}%
        </div>
    </div>
    <div class="result-card loser">
        <img src="{teams[loser_team]}" alt="{loser_team} Logo">
        <h2>{loser_team} Win Probability</h2>
        <div class="progress-bar">
            {round(loser_prob * 100)}%
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

