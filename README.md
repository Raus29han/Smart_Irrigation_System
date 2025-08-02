# 🌿 Smart Irrigation System using Machine Learning

An intelligent, sensor-driven irrigation automation system that uses machine learning to predict sprinkler activation across 20 zones. Designed for efficiency, water conservation, and real-time control, the project integrates a trained ML model with an interactive Streamlit dashboard and historical logging system.

---
## ✅ Features

- 💧 Predicts sprinkler ON/OFF status based on sensor input
- 📊 Dashboard with real-time input controls and visual analytics
- 🧠 Machine learning model trained on 20-sensor datasets
- ⏱️ Logs historical activations with timestamp
- 📤 CSV export for analysis and auditing
- 🧩 Modular design ready for hardware integration

---

## 🎯 Problem Statement

Traditional irrigation systems are inefficient—relying on fixed schedules rather than actual soil conditions—leading to water wastage, poor crop health, and high labor costs.

> The challenge: How can we create an adaptive, intelligent irrigation system that responds to real-time soil data?

---

## 💡 Solution

A smart irrigation dashboard that:
- Collects data from 20 virtual soil sensors.
- Uses a trained **MultiOutputClassifier** to predict the ON/OFF status of sprinklers.
- Displays predictions and historical trends in an intuitive UI built with **Streamlit**.
- Logs every decision for transparency and optimization.

---

## 🧠 Methodology

1. **Data Collection & Preprocessing**
   - Normalized sensor values between 0–1.
   - Used labeled CSV (`irrigation_machine.csv`) for supervised learning.

2. **Model Training**
   - Trained a multi-output classifier using scikit-learn.
   - Exported the model as `Farm_Irrigation_System.pkl`.

3. **Web App Development**
   - Built a real-time dashboard using Streamlit.
   - Created sliders for input, and charts for visual feedback.

4. **Prediction & Logging**
   - Predictions are generated live, displayed with parcel-wise status.
   - Logs are saved in `prediction_history.csv`.

5. **Historical Analytics**
   - Line charts visualize past sprinkler activations.
   - CSV download option allows external analysis.

---

## 🛠 Tech Stack

| Category             | Tools & Technologies                            |
|----------------------|--------------------------------------------------|
| **Language**         | Python 3.x                                       |
| **Machine Learning** | scikit-learn, MultiOutputClassifier, joblib      |
| **Web Framework**    | Streamlit                                        |
| **Data Handling**    | pandas, numpy                                    |
| **Visualization**    | Streamlit Charts (line chart, bar chart)         |
| **Data Storage**     | CSV files (`irrigation_machine.csv`, `prediction_history.csv`) |
| **Model Deployment** | Joblib for model serialization and loading       |
| **Dev Tools**        | Jupyter Notebook, VS Code                        |
| **System Utilities** | os, datetime                                     |

---

## 🧱 System Architecture

```text
[ Sensor Input (20 features) ] 
        ⬇
[ Trained ML Model (.pkl) ]
        ⬇
[ Streamlit Dashboard UI ]
        ⬇
[ Sprinkler ON/OFF Prediction ]
        ⬇
[ Logging + Visualization ]

```

## ▶️ How to Run

Clone the project

```bash
  git clone https://github.com/yourusername/smart-irrigation-system.git
```

Go to the project directory

```bash
  cd smart-irrigation-system
```

Install dependencies

```bash
  pip install pandas matplotlib seaborn scikit-learn joblib streamlit 
```

Run streamlit web front-end

```bash
  streamlit run app.py
```


## 🖼 Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## 🔮 Future Enhancements


- Predictive analytics for long-term planning

- Plant health monitoring via Pi Camera and OpenCV

- Voice command integration with Alexa or Google Assistant

- Fault detection with real-time alert system


## 👨‍💻 Authors

- Raushan Kumar
- B.Tech CSE | Uttaranchal University
- LinkedIn: [https://www.linkedin.com/in/raushan-kumar-702036305/]

