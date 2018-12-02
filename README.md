# FiPi Web Application

The FiPi Web Application is a senior seminar project that functions as an alternative method for storing and securing valuable items.  The project itself encompases the functionalities built-in with OpenCV's facial recognition software (LBPH) in order to create a smart lock that uses a Raspberry Pi to unlock a treasure box.  Please see below for installation guidelines.

# Pre Installation:

In order to recreate this project, you must have the following prerequisites:

1) Have an AWS account - this can be free tier elegability
2) Have a Google account
3) Have Python 3.6 (or newer) installed on your local machine

# Installation:

Now that you have the prerequisites taken care of, the installation description follows.  

1) The Python framework that we will be using throughout this project is Flask.  This is a lightweight framework that has a smaller learning curve than other frameworks, such as Django.  
  - In order to download Flask and install virtualenv in order to create a virtual enviornment, follow the tutorial on AWS:           https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html.  This will guide you through creating your first Flask application hosted on AWS.  
  - IMPORTANT: when creating an enviornment with eb init -i, MAKE SURE TO SAVE YOUR KEYPAIR ONCE CREATED.  This will be required in step 5c.
2) Once eb-flask, virtualenv, and eb cli are installed and saved into your requirements.txt, you are now able to start coding.  In order to start this in a Flask application, you must create an application.py file and pull the file present in this github repository.  This file will route to the subsequent files that make this project.  
3) Go to https://console.developers.google.com/apis/ and create a new project.  Once this is done, navigate to credentials -> create credentials -> OAuth Client ID.
**** GOOGLE SIGN IN ONLY WORKS ON AWS, THIS WILL NOT WORK ON LOCALHOST ****

  - This is where you will get the client ID (that must be put into your profile.html page in order to use Google OAuth for sign in.
  - You will also need to specify your Javascript origins and redirect URIs after selecting "Web Application."
4) Once the console is set up, navigate to https://developers.google.com/identity/sign-in/web/sign-in in order to find how the Google signin button is created.  Troubleshooting can also be done on this page, along with getting profile information once the user is logged in (https://developers.google.com/identity/sign-in/web/people).
5) Run a "pip install flask-uploads" and then "pip freeze > requirements.txt" in order to include the flask_uploads library in your application.py file for uploading photos.  

**** THIS NEXT STEP IS OPTIONAL BUT NECESSARY IF YOU WISH TO HAVE ACCESS TO YOUR WEBCAM ON YOUR AWS HOSTED SITE ****
5a) Due to the fact that having webcam accessibility requires a secure connection, you must have an SSL certification attached to your public AWS IP.  However, this IP that is given once you spin up an instance cannot be given an SSL certification.  An option to circumvent this is to buy a host name on Route 53.
5b) Once you buy a domain, follow this link to route the traffic from your instance to your created domain name (https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html).  Once this is done, you will need to navigate to the configuration section in your elastic beanstalk dashboard and modify your load balancer.  You will need to "Add Listener" in order to service HTTPS requests (see link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html).  
5c) You will now need SSH access to your application.  Download PuTTY for this.  You will need to use PuTTYgen to create a private key.  See this link for a walkthrough: https://www.youtube.com/watch?v=bi7ow5NGC-U.
  - optional: you can either use the hostname of your Route 53 domain OR elastic beanstalk instance if you set up an Elastic IP (recommended).  This allows multiple elastic beanstalk instances to assume the same Elastic IP when terminated

6) 
