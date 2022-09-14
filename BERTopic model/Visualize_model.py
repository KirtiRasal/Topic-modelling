import pandas as pd
import pickle

from gensim import corpora

from bertopic import BERTopic
from flair.embeddings import TransformerDocumentEmbeddings


def main():
    legal_docs_df = pd.read_json('data/data_files.json')

    documents_orig = []
    documents_orig = legal_docs_df.clean_Document_Content.to_list()

    dates = legal_docs_df['Effective_date'].apply(lambda x: pd.Timestamp(x))

    topic_model = BERTopic.load("pickle/BERT_Model")

    topics = topic_model.get_topics()

    topics_over_time = topic_model.topics_over_time(documents_orig, topics, dates, nr_bins=20)


    topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=20)

    topic_model.get_topic_info()

    docs = topic_model.get_representative_docs(2)

    for n in docs[5]:
        for i, c in enumerate(legal_docs_df['clean_Document_Content']):   
            if n == c:
                elinks = legal_docs_df.iloc[[i]]
                print(elinks.Doc_elink)


if __name__ == "__main__":
	main()