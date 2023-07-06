import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def main():
    st.title("Solar and Wind Generation Data Analysis")
    
    # Load the data
    df = pd.read_csv("Generation Forecasts for Wind and Solar_202307040000-202307050000 (1).csv", index_col="MTU (CET/CEST)", parse_dates=True)
    
    
    # Display the DataFrame
    st.subheader("Data")
    st.dataframe(df.head(10))
    
    # Display DataFrame information
    st.subheader("Data Information")
    st.write(df.info())
    
    # Sidebar for selecting column
    selected_column = st.sidebar.selectbox("Select Column", df.columns)
    # Create the initial line plot
    fig = px.line(df, x=df.index, y="Generation - Solar  [MW] Day Ahead/ BZN|BE")
    
    # Add additional traces for other variables
    fig.add_trace(px.line(df, x=df.index, y="Generation - Solar  [MW] Intraday / BZN|BE", color_discrete_sequence=["red"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Solar  [MW] Current / BZN|BE", color_discrete_sequence=["blue"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Offshore  [MW] Day Ahead/ BZN|BE", color_discrete_sequence=["green"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Offshore  [MW] Intraday / BZN|BE", color_discrete_sequence=["brown"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Offshore  [MW] Current / BZN|BE", color_discrete_sequence=["purple"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Onshore  [MW] Day Ahead/ BZN|BE", color_discrete_sequence=["pink"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Onshore  [MW] Intraday / BZN|BE", color_discrete_sequence=["gray"]).data[0])
    fig.add_trace(px.line(df, x=df.index, y="Generation - Wind Onshore  [MW] Current / BZN|BE", color_discrete_sequence=["blue"]).data[0])
    fig.update_layout(height=600, width=800)
    
    # Display the line plot
    st.subheader("The Line plots of All the variables shown in the figure")
    st.plotly_chart(fig)
    # Create the scatter plot for Solar vs. Intraday Wind and currect
    scatter_fig1 = px.scatter(df, x="Generation - Solar  [MW] Day Ahead/ BZN|BE", y="Generation - Solar  [MW] Intraday / BZN|BE", color="Generation - Solar  [MW] Current / BZN|BE")
    scatter_fig1.update_traces(marker=dict(size=8))  # Change marker size
    scatter_fig1.update_layout(title="Scatter Plot: Solar vs. Intraday Wind", xaxis_title="Generation - Solar  [MW] Day Ahead/ BZN|BE", yaxis_title="Generation - Solar  [MW] Intraday / BZN|BE")
    
    # Display the scatter plot
    st.subheader("Scatter Plot: Solar vs. day ahead Wind")
    st.plotly_chart(scatter_fig1)
 #Create the scatter plot for Solar vs. Intraday Wind and currect
    scatter_fig2 = px.scatter(df, x="Generation - Wind Offshore  [MW] Day Ahead/ BZN|BE", y="Generation - Wind Offshore  [MW] Intraday / BZN|BE", color="Generation - Wind Offshore  [MW] Current / BZN|BE")
    scatter_fig2.update_traces(marker=dict(size=8))  # Change marker size
    scatter_fig2.update_layout(title="Scatter Plot: Wind Offshore vs. Intraday Wind", xaxis_title="Generation - Solar  [MW] Day Ahead/ BZN|BE", yaxis_title="Generation - Wind Offshore  [MW] Day Ahead/ BZN|BE")
    
    # Display the scatter plot
    st.subheader("Scatter Plot: Wind Offshore vs. Intraday Wind and Wind Offshore  [MW] Current")
    st.plotly_chart(scatter_fig2)

# Create the scatter plot for Solar vs. Intraday Wind and currect
    scatter_fig3 = px.scatter(df, x="Generation - Wind Onshore  [MW] Day Ahead/ BZN|BE", y="Generation - Wind Onshore  [MW] Intraday / BZN|BE", color="Generation - Wind Onshore  [MW] Current / BZN|BE")
    scatter_fig3.update_traces(marker=dict(size=8))  # Change marker size
    scatter_fig3.update_layout(title="Scatter Plot: Wind vs. Intraday Wind", xaxis_title="Wind Onshore  [MW] Day Ahead/ BZN|BE", yaxis_title="Wind Onshore  [MW] Intraday / BZN|BEE")
    
    # Display the scatter plot
    st.subheader("Scatter Plot: Wind Onshore  [MW] Day Ahead vs. Wind Onshore  [MW] Intraday and Wind Onshore  [MW] Current")
    st.plotly_chart(scatter_fig3)
    
    # Create the initial line plot
    fig = px.line(df, x=df.index, y=selected_column)
    fig.update_layout(height=600, width=800)
    
    # Display the line plot
    st.subheader("Line Plot")
    st.plotly_chart(fig)
    
    # Create the scatter plot for Solar vs. Intraday Wind and Current
    scatter_fig = px.scatter(df, x="Generation - Solar  [MW] Day Ahead/ BZN|BE", y=selected_column, color="Generation - Solar  [MW] Current / BZN|BE")
    scatter_fig.update_traces(marker=dict(size=8))  # Change marker size
    scatter_fig.update_layout(title="Scatter Plot: Solar vs. " + selected_column, xaxis_title="Generation - Solar  [MW] Day Ahead/ BZN|BE", yaxis_title=selected_column)
    
    # Display the scatter plot
    st.subheader("Scatter Plot: Solar vs. " + selected_column)
    st.plotly_chart(scatter_fig)

    # Calculate the correlation coefficients
    correlation = df["Generation - Solar  [MW] Day Ahead/ BZN|BE"].corr(df[selected_column])

    # Display the correlation coefficients
    st.subheader("Correlation Coefficient")
    st.write("Correlation between Solar and " + selected_column + ":", correlation)

if __name__ == "__main__":
    main()
