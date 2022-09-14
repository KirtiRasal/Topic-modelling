import pandas as pd
import pickle

from gensim import corpora

from bertopic import BERTopic
from flair.embeddings import TransformerDocumentEmbeddings


def bertopic_model(legal_embedding, top_n_words = None, n_gram_range = (1,2), 
                 min_topic_size = 5, documents_orig=None):
    

    print ("initializing the model.....")
    topic_model = BERTopic(embedding_model= legal_embedding, n_gram_range=n_gram_range, 
                           top_n_words=top_n_words, min_topic_size=min_topic_size)

    topics, _ = topic_model.fit_transform(documents_orig)
    print('BERTopic model loaded')
    return topics, topic_model


def get_topic_information(topic_model):

    topic_information = topic_model.get_topic_info()

    return topic_information


def save_model(topic_model, path):
    
    topic_model.save(path)

    print ("Model saved successfully")


def load_saved_model(path):
    
    model = BERTopic.load(path)

    return model


def main():
    
    legal_embedding = TransformerDocumentEmbeddings("nlpaueb/bert-base-uncased-eurlex")

    # save the model to local
    filename = 'pickle/Legal_model.pkl'
    pickle.dump(legal_embedding, open(filename, 'wb'))


    legal_docs_df = pd.read_json('data/data_files.json')


    documents_orig = []
    documents_orig = legal_docs_df.clean_Document_Content.to_list()

    #loading bertopic model, passing the arguments
    topics, topic_model = bertopic_model(legal_embedding, top_n_words=10, n_gram_range= (1,2), min_topic_size=15, documents_orig=documents_orig)

    print(topics)

    save_model(topic_model, path="pickle/BERT_Model.pkl")

    topic_model = load_saved_model(path="pickle/BERT_Model.pkl")

    dates = legal_docs_df['Effective_date'].apply(lambda x: pd.Timestamp(x))
	
    topics_over_time = topic_model.topics_over_time(documents_orig, topics, dates, nr_bins=20)

    topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=20)

    topic_information = get_topic_information(topic_model)

    print(topic_information)

if __name__ == "__main__":
	main()


