#import pandas as pd
from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

df = pd.DataFrame('rumahsakit_medicalclinicid_cleaned.csv')

@app.route('/')
def index():
    results_df = df.to_dict(orient='records')
    return render_template('index.html', results=results_df)

