import spacy as spacy
import urllib.request
import nltk



class Bs4:
    def __init__(self):
        print("constructor ==>")

    def execute(self):
        self.execute_exemplo1()
        self.execute_exemplo2()

    def execute_exemplo1(self):
        pln = spacy.load("/home/gui/.local/lib/python3.10/site-packages/pt_core_news_sm/pt_core_news_sm-3.7.0")
        documento = pln("Estou aprendendo processamento de linguagem natural agora, vai dar certo!")
        print(type(documento))
        for token in documento:
            print(token.text, token.pos_, token.lemma_)
        # o lema extrai o radical da palavra no infinitivo
        doc = pln("encontrei encontraram encontrarão encontrariam cursando curso cursei")
        print([token.lemma_ for token in doc])
        # extrai a palavra no radical
        nltk.download('rslp')
        stremmer = nltk.stem.RSLPStemmer()
        print(stremmer.stem('aprender'))
        for token in doc:
            print(token.text, token.lemma_, stremmer.stem(token.text))

    def execute_exemplo2(self):
        dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')
        dados = dados.read()
        dados_html = bs.BeatifulSoup(dados, 'lxml')