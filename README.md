# Elbow Bump Backend

## Introduction

This is the backend of the Elbowbump App, build with flask, Python 3.9.1 .

---

## Installation

### ~~Heroku~~

**This might not be necessary anymore since we use github to deploy**

If you got a heroku account, please install heroku on your computer and use the

<pre>
heroku login
</pre>

to login to your heroku account.

### Virtual Environment Setup

## Linux
Use "source venv.sh" command or use following command under the root directory of this repo:

<pre>
pip install virtualenv

virtualenv venv

source ./venv/bin/activate

pip install -r requirements.txt
</pre>

After virtual environment setting is done,   
next time you can enter virtual environment simply with   
"source ./venv/bin/activate" or ". ./venv/bin/activate".

## Windows
The commands are slightly different on Windows to set up the virtual environment.  
Again, on the root directory of this repo:

<pre>
pip install virtualenv

python -m virtualenv venv

./venv/Scripts/activate

pip install -r requirements.txt
</pre>
### Test

Then you can try to run main.py on your local machine to test:

<pre>
python main.py
</pre>

to see if it works properly.

---
## Setting up your local database

In order to set up a local database which allows testing, you need to first install [Postgres](https://www.postgresql.org/download/), and set up your local database.  

For it to work with the code that's already in the repo, you'd need to set your password to '123' for your local repo, otherwise you can change the local database URI in the main.py file towards the end of the file, replacing '123' with whatever you hav set the password to.  

---
## Linking to the remote database

For the remote database to work when testing, you first need to add a .env file containing the Postgres URI. This can be found in the WhatsApp group.  

To set it up properly, you need to provide it with the relevant key and `import os` in main.py. To provide it with the right key, you need to enter `SQLALCHEMY_DATABASE_URI = [the database URI]` in the .env file, and change the ENV variable in the bottom of main.py to anything other than `dev`.

--- 
## Testing the API

To test the API easily, you need to download [Postman](https://www.postman.com/) or use the web-app. You simply need to add a request and point to the right endpoint with the right method, entering the correct parameters.

---

## Commit

You can simply use push.sh script to push, or use the following commands:

<pre>
git add .
git commit -m "commit info"
git push
</pre>

if use heroku CLI, use
<pre> git push heroku main </pre>

instead of general "git push", but shouldn't going to use that anymore.
