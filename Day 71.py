#Day 71: Interactive data visualizations

#Create interactive data visualizations with Plotly or Bokeh.

# Install necessary libraries
# pip install plotly bokeh

import pandas as pd
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool
from bokeh.layouts import column

# Enable Bokeh output in Jupyter Notebooks
output_notebook()

# Sample Data
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 15, 13, 17, 14],
    'Category': ['A', 'B', 'A', 'B', 'A']
})

# -------------------- Plotly Interactive Scatter Plot --------------------
plotly_fig = px.scatter(df, x='X', y='Y', color='Category', size='Y',
                        hover_data=['Category'], title='Plotly Interactive Scatter Plot')

# Display Plotly Plot
plotly_fig.show()

# -------------------- Bokeh Interactive Line Plot --------------------
# Create a Bokeh figure
bokeh_fig = figure(title="Bokeh Interactive Line Plot", 
                   x_axis_label='X', y_axis_label='Y', 
                   tooltips=[("X", "@x"), ("Y", "@y")])

# Add a line to the plot
bokeh_fig.line(df['X'], df['Y'], line_width=2, legend_label="Line")

# Display Bokeh Plot
show(bokeh_fig)
