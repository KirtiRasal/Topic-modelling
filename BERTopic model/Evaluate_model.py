import pandas as pd

from gensim import corpora
from gensim.models import CoherenceModel

from bertopic import BERTopic
from flair.embeddings import TransformerDocumentEmbeddings


def get_c_v(topic_words, tokens, corpus, dictionary):
    # Evaluate
    coherence_model = CoherenceModel(topics=topic_words, 
                                    texts=tokens, 
                                    corpus=corpus,
                                    dictionary=dictionary, 
                                    coherence='c_v')
    coherence = coherence_model.get_coherence()

    return coherence


def get_u_mass(topic_words, tokens, corpus, dictionary):
    # Evaluate
    coherence_model = CoherenceModel(topics=topic_words, 
                                    texts=tokens, 
                                    corpus=corpus,
                                    dictionary=dictionary, 
                                    coherence='u_mass')
    coherence = coherence_model.get_coherence()

    return coherence


def get_c_uci(topic_words, tokens, corpus, dictionary):
    # Evaluate
    coherence_model = CoherenceModel(topics=topic_words, 
                                    texts=tokens, 
                                    corpus=corpus,
                                    dictionary=dictionary, 
                                    coherence='c_uci')
    coherence = coherence_model.get_coherence()

    return coherence


def get_w2v(topic_words, tokens, corpus, dictionary):
    # Evaluate
    coherence_model = CoherenceModel(topics=topic_words, 
                                    texts=tokens, 
                                    corpus=corpus,
                                    dictionary=dictionary, 
                                    coherence='c_w2v')
    coherence = coherence_model.get_coherence()

    return coherence

def main():

    #loading the cleaned dataset
    legal_docs_df = pd.read_json('data/data_files.json')

    #creating list of text documents
    documents_orig = []
    documents_orig = legal_docs_df.clean_Document_Content.to_list()

    #loading the bertopic model pickle file
    topic_model = BERTopic.load("pickle/BERT_Model.pkl")

    #getting all the topics from the model
    topics = topic_model.get_topics()


    # Preprocess Documents
    documents = pd.DataFrame({"Document": documents_orig,
                            "ID": range(len(documents_orig)),
                            "Topic": topics})
    documents_per_topic = documents.groupby(['Topic'], as_index=False).agg({'Document': ' '.join})
    cleaned_docs = topic_model._preprocess_text(documents_per_topic.Document.values)

    # Extract vectorizer and analyzer from BERTopic
    vectorizer = topic_model.vectorizer_model
    analyzer = vectorizer.build_analyzer()

    # Extract features for Topic Coherence evaluation
    words = vectorizer.get_feature_names()
    tokens = [analyzer(doc) for doc in cleaned_docs]
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    topic_words = [[words for words, _ in topic_model.get_topic(topic)] 
                for topic in range(len(set(topics))-1)]

    #evaluating c_V coherence measure
    c_v = get_c_v(topic_words, tokens, corpus, dictionary)
    print("Topic coherence c_v is", c_v)

    #evaluating u_mass coherence measure
    u_mass = get_u_mass(topic_words, tokens, corpus, dictionary)
    print("Topic coherence c_v is", u_mass)

    #evaluating c_uci coherence measure
    c_uci = get_c_uci(topic_words, tokens, corpus, dictionary)
    print("Topic coherence c_v is", c_uci)

    #evaluating c_w2v coherence measure
    c_w2v = get_w2v(topic_words, tokens, corpus, dictionary)
    print("Topic coherence c_v is", c_w2v)


if __name__ == "__main__":
	main()