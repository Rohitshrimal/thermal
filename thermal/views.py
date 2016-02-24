import json

from flask import Blueprint, request, Response

thermal = Blueprint('thermal', __name__)


@thermal.route('/')
def index():
    # TODO we want to return an index of top level links for the apps, so admin, camera, etc.
    #  Hardcode for now, but the right way is to probe the application context for these
    #  TODO determine hostname and protocol automatically too
    url_base = request.environ['wsgi.url_scheme'] + '://' + request.environ['HTTP_HOST'] + '/'
    top_level_links = {
        'admin': url_base + 'admin/',
        'camera': url_base + 'camera/',
        'pictures': url_base + 'pictures/',
        'merging': url_base + 'merging/',
        'analysis': url_base + 'analysis/',
    }
    return Response(json.dumps(top_level_links), status=200, mimetype='application/json')