echo "Setting-up virtual environment..."

pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt

echo "finished"