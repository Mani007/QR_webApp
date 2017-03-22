from flask import Flask, render_template, url_for
from app import *
import qrcode
import qrtools

img1 = qrcode.make('THE QR test')
img = img1.save("C:/Users/madhu/Documents/visualGIT/QR_webApp/test_QR_Code/static/images/myQR.png")

@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html') 

@app.route('/QR')
def qrcode():
    """Renders a sample page."""
    return render_template('sampleCoupon.html') 
