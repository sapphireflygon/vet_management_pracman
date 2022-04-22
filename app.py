from flask import Flask

from controllers.animals_controller import animals_blueprint
from controllers.practices_controller import practices_blueprint
from controllers.vets_controller import vets_blueprint

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(practices_blueprint)
app.register_blueprint(vets_blueprint)

if __name__ == '__main__':
    app.run()