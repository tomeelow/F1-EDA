import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

'''
1) Bar chart that would allow to choose options for the following: 
    - top drivers by number of wins
    - top drivers by number of pole positions
    - top drivers by number of fastest laps
    - top drivers by number of podiums
    - top drivers by number of total points
    - top drivers by the win rate
    
2) Line charts on one panel that would show all teams and their positions for a chosen decade

3) Heatmap where x-axis is the year, y-axis is the team, and the color is the number of points scored by the team in the given year
'''

# Load the data
drivers_data_df = pd.read_csv('F1Drivers_Dataset.csv')
teams_data_df = pd.read_csv('teams_updated.csv')


