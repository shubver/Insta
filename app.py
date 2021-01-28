import os
from flask import redirect, send_from_directory, url_for
import pandas as pd
from dtale.app import build_app
from dtale.views import startup
from flask import Flask, render_template, request
import business_discovery_new


additional_templates = os.path.join(os.path.dirname(__file__), "templates")
app = build_app(reaper_on=False, additional_templates=additional_templates)
# app = Flask(__name__)

CUSTOM_STATIC_PATH=app.root_path + '/static/'

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['CUSTOM_STATIC_PATH'], filename)

@app.route("/")
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_username():
    if request.method == 'POST':
        f = request.files['file']
    username_df = pd.read_csv(f, header=None)
    data = business_discovery_new.return_business_discovery(list(username_df.values.flatten()))
    instance = startup(data_id="1",data=data, ignore_duplicate=True)
    return redirect(f"/dtale/main/{instance._data_id}", code=302)

@app.route('/uploader2', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
    data = pd.read_csv(f)
    # data = business_discovery_new.return_business_discovery(list(username_df.values.flatten()))
    instance = startup(data_id="1",data=data, ignore_duplicate=True)
    return redirect(f"/dtale/main/{instance._data_id}", code=302)
    

@app.route("/create-df")
def create_df(data):
    # cleanup("1")
    instance = startup(data_id="1",data=data, ignore_duplicate=True)
    return redirect(f"/dtale/main/{instance._data_id}", code=302)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
