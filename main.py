import streamlit as st
import pandas as pd
from preprocessing import load_data, clean_data, transform_data
from visualization import plot_data, display_statistics

def main():
    st.title("Data Dashboard Web Application")

    # File uploader for dataset
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
    
    if uploaded_file is not None:
        # Load and preprocess the data
        data = load_data(uploaded_file)
        cleaned_data = clean_data(data)
        transformed_data = transform_data(cleaned_data)

        # Display the data
        st.subheader("Data Preview")
        st.write(transformed_data)

        # Display statistics
        st.subheader("Summary Statistics")
        display_statistics(transformed_data)

        # Visualization
        st.subheader("Data Visualization")
        plot_data(transformed_data)

if __name__ == "__main__":
    main()