import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF, XPos, YPos

def generate_random_dataframe(rows: int, cols: int) -> pd.DataFrame:
    """
    Generates a random dataframe with specified number of rows and columns.
    
    Parameters:
        rows (int): Number of rows in the dataframe.
        cols (int): Number of columns in the dataframe.

    Returns:
        pd.DataFrame: A dataframe with random data.
    """
    # Column names as 'Col1', 'Col2', ..., 'ColN'
    column_names = [f'Col{i+1}' for i in range(cols)]

    # Generate random data
    data = np.random.randn(rows, cols)

    # Create the dataframe
    df = pd.DataFrame(data, columns=column_names)
    
    return df


def create_seaborn_chart_from_dataframe(df: pd.DataFrame, filename: str) -> None:
    """
    Generates a line plot for the data in the DataFrame using Seaborn and saves it as an image file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        filename (str): The name of the file to save the plot to.
    """
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.set_theme(style="whitegrid")   # Set the style of the plot using Seaborn

    # Creating a line plot for each column in the DataFrame
    ax = sns.lineplot(data=df)

    plt.title('Line Plot of DataFrame')  # Add a title to the plot
    plt.xlabel('Index')  # Label for the x-axis
    plt.ylabel('Values')  # Label for the y-axis
    plt.legend(title='Columns', title_fontsize='13', fontsize='10', loc='upper right', labels=df.columns)
    plt.savefig(filename)  # Save the figure to a file
    plt.close()  # Close the plotting window to free up system resources


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Data and Chart Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_table(self, df):
        self.set_fill_color(200, 220, 255)  # Light blue background for header
        self.set_text_color(0)  # Black text
        self.set_font('Arial', 'B', 10)  # Bold font for header

        # Column widths calculated as a fraction of page width
        column_widths = [self.epw / len(df.columns)] * len(df.columns)
        
        # Header
        for header in df.columns:
            self.cell(column_widths[0], 10, str(header), border=1, ln=0, align='C', fill=True)
        self.ln()

        # Reset font for data rows
        self.set_font('Arial', size=10)
        self.set_fill_color(255, 255, 255)  # White background for data rows
        # Data rows
        for idx, row in df.iterrows():
            for i, item in enumerate(row):
                self.cell(column_widths[i], 10, str(item), border=1)
            self.ln()

def create_pdf_from_data_and_charts(dataframes: list[pd.DataFrame], chart_paths: list[str], filename: str):
    pdf = PDF()
    pdf.add_page()

    # Add dataframes to the PDF
    for df in dataframes:
        pdf.add_page()
        pdf.add_table(df)  # Add formatted table
        pdf.ln(10)  # Add a line break after each table

    # Add charts to the PDF
    for chart in chart_paths:
        pdf.add_page()
        pdf.image(chart, x=10, y=10, w=180)  # Adjust size as needed

    pdf.output(filename)


# Assuming you have two dataframes and two chart files
# df1 = pd.DataFrame({'A': range(5), 'B': range(5, 10)})
# df2 = pd.DataFrame({'X': range(10, 15), 'Y': range(15, 20)})
# dataframes = [df1, df2]

# create_seaborn_chart_from_dataframe(df1, 'df1_image.png')
# create_seaborn_chart_from_dataframe(df2, 'df2_image.png')

# chart_paths = ['df1_image.png', 'df2_image.png']

# create_pdf_from_data_and_charts(dataframes, chart_paths, 'report.pdf')
