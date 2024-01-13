# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create a simple Streamlit app
def main():
    st.set_page_config(
        page_title="1st app",
        page_icon="👋",
    )
    # Set the title of the app
    st.title("Streamlit Example App")

    # Create a sidebar with options
    option = st.sidebar.selectbox(
        'Select an option',
        ('Home', 'Data Exploration', 'About')
    )

    # Home Page
    if option == 'Home':
        st.write('Welcome to the Home Page!')
        st.image("logo.png", caption="Streamlit Logo", use_column_width=True)

    # Data Exploration Page
    elif option == 'Data Exploration':
        st.subheader('Explore your data here:')
        uploaded_file = st.file_uploader("Please upload the csv file.", type="csv")

        if uploaded_file is not None:
            exp=st.sidebar.selectbox('Select the exploration method:',('Chart','Graph','Summary'))
            # Read the data from the uploaded CSV file
            df = pd.read_csv(uploaded_file)
            # Display the dataframe
            if exp=='Chart':
                try:
                  # Show the DataFrame
                  st.subheader("DataFrame Preview:")
                  st.write(df)

                  # Allow user to choose X and Y columns
                  x_column = st.selectbox("Select X Column:", df.columns)
                  y_column = st.selectbox("Select Y Column:", df.columns)

                  # Plot the chart
                  chart_type = st.selectbox("Select Chart Type:", ["Line Chart", "Scatter Plot", "Bar Chart"])
                  
                  if chart_type == "Line Chart":
                      st.line_chart(df[[x_column, y_column]])
                  elif chart_type == "Scatter Plot":
                      st.scatter_chart(df[[x_column, y_column]])
                  elif chart_type == "Bar Chart":
                      st.bar_chart(df[[x_column, y_column]])

                except Exception as e:
                  st.error(f"An error occurred: {e}")
            
            elif exp=='Graph':
              st.subheader("Raw Data")
              st.write(df)

              # Choose a column for the graph
              selected_row = st.selectbox("Select a row for the graph", df.columns)
              selected_column = st.selectbox("Select a column for the graph", df.columns)

              # Create a graph using Plotly Express
              fig = px.line(df, x=selected_row, y=selected_column, title=f"{selected_column} over time with respect to {selected_row}")
              st.plotly_chart(fig)

            elif exp=='Summary':
              st.dataframe(df)
              # Display summary statistics
              st.write('Summary Statistics:')
              st.write(df.describe())

    # About Page
    elif option == 'About':
        st.write('This is a simple Streamlit app created as an example.')

# Run the app
if __name__ == "__main__":
    main()
