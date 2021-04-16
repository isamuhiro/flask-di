from flask import request, jsonify
from dependency_injector.wiring import inject, Provide

from .services import SearchService
from .containers import Container


@inject
def index(search_service: SearchService = Provide[Container.search_service]):
    query = request.args.get('query', 'Dependency Injector')
    limit = request.args.get('limit', 10, int)

    repositories = search_service.search_repositories(query, limit)

    return jsonify(repositories)
