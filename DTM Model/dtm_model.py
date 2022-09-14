
from dtmvisual import gensim_corpus
from dtmvisual import VisualizeTopics

import pandas as pd

from dtmvisual import DTMmodel as mod

def main():

    legal_docs_df = pd.read_json('data/data_files.json')

    legal_docs_df['Effective_date'] = legal_docs_df['Effective_date'].apply(lambda x: pd.Timestamp(x))

    path = "DTM_Wrapper/dtm-win64.exe"

    legal_docs_df['Year'] = legal_docs_df['Effective_date'].dt.year

    time_slices = legal_docs_df.groupby('Year').size()
    time_seq = time_slices.values.tolist()

    sentences = gensim_corpus.docs_to_list(legal_docs_df['clean_Document_Content'])
    corpus = gensim_corpus.corpus_dtm(sentences)

    model = mod.dtm_model(path, corpus, time_seq, num_topics=15,
                    id2word=corpus.dictionary, alpha=0.01, model='fixed')


    mod.save_model(model=model, path="model/", output_name="DTM_Fixed")

    model = mod.load_saved_model(path="" , output_name='DTM_Fixed')

    topicsnew = model.show_topic(topicid=6, time=13, topn=20)
    topicsnew

    df = VisualizeTopics.topic_distribution(num_topics=5, model=model, time_seq=time_seq)


    VisualizeTopics.visualize_topics(df)

if __name__ == "__main__":
	main()



