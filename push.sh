echo "Please enter your commit info: "
read info
git add .
git commit -m "$info"
git push heroku main