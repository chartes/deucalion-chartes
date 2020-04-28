from cltk.corpus.utils.importer import CorpusImporter

corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')

from pie_extended.cli.sub import download
for file in download("lasla"):
    print(file)
for file in download("fr"):
    print(file)
for file in download("fro"):
    print(file)
