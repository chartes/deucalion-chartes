from flask import Flask, render_template

from flask_pie import PieController
from pie_extended.models.lasla.get import get_iterator_and_processor
from pie_extended.cli.sub import get_tagger

app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")


# Add the lemmatizer routes
controller = PieController(
    tagger=get_tagger("lasla", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=get_iterator_and_processor,
    force_lower=True
)
controller.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
