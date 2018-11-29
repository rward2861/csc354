from flask import Flask, render_template, url_for, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
application = Flask(__name__)

photos = UploadSet('photos', IMAGES)

application.config['UPLOADED_PHOTOS_DEST'] = './training-data/s4'
configure_uploads(application, photos)

@application.route('/')
def profile():
  return render_template("profile.html")
  
  
@application.route('/dashboard')
def dashboard():
  return render_template("dashboard.html")
  
@application.route('/unlock')
def unlock():
  return render_template("unlock.html")
  
@application.route('/account')
def account():
  return render_template("account.html")
  
@application.route('/uploads', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST' and 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    return render_template("dashboard.html")
  return render_template('dashboard.html')  
  

if __name__ == "__main__":
    application.debug = True
    application.run()
