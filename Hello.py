# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create a simple Streamlit app
def main():
    st.set_page_config(
        page_title="Dynamic Dashboard",
        page_icon="👋",
    )
    # Set the title of the app
    st.title("Welcome to home page!!")
    st.image("logo.png", caption="Streamlit Logo", use_column_width=True)


    # Create a sidebar with options
    option = st.sidebar.selectbox(
        'Select an option',
        ('Home', 'Data Exploration', 'About')
    )

    # Home Page
    if option == 'Home':
        st.write('Welcome to the Home Page!')

    # Data Exploration Page
    elif option == 'Data Exploration':
        st.subheader('Explore your data here:')
        uploaded_file = st.file_uploader("Please upload the csv file.", type="csv")

        if uploaded_file is not None:
            exp=st.sidebar.selectbox('Select the exploration method:',('Chart','Graph','Summary'))
            # Read the data from the uploaded CSV file
            df = pd.read_csv(uploaded_file)
            
            if exp == 'Chart':
                chart_type = st.selectbox("Select Chart Type:", ["Line Chart", "Scatter Plot", "Bar Chart"])

                x_column = st.selectbox("Select X Column:", df.columns)
                y_column = st.selectbox("Select Y Column:", df.columns)

                # Animator for animation_frame (useful for time-based data)
                animator_column = st.selectbox("Select Animator (Animation Frame):", [None] + df.columns.tolist())

                if animator_column:
                    # Sort DataFrame by the animator column
                    df_sorted = df.sort_values(by=animator_column)

                    # Create animated chart using Plotly Express
                    if chart_type == "Line Chart":
                        fig = px.line(df_sorted, x=x_column, y=y_column, animation_frame=animator_column,
                                    labels={x_column: x_column, y_column: y_column, 'animation_frame': animator_column})
                    elif chart_type == "Scatter Plot":
                        fig = px.scatter(df_sorted, x=x_column, y=y_column, animation_frame=animator_column,
                                        labels={x_column: x_column, y_column: y_column, 'animation_frame': animator_column})
                    elif chart_type == "Bar Chart":
                        fig = px.bar(df_sorted, x=x_column, y=y_column, animation_frame=animator_column,
                                    labels={x_column: x_column, y_column: y_column, 'animation_frame': animator_column})
                else:
                    # Create non-animated chart
                    if chart_type == "Line Chart":
                        fig = px.line(df, x=x_column, y=y_column, labels={x_column: x_column, y_column: y_column})
                    elif chart_type == "Scatter Plot":
                        fig = px.scatter(df, x=x_column, y=y_column, labels={x_column: x_column, y_column: y_column})
                    elif chart_type == "Bar Chart":
                        fig = px.bar(df, x=x_column, y=y_column, labels={x_column: x_column, y_column: y_column})

                # Show the chart in Streamlit
                st.plotly_chart(fig)
        
            elif exp=='Graph':
                Graph_type = st.selectbox("Select Chart Type:", ["Bar Graph", "Violin Plot", "Bubble Plot"])

                x_column = st.selectbox("Select X Column:", df.columns)
                y_column = st.selectbox("Select Y Column:", df.columns)

                # Animator for animation_frame (useful for time-based data)
                animator_column = st.selectbox("Select Animator (Animation Frame):", df.columns.tolist())
                df_sorted = df.sort_values(by=animator_column)

                if Graph_type == "Bar Graph":
                    # Create a moving bar graph based on user-selected axes and animator
                    fig = px.bar(df_sorted, x=x_column, y=y_column, color=x_column,
                                                animation_frame=animator_column,
                                                title=f"Moving Bar Graph: {y_column} by {x_column} (Animated by {animator_column})",
                                                labels={x_column: x_column, y_column: y_column, animator_column: animator_column})

                    # Show the moving bar graph in Streamlit
                    st.plotly_chart(fig)
                        
                elif Graph_type == 'Violin Plot':
                    # Create animated violin plot
                    fig= px.violin(df_sorted, x=x_column, y=y_column,
                                                    animation_frame=animator_column,
                                                    title=f'Violin Plot of {y_column} for Different {x_column}s (Animated by {animator_column})',
                                                    labels={x_column: x_column, y_column: y_column})

                    # Show the animated violin plot in Streamlit
                    st.plotly_chart(fig)


                elif Graph_type == 'Bubble Plot':

                    # Creating the animated bubble plot
                    fig = px.scatter(df_sorted, x=x_column, y=y_column,
                                    animation_frame=animator_column,
                                    title=f"{x_column} vs {y_column} (Animated by {animator_column})",
                                    labels={x_column: x_column, y_column: y_column},
                                    log_x=False)

                    # Updating layout with play/pause buttons
                    fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                                        buttons=[dict(label='Play',
                                                                    method='animate',
                                                                    args=[None, dict(frame=dict(duration=1000, redraw=True),
                                                                                    fromcurrent=True)]),
                                                                dict(label='Pause',
                                                                    method='animate',
                                                                    args=[[None], dict(frame=dict(duration=300, redraw=True),
                                                                                        mode='immediate',
                                                                                        transition=dict(duration=100))])])],
                                    xaxis_title=x_column, yaxis_title=y_column,
                                    xaxis=dict(type='linear'), height=600)

                    # Show the animated bubble plot in Streamlit
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
