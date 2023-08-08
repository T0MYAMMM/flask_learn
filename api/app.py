import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

data = pd.read_csv('rumahsakit_medicalclinicid_cleaned.csv')

@app.route('/')
def home_dashboard():
    results_df = data.to_dict(orient='records')
    return render_template('index.html', results=results_df)

