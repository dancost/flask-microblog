from flask import Flask

# create the application object as an instance of class Flask
app = Flask(__name__)

# we import the routes module from the app package here because the routes module
# depends on the app variable - this way we avoid circular imports

from app import routes