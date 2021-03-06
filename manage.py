# This file starts the WSGI web application.
# - Heroku starts gunicorn, which loads Procfile, which starts manage.py
# - Developers can run it from the command line: python runserver.py

from app import create_app
from flask_debugtoolbar import DebugToolbarExtension

app = create_app()


### DebugToolbar
toolbar = DebugToolbarExtension()
toolbar.init_app(app)

# Start a development web server if executed from the command line
if __name__ == "__main__":
    # Manage the command line parameters such as:
    # - python manage.py runserver
    # - python manage.py db
    from app import manager

    manager.run()
