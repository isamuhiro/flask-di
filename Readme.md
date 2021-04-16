# Flask Web Service - Github Repositories Search

This project follows the dependency injection paradigms using Python, consuming Github API Client.

## Enviroment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=githubnavigator.application
export FLASK_ENV=development
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN
flask run
```

## Endoints

```bash
curl --request GET \
  --url 'http://localhost:5000/?query=Python&limit=10'
```