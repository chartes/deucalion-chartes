from flask import Flask, render_template

from flask_pie import PieController
from pie_extended.models.lasla import imports as lasla_get
from pie_extended.models.fro import imports as fro_get
from pie_extended.models.fr import imports as fr_get
from pie_extended.models.freem import imports as freem_get
from pie_extended.models.grc import imports as grc_get
from pie_extended.cli.sub import get_tagger

app = Flask(__name__)
# Add the lemmatizer routes


controller_lasla = PieController(
    path="/api/lasla/", name="lasla-api",
    tagger=get_tagger("lasla", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=lasla_get.get_iterator_and_processor,
    force_lower=False
)
controller_lasla.init_app(app)


controller_fro = PieController(
    path="/api/fro-1/", name="fro-api",
    tagger=get_tagger("fro", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=fro_get.get_iterator_and_processor,
    force_lower=True
)
controller_fro.init_app(app)


controller_fr = PieController(
    path="/api/fr/", name="fr-api",
    tagger=get_tagger("fr", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=fr_get.get_iterator_and_processor,
    force_lower=True
)
controller_fr.init_app(app)


controller_freem = PieController(
    path="/api/freem/", name="freem-api",
    tagger=get_tagger("freem", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=freem_get.get_iterator_and_processor,
    force_lower=True
)
controller_freem.init_app(app)


controller_grc = PieController(
    path="/api/grc/", name="grc-api",
    tagger=get_tagger("grc", batch_size=8, device="cpu"),
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_processor=grc_get.get_iterator_and_processor,
    force_lower=True
)
controller_freemgrc.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
