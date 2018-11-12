from flask import Flask, redirect, url_for, session, render_template

application = Flask(__name__)

#@application.route('/')
#def profile():
##  access_token = session.get('access_token')
#  if access_token is None:
#  return render_template('profile.html')
#  else:
#    return render_template('dashboard.html')

@application.route('/')
def dashboard():
  return render_template('dashboard.html')

@application.route('/unlock')
def unlock():
    return render_template("unlock.html")

@application.route('/upload')
def upload():
    return render_template("upload.html")

@application.route('/account')
def account():
    return render_template("account.html")
'''
  access_token = session.get('access_token')
  if access_token is None:
    return redirect(url_for('profile'))
  access_token = access_token[0]
  from urllib2 import Request, urlopen, URLError
  headers = {'Authorization': 'OAuth ' + access_token}
  req = Request('https://www.googleapis.com/oauth2/v1/userinfo', None, headers)

  try:
    res = urlopen(req)
  except URLError as e: 
    if e.code == 401:
      #bad token
      session.pop('access_token', None)
      return redirect(url_for('profile'))
    return res.read()
  '''
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
