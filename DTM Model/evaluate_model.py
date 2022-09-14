from dtmvisual import gensim_corpus

import pandas as pd

from gensim.models import CoherenceModel
from dtmvisual import DTMmodel as mod



def get_c_v(time, model, sentences, corpus):

    topics_dtm = model.dtm_coherence(time=time)
    c_v_coherence = CoherenceModel(topics=topics_dtm, 
                                texts=sentences, 
                                dictionary=corpus.dictionary, 
                                coherence='c_v')
    coherence = c_v_coherence.get_coherence()

    return coherence


def get_u_mass(time, model, sentences, corpus):

    topics_dtm = model.dtm_coherence(time=time)
    u_mass_coherence = CoherenceModel(topics=topics_dtm, 
                                texts=sentences, 
                                dictionary=corpus.dictionary, 
                                coherence='u_mass')
    coherence = u_mass_coherence.get_coherence()

    return coherence


def get_c_uci(time, model, sentences, corpus):

    topics_dtm = model.dtm_coherence(time=time)
    c_uci_coherence = CoherenceModel(topics=topics_dtm, 
                                texts=sentences, 
                                dictionary=corpus.dictionary, 
                                coherence='u_uci')
    coherence = c_uci_coherence.get_coherence()

    return coherence


def get_c_w2v(time, model, sentences, corpus):

    topics_dtm = model.dtm_coherence(time=time)
    c_w2v_coherence = CoherenceModel(topics=topics_dtm, 
                                texts=sentences, 
                                dictionary=corpus.dictionary, 
                                coherence='c_w2v')
    coherence = c_w2v_coherence.get_coherence()

    return coherence

def main():

    legal_docs_df = pd.read_json('data/data_files.json')

    sentences = gensim_corpus.docs_to_list(legal_docs_df['clean_Document_Content'])
    corpus = gensim_corpus.corpus_dtm(sentences)


    model = mod.load_saved_model(path="model/" , output_name='DTM_Fixed')

    #evaluating c_v coherence measure
    c_v = get_c_v(time=2, model=model, sentences=sentences, corpus=corpus)
    print("Topic coherence c_v is", c_v)

    #evaluating u_mass coherence measure
    u_mass = get_u_mass(time=2, model=model, sentences=sentences, corpus=corpus)
    print("Topic coherence u_mass is", u_mass)

    #evaluating c_uci coherence measure
    c_uci = get_c_uci(time=2, model=model, sentences=sentences, corpus=corpus)
    print("Topic coherence c_uci is", c_uci)

    #evaluating c_w2v coherence measure
    c_w2v = get_c_w2v(time=2, model=model, sentences=sentences, corpus=corpus)
    print("Topic coherence c_w2v is", c_w2v)


if __name__ == "__main__":
	main()
