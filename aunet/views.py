# -*-coding:utf-8 -*-
from flask import render_template

from aunet import app

@app.route('/Developing')
def develop_next():
	return render_template('Public/fixed.html')
