from flask import Blueprint

search = Blueprint('search', __name__)

from myapp.source.search import routes