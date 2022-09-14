

from dtmvisual import gensim_corpus

import json
import pandas as pd

data_file_name_with_path = 'data_files.json'

with open(file=data_file_name_with_path, mode='r') as file:
    data = json.load(fp=file)

legal_docs_df = pd.read_json('data_files.json')

legal_docs_df['Effective_date'] = legal_docs_df['Effective_date'].apply(lambda x: pd.Timestamp(x))

legal_docs_df['Year'] = legal_docs_df['Effective_date'].dt.year

legal_docs_df.sort_values('Year')

time_slices = legal_docs_df.groupby('Year').size()

path = "dtmvisual\dtm-win64.exe"

sentences = gensim_corpus.docs_to_list(legal_docs_df['clean_Document_Content'])
corpus = gensim_corpus.corpus_dtm(sentences)





