from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info_promo')
def info_promo(info_promo=None):
    info = pd.read_csv('../info_extract_data/info_extract.csv')
    return render_template('info_promo.html', info_promo = info)