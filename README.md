# Safe_Routes
Rookie Hackathon Project

URL: https://saferoutes-278721.wl.r.appspot.com/

## Description
Our application is a app that helps users determine what is the safest route to take occured related to Substance incidents occured in the past government database that hosts latitudes information on what routes contain take the safest route or the route with less incidents.

For this application we use:
* HTML
* Bootstrap: learned this for easier CSS styling since it has predefined styled components
* Flask and Python: Flask is a python framework that is used for the backend functionality. Primarily the data for the incidents.
* Google Maps Api: Google's API for creating and modifying the map
* Google Cloud App Engine: We deployed out site using Google Cloud's app engine which adds Google debugging, Google analytics, and Google storage. our app to a server app deploy command.
* Google Cloud URL: https://saferoutes-278721.wl.r.appspot.com/


## Git Commands

### Commiting and pushing code to remote
```
git add .
git commit -am 'Some message here on what you changed'
git push
```

### Pulling a branch
`git pull` or `git fetch`

### Checkout a new branch
`git branch checkout branch_name`

### Cleanup branches
`git remote prune origin`

# Gcloud deploying app

Commands to authenticate  and deploy to project we created on google cloud console.
```
gcloud auth application-default login
gcloud app deploy
```

App structure from docs:
```
SAFE_ROUTES/
    app.yaml
    main.py
    requirements.txt
    static/
        script.js
        style.css
    templates/
        index.html
```