# Restaurant Location-Based Analysis Dashboard

This project is a powerful, interactive web application built with **Streamlit** designed to perform geospatial and statistical analysis on restaurant datasets. It enables users to visualize restaurant locations on an interactive map, analyze market concentration, and generate automated business insights based on city or locality.

---

# 🚀 Features

* Geospatial Visualization: Automatically plots all restaurants on an interactive map using latitude and longitude coordinates.
* Market Concentration Analysis: View the top 10 cities or localities by restaurant count using dynamic bar charts.
* Statistical Breakdown: A comprehensive data table showing:
* Total restaurant count per area.
* Average customer ratings.
* Average price range levels.
* The most common cuisine type per area.


* Automated Business Intelligence: Generates actionable insights, including market saturation, top-rated areas, and premium dining zones based on your uploaded data.

---

# 🛠️ Prerequisites

To run this application, you will need to have **Python** installed on your system. You will also need the following libraries:

```bash
pip install streamlit pandas

```

---

# 📂 Data Requirements

The application expects a CSV file (`Dataset.csv`) with the following headers:

* `Restaurant Name`
* `Latitude`
* `Longitude`
* `City`
* `Locality`
* `Cuisines`
* `Aggregate rating`
* `Price range`

---
# 🏃‍♂️ How to Run

1. **Clone or save** the code file as `app.py`.
2. **Open your terminal** or command prompt.
3. **Navigate** to the folder where you saved the file.
4. **Run the application** using the following command:

```bash
streamlit run app.py

```

5. Interact: Once the browser opens, use the sidebar to upload your `Dataset.csv` file to begin the analysis.

---

# 💡 How It Works

The application processes your data in three main stages:

* **Preprocessing:** Automatically cleans the dataset by removing entries with missing or invalid coordinates.
* **Mapping:** Uses `st.map` to render an interactive map based on your geographical data.
* **Aggregation:** Utilizes `pandas` to group data by area, calculate averages, and derive insights regarding market trends and quality metrics.
