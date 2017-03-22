# QR_webApp
Qr code Application using Flask Framework in Python.

My setup environment:
I am using visual studio 2015 (VS2015) community edition along with python tools.

Required packages
virtualenv
Flask
pillow
qrcodes
qrtools

Steps for setup:
I. setup virtual environment (optional but recomended)
II. clone https://github.com/Mani007/QR_webApp.git
III. pip install virtualenv, Flask, pillow, qrcodes, qrtools
VI. If you are not using VS2015 then make the following line as comment in app.py
wsgi_app = app.wsgi_app
import os
  HOST = os.environ.get('SERVER_HOST', 'localhost')
  try:
     PORT = int(os.environ.get('SERVER_PORT', '5555'))
  except ValueError:
     PORT = 5555
  app.run(HOST, PORT)
AND the following line in if __name__ == '__main__':
app.run()
V. on the command prompt go to the current working directory location (this line in not required in VS2015)
VI. activate the virtual environment (this line in not required in VS2015)
VII. run python app.py (this line in not required in VS2015)
VIII. In VS2015 - don't follow instruction 4,5,6,7 insted directly run the project into default selected browser.
IX. If the code did not run in VS2015 then just refresh the browser
That all
