import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    # Use matplotlib to create a scatter plot using the Year column as the x-axis 
    # and the CSIRO Adjusted Sea Level column as the y-axis.
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # 3. Create first line of best fit (1880 - 2050)
    # Use linregress to get the slope and y-intercept
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create a list of years from 1880 to 2050
    x_pred = pd.Series([i for i in range(1880, 2051)])
    # Calculate the y values for the line of best fit
    y_pred = res.slope * x_pred + res.intercept
    
    # Plot the line
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1')

    # 4. Create second line of best fit (2000 - 2050)
    # Filter data for year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    
    # Use linregress on the recent data
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create a list of years from 2000 to 2050
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    # Calculate the y values
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    
    # Plot the line
    plt.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line 2')

    # 5. Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()