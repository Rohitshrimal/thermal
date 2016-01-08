from .appmodule import create_app, make_celery, register_db

app = create_app()
register_db(app)
celery = make_celery(app)
