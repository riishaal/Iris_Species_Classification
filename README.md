# Iris Species Classification

This repository contains a complete end-to-end Machine Learning project that classifies Iris flower species using the famous Iris dataset. The project includes data exploration, model training, and a web-based interactive application built with Streamlit.

## Project Structure

- **`Iris.csv` / `Iris.zip`**: The dataset used for training the model, containing features like sepal length, sepal width, petal length, and petal width.
- **`iris.ipynb`**: A Jupyter Notebook detailing the data loading, exploratory data analysis (EDA), preprocessing, and model training processes.
- **`iris.pkl`**: The trained Machine Learning model serialized as a pickle file for deployment.
- **`stream_iris.py`**: A Streamlit application that provides a user interface to interact with the trained model and predict Iris species based on user input.

## How to Run the App Locally

To run the Streamlit app on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/riishaal/Iris_Species_Classification.git
   cd Iris_Species_Classification
   ```

2. **Install the required libraries:**
   (Ensure you have `streamlit`, `pandas`, and `scikit-learn` installed)
   ```bash
   pip install streamlit pandas scikit-learn
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run stream_iris.py
   ```

## Model
The notebook explores the data and trains a model (saved as `iris.pkl`) to accurately classify the three Iris species: Setosa, Versicolor, and Virginica based on petal and sepal measurements.
