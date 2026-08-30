# House Price Prediction Project

This project demonstrates a complete data science pipeline for predicting house prices using regression techniques.

## Project Structure

- `main.py`: Main script that runs the entire pipeline
- `requirements.txt`: List of Python dependencies
- `data/`: Directory for storing datasets (not included in repo)
- `models/`: Directory for saving trained models (not included in repo)
- `notebooks/`: Directory for exploratory data analysis (not included in repo)

## Setup Instructions

1. Clone the repository
2. Navigate to the project directory:
   ```bash
   cd solutions/project_1_house_price_prediction
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the main script:
   ```bash
   python main.py
   ```

## Pipeline Overview

1. **Data Loading**: Load house price dataset (sample data generated if file not found)
2. **Exploratory Data Analysis**: Basic statistics and visualizations
3. **Data Preprocessing**: Handle missing values, encode categorical variables, scale features
4. **Model Training**: Train multiple regression models (Linear Regression, Random Forest, Gradient Boosting)
5. **Model Evaluation**: Compare models using RMSE and R-squared metrics
6. **Model Persistence**: Save the best model for future use
7. **Prediction**: Example of making predictions on new data

## Dependencies

See `requirements.txt` for the list of required packages.

## Customization

- To use your own dataset, place a CSV file named `house_prices.csv` in the `data/` directory
- Modify the feature engineering steps in `main.py` as needed
- Experiment with different models and hyperparameters

## License

This project is for educational purposes.