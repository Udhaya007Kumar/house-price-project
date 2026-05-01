# 🏠 House Price Predictor (Machine Learning Project)

This project predicts house prices using a Machine Learning model built with **Linear Regression**.

---

## 📌 Project Overview

The goal of this project is to estimate house prices based on key features like:

* Size of the house (sqft)
* Age of the house (years)
* Distance from city center (km)

This is a complete **end-to-end ML project** including:

* Data analysis
* Model building
* Evaluation
* User input prediction
* Web app using Streamlit

---

## 🚀 Model Performance

| Metric   | Value  |
| -------- | ------ |
| RMSE     | ~6277  |
| R² Score | ~0.998 |

👉 The model achieves **~98%+ accuracy**, which is excellent.

---

## 🔍 Key Insights

* 📈 Price increases with **house size**
* 📉 Price decreases as **house age increases**
* 📉 Price decreases as **distance from city center increases**

---

## 🧠 Machine Learning Concepts Used

* Linear Regression
* Feature Selection
* Correlation Analysis
* Train/Test Split
* Model Evaluation (RMSE, R²)
* Prediction using user input

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* scikit-learn
* Matplotlib
* Streamlit

---

## 📂 Project Structure

```
house-price-predictor/
│
├── app.py              # Streamlit app
├── model.pkl           # Trained ML model
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

---

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Run the app

```bash
streamlit run app.py
```

👉 App will open in your browser 🎉

---

## 🧪 Example Prediction

### Input:

* Size: 1500 sqft
* Age: 5 years
* Distance: 10 km

### Output:

```
Predicted Price: ₹260,925
```

---

## 📊 Sample Test Cases

| Size | Age | Distance | Prediction      |
| ---- | --- | -------- | --------------- |
| 800  | 10  | 15       | Low price       |
| 1500 | 5   | 10       | Medium price    |
| 2500 | 3   | 2        | High price      |
| 2500 | 3   | 20       | Reduced price   |
| 1500 | 20  | 5        | Slight decrease |

---

## 🌟 Features

* Simple and clean ML model
* User input prediction
* Real-time web interface (Streamlit)
* Lightweight and fast

---

## 📌 Future Improvements

* Add more features (location, floor, amenities)
* Try advanced models (Random Forest, XGBoost)
* Deploy app online (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Udhayakumar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
