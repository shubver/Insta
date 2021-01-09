import os
from flask import redirect
import pandas as pd
from dtale.app import build_app
from dtale.views import startup
from flask import Flask, render_template, request
import business_discovery_new

if __name__ == '__main__':
    additional_templates = os.path.join(os.path.dirname(__file__), "templates")
    app = build_app(reaper_on=False, additional_templates=additional_templates)
    # app = Flask(__name__)

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

    app.run(host="0.0.0.0", port=5000, debug=True)
    