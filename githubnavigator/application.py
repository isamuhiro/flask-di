from dependency_injector import containers
from flask import Flask

from .containers import Container
from . import views


def create_app() -> Flask:
    container = Container()
    container.config.from_yaml('config.yml')
    container.config.github.auth_token.from_env('GITHUB_TOKEN')
    container.wire(modules=[views])

    app = Flask(__name__)
    app.container = container
    app.add_url_rule('/', 'index', views.index)

    return app
