#import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

data = {'Nama Rumah Sakit' : ['RS A', 'RS B', 'RS C'], 
        'Jenis Rumah Sakit': ['RS',  'RSIA', 'RSJ'],
        'Alamat': ['Jalan-jalan', 'Jalan kayang','Jalangkote']}

@app.route('/')
def index():
    results_df = data.to_dict(orient='records')
    return render_template('index.html', results=results_df)

