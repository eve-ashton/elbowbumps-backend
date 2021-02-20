# Elbow Bump Backend

## Introdution

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
