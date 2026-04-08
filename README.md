# ⚡ Energy Consumption Prediction

An end-to-end Machine Learning project that forecasts household energy usage using time-series features derived from historical consumption data. This project demonstrates the complete pipeline from data preprocessing and model development to deployment as an interactive web application.

---

## 🚀 Project Overview

This application predicts future energy consumption based on the last three days of usage. It leverages time-based feature engineering to capture consumption patterns and provides real-time predictions through a user-friendly interface.

---

## 🧠 Key Features

- Time-series feature engineering using lag values and rolling averages  
- Model comparison using Linear Regression, Random Forest, and XGBoost  
- Best model selection based on performance (R² ≈ 0.84)  
- Interactive web application built with Streamlit  
- Real-time predictions with simple trend insights (increase/decrease)

---

## 📊 Dataset

- London Household Energy Consumption Dataset  
- Source: Kaggle  
- Link: https://www.kaggle.com/datasets/emmanuelfwerr/london-homes-energy-data  

---

## ⚙️ Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- pandas  
- numpy  
- joblib  

---

## 📁 Project Structure

```
energy-consumption-prediction-ml/
│
├── streamlit_app.py          # Main application
├── energy_model.pkl          # Trained ML model
├── requirements.txt          # Project dependencies
├── energy_consumption_model_training.ipynb   # Model development notebook
```

---

## ▶️ How to Run Locally

1. Clone the repository:
```
git clone https://github.com/Koushiksundarbabu/energy-consumption-prediction-ml.git
```

2. Navigate to the project folder:
```
cd energy-consumption-prediction-ml
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
streamlit run streamlit_app.py
```

---

## 🌍 Live Demo

👉 https://energy-consumption-prediction-ml-koushik.streamlit.app

---

## 💡 Key Learnings

- Importance of feature engineering in time-series problems  
- Simpler models can outperform complex ones with well-designed features  
- End-to-end ML workflow from model development to deployment  
- Building user-friendly ML applications for real-world usage  

---

## 🔮 Future Improvements

- Incorporate external factors like weather data  
- Add long-term forecasting capabilities  
- Store historical user inputs for automated predictions  
- Enhance UI with visualizations and analytics  

---

## 📌 Conclusion

This project demonstrates how machine learning models can be transformed into practical, user-facing applications by combining data science with deployment and user experience design.

---

## 🤝 Connect

If you have any feedback or suggestions, feel free to connect or reach out.
