# 🌱 Adaptive Systems: Real-Time Crop Health Monitoring for Urban Farming

---

## 📋 Overview
Urban farming is gaining popularity, but maintaining optimal crop health in a city environment can be tricky. Factors like fluctuating temperatures, inconsistent sunlight, and varying soil moisture levels can impact plant growth. In this challenge, you'll develop a **data-driven monitoring system** that tracks key environmental variables and alerts farmers when conditions might stress the crops.

---

## 🌍 Scenario
You’ve partnered with an urban farming collective in Southern California that maintains rooftop gardens. The collective needs a **real-time monitoring system** to track crop health indicators, helping farmers respond promptly to potential issues. Your task is to build a system that **collects data**, **analyzes trends**, and **notifies farmers** when conditions are likely to cause stress or poor growth.

The goal? To make data-driven decisions without relying on fully autonomous AI. This project will use **data analytics and basic machine learning models** to interpret environmental changes.

---

## 📝 Problem Tasks

### ⚙️ Task 1: Setting Up Data Collection
Build a system to collect environmental data and track crop health metrics.

**Sub-tasks:**
- 🌡️ Set up simulated sensors to collect temperature, humidity, and soil moisture data.
- 💡 Integrate light intensity readings to monitor sunlight exposure.
- 📊 Store the data in a structured format (e.g., CSV or SQLite).

**Expected Outcome:**
- A reliable data collection pipeline that continuously logs key metrics.

---

### 🔬 Task 2: Data Analysis and Trend Detection
Identify patterns and anomalies that could affect crop health.

**Sub-tasks:**
- 📈 Perform exploratory data analysis (EDA) to understand the range and variability of collected metrics.
- 🔍 Implement a simple anomaly detection algorithm to flag unusual readings (e.g., sudden drops in moisture).
- 📝 Generate summary statistics and visualizations of the data.

**Expected Outcome:**
- A script that identifies and highlights potential stress indicators based on collected data.

---

### 🔧 Task 3: Building a Notification System
Alert the farmers when conditions deviate from optimal ranges.

**Sub-tasks:**
- 🚨 Set threshold values for temperature, moisture, and light based on optimal crop conditions.
- 💬 Implement a notification system that triggers alerts (console messages or emails) when conditions go out of range.
- 🔄 Allow customization of threshold values for different crops.

**Expected Outcome:**
- An alert system that informs farmers when environmental conditions become unfavorable.

---

### 🖊️ Task 4: Visualizing Real-Time Data
Make it easy to see the current state of the crops and potential issues.

**Sub-tasks:**
- 📊 Use **Matplotlib** to create real-time plots of environmental data.
- 🌱 Display trend lines to show how conditions change over time.
- 🚥 Use colored indicators (e.g., green for optimal, red for problematic) to visualize crop health.

**Expected Outcome:**
- An interactive dashboard that displays real-time and historical data with clear visual cues.

---

## 📦 Deliverables
- **💻 Code Implementation:**
  - Python scripts for data collection, trend analysis, and notifications.

- **📊 Analysis Report:**
  - Documentation of data analysis methods, anomaly detection logic, and visualization techniques.

- **🖼️ Visual Demonstration:**
  - A video or demo showing the system detecting changes and alerting farmers.

---

## 🎁 Bonus Section
1. **🔄 Dynamic Threshold Adjustment**
   - Automatically update thresholds based on historical data trends.

2. **📱 Mobile Notification System**
   - Integrate a simple SMS or app-based alert system.

3. **🧠 Machine Learning Enhancement**
   - Use a lightweight regression model to predict crop stress based on collected data.

4. **🌐 Web-Based Dashboard**
   - Create a Flask app to display real-time data from any device.

5. **📊 Advanced Data Visualization**
   - Include correlation plots between environmental variables to identify interconnected factors.

---

## 🏅 Bonus Section Deliverables
- **🔄 Dynamic Threshold Demo:**
  - Demonstrate adaptive alerting as conditions change.

- **📱 Mobile App Prototype:**
  - Real-time notifications displayed on a smartphone.

- **🧠 ML-Driven Prediction Report:**
  - Show how predictions improve alert accuracy.

- **🌐 Web Dashboard Demo:**
  - A web-based interface showing crop conditions in real time.

- **📊 Correlation Analysis:**
  - Plot showing relationships between variables (e.g., temperature and moisture).

---

## 📚 Resources

- **🔗 [Pandas for Data Handling](https://pandas.pydata.org/)**

- **🔗 [Matplotlib for Visualization](https://matplotlib.org/)**

- **🔗 [Scikit-learn for Anomaly Detection](https://scikit-learn.org/)**

- **🔗 [Flask for Web App Development](https://flask.palletsprojects.com/)**

- **🔗 [Twilio API for SMS Alerts](https://www.twilio.com/)**

---
