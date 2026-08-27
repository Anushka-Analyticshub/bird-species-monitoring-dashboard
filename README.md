# 🐦 Bird Species Monitoring and Biodiversity Analysis Dashboard

An interactive data analytics dashboard developed to explore and analyze bird species monitoring observations, biodiversity patterns, monitoring locations, environmental conditions, and observation methods.

The project was developed as part of an internship project using Python, Pandas, Plotly, and Streamlit.

---

## 👩‍💻 Project Author

**Anushka Gupta**

BBA (Hons.) – Business Analytics and Intelligence

---

## 📌 Project Overview

The **Bird Species Monitoring and Biodiversity Analysis Dashboard** provides an interactive interface for exploring a cleaned bird monitoring dataset.

The dashboard allows users to examine:

- Bird species diversity
- Species observation frequency
- Monitoring sites and plots
- Environmental conditions
- Monitoring methods
- Observer activity
- Observation distance
- Flyover observations
- Initial three-minute count records
- Filtered bird monitoring records

The project demonstrates the application of **data cleaning, exploratory data analysis, data visualization, and interactive dashboard development**.

---

## 🎯 Objectives

The main objectives of the project are:

1. To organize and analyze bird monitoring observations.
2. To identify patterns in bird species observations.
3. To examine species richness across monitoring locations.
4. To explore environmental conditions recorded during monitoring.
5. To analyze different monitoring and identification methods.
6. To provide an interactive dashboard for data exploration.
7. To enable users to filter and download relevant monitoring records.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and data analysis |
| Pandas | Data processing and analysis |
| Plotly | Interactive data visualization |
| Streamlit | Interactive dashboard development |
| GitHub | Source code and project version control |

---

## 📊 Dashboard Sections

### 1. 📊 Overview

Provides a high-level summary of the monitoring dataset, including:

- Total observations
- Number of bird species
- Monitoring sites
- Monitoring plots
- Three-minute records
- Years covered
- Flyover records
- Monitoring period

It also includes visualizations for:

- Most frequently observed species
- Monitoring site comparison
- Total observations by site
- Unique species by site

---

### 2. 🐦 Species Analysis

This section focuses on bird species-level analysis.

It provides:

- Species summary
- Scientific names
- Total observations
- Initial three-minute records
- Three-minute observation percentage
- Top 10 observed species
- Initial three-minute count visualization

---

### 3. 🌲 Location & Habitat Analysis

This section explores observations across monitoring locations.

It includes:

- Monitoring site summaries
- Total observations by site
- Unique species by site
- Monitoring plot summaries
- Species richness by monitoring plot

---

### 4. 🌤️ Environmental Analysis

This section examines environmental conditions recorded during monitoring.

It includes:

- Average temperature
- Temperature range
- Average humidity
- Humidity range
- Most common disturbance
- Sky conditions
- Wind conditions
- Temperature distribution

---

### 5. 🔎 Monitoring Analysis

This section examines how observations were recorded.

It includes:

- Identification methods
- Observations by visit
- Observations by observer
- Observation distance
- Flyover observations

---

### 6. 📋 Data Explorer

The Data Explorer allows users to interactively examine the cleaned dataset.

Users can filter records by:

- Monitoring Site
- Bird Species
- Identification Method

The filtered dataset can also be downloaded as a CSV file.

---

## 📁 Project Structure

```text
bird-species-monitoring-dashboard/
│
├── app.py
│
├── requirements.txt
│
├── output/
│   └── cleaned_bird_data.csv
│
└── .devcontainer/
