from flask import Flask, render_template

from controllers.animals_controller import animals_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.treatment_notes_controller import treatment_note_blueprint

app = Flask(__name__)

app.register_blueprint(owners_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(animals_blueprint)
app.register_blueprint(treatment_note_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()