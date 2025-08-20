# Autism Catatonia Treatment Effectiveness

The goal of this project is to find out how well different treatments work for autism-related catatonia and to identify which treatments are the most effective.

---

## About Catatonia and treatment type

Catatonia in autism is a serious condition where a person may slow down, freeze, or show repetitive movements. Treatment usually involves a mix of medications (like benzodiazepines or antipsychotics), and in some cases, ECT (electroconvulsive therapy) if symptoms are very severe.

---

## Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/Sahiladevi/Autism_Catatonia_Treatment_Effectiveness.git
```

### 2. Navigate to the cloned directory

Change your current directory to the cloned repository's directory (health_track)

```bash
cd Autism_Catatonia_Treatment_Effectiveness
```

### 3. Create Virtual Environment

On Windows:
```bash
python -m venv venv
```

On macOS and Linux:
```bash
python3 -m venv venv
```

This will create a new virtual environment named venv in your current directory

### 4. Activate Virtual Environment

On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```
Your prompt should change to indicate that you are now operating within a Python virtual environment.

### 5. Install Requirements

Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

**Note:** Make sure ipykernel is included in the requirements.txt file. If not, install it manually:

```bash
pip install ipykernel
```
### 6. Register the Environment as a Jupyter Kernel

```bash
python -m ipykernel install --user --name=venv --display-name "Python (health_track)"
```
This step lets you select this environment inside Jupyter.

### 7. Run Jupyter Notebook

```bash
jupyter notebook
```

### 8. To deactivate the virtual environment, after running the project

```bash
deactivate
```
---

## Requirements

Contents of `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn
plotly
jupyter
streamlit
Pillow

```

> Only the necessary libraries are included to keep things clean and lightweight. A virtual environment was used to avoid any conflicts and keep the setup isolated from the rest of the system. 

---

## Medication Treatment Analysis Dashboard
file name: autism_catatonia_medication.py
This Streamlit dashboard provides visual insights into patient data for medication treatments, including:

- Most common side effects
- Improvement by gender and side effect presence
- Age and treatment duration correlations
- Top 5 responders for each medication
- Interactive pre/post treatment score comparisons

---

##  How to Run the Streamlit App

### 1. Ensure dependencies are installed

Make sure your virtual environment is active and install the required packages if you haven’t already:

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit app

streamlit run autism_catatonia_treatment.py

### 3. View in browser

Streamlit will open the app automatically in your default web browser. If not, copy the URL from the terminal (usually http://localhost:8501) and paste it into your browser.

### 4. Stop the app

Press Ctrl + C in the terminal to stop the app when finished.

---

### Data visualization for Autism and catatonia treatment effectiveness 

file name: autism_catatonia_medication.ipynb