"""
This app uses Python, numpy, pandas, and matplotlib to generate a set of data points and plot them on a graph.
"""

# imports
import numpy as np                # for numerical operations
import pandas as pd         # for data manipulation
import matplotlib.pyplot as plt  # for data visualization

"""
Create a function 'gen_data' that generates a set of data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the range of x values to generate.
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated as a non-linear function of x with excessive random noise: y = x ^ 1.5  + noise.
- The data frame is sorted by the 'x' values.
Error Handling:
- If 'x_range' is not a tuple of two integers, raise a ValueError with the message "x_range must be a tuple of two integers".
Example:
- gen_data((0, 100)) returns a data frame with 'x' values between 0 and 100 and 'y' values calculated as described.
- The function should also handle the case where the range is invalid (e.g., if the first element is greater than the second).
"""
def gen_data(x_range):
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(i, int) for i in x_range):
        raise ValueError("x_range must be a tuple of two integers")
    
    if x_range[0] >= x_range[1]:
        raise ValueError("Invalid range: the first element must be less than the second element")
    
    # Generate random x values within the specified range
    x = np.random.randint(x_range[0], x_range[1], size=100)
    
    # Calculate y values with a non-linear function and excessive noise
    noise = np.random.normal(0, 10, size=x.shape)
    y = x ** 1.5 + noise
    
    # Create a pandas DataFrame
    data = pd.DataFrame({'x': x, 'y': y})
    
    # Sort the DataFrame by 'x' values
    data.sort_values(by='x', inplace=True)
    
    return data

"""
Create a function 'plot_data' that plots the data points from the data frame. The copilot response should contain python docstrings for the function.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- The data points are plotted as a scatter plot.
- The plot has a title 'Data Points', x-axis label 'x', and y-axis label 'f(x)'.
- The x-axis limits are set to the minimum and maximum of the 'x' values in the data frame.
- The y-axis limits are set to the minimum and maximum of the 'y' values in the data frame.
- The plot is displayed using plt.show().
Error Handling:
- If 'data' is not a pandas DataFrame or does not contain the required columns, raise a ValueError with the message "data must be a pandas DataFrame with 'x' and 'y' columns".
Example:
- plot_data(gen_data((0, 100))) displays a scatter plot of the generated data points.
"""
def plot_data(data):
    """
    Plots the data points from a pandas DataFrame as a scatter plot.

    Args:
        data (pd.DataFrame): A pandas DataFrame with two columns, 'x' and 'y'.

    Returns:
        None

    Raises:
        ValueError: If 'data' is not a pandas DataFrame with 'x' and 'y' columns.

    Details:
        - The data points are plotted as a scatter plot.
        - The plot has a title 'Data Points', x-axis label 'x', and y-axis label 'f(x)'.
        - The x-axis limits are set to the minimum and maximum of the 'x' values in the data frame.
        - The y-axis limits are set to the minimum and maximum of the 'y' values in the data frame.
        - The plot is displayed using plt.show().
    """
    if not isinstance(data, pd.DataFrame) or not all(col in data.columns for col in ['x', 'y']):
        raise ValueError("data must be a pandas DataFrame with 'x' and 'y' columns")
    
    # Create a scatter plot of the data points
    plt.scatter(data['x'], data['y'], color='blue', label='Data Points')
    
    # Set the title and labels
    plt.title('Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Set the x and y limits
    plt.xlim(data['x'].min(), data['x'].max())
    plt.ylim(data['y'].min(), data['y'].max())
    
    # Show the plot
    plt.legend()
    plt.show()


"""
Create a function 'main' that generates data and plots it.
Returns:
- None
Details:
- Calls 'gen_data' with a specified range and then calls 'plot_data' to display
the generated data points.
- The range for 'gen_data' is set to (0, 100).
"""
def main():
    # Generate data within the specified range
    data = gen_data((0, 100))
    
    # Plot the generated data
    plot_data(data)
    
if __name__ == "__main__":
    main()

