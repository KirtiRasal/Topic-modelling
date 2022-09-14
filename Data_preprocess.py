import pickle
from collections import Counter
import html
from bs4 import BeautifulSoup
import json
from json import dumps
import datetime

import numpy as np
import pandas as pd
import re, nltk, spacy
from nltk.corpus import stopwords
from datetime import datetime
from nltk.stem import WordNetLemmatizer

import lexnlp.nlp.en.tokens

#Loading spacy 
nlp = spacy.load("en_core_web_sm")

#downloading english stopwords from nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

#downloading wordnet from nltk
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def create_celex_ids(legal_docs):
    celex_ids = []
    for i, c in enumerate(legal_docs.keys()):    
        #id = legal_docs[i]

        celex_ids.append(c)

    return celex_ids

def create_title(legal_docs):
    titles = []
    for i, c in enumerate(legal_docs.keys()):    
        title = legal_docs[c]['title']

        titles.append(title)

    return titles

def create_doc_elinks(legal_docs):
    doc_elinks = []
    for i, c in enumerate(legal_docs.keys()):    
        elink = legal_docs[c]['eliLink']

        doc_elinks.append(elink)

    return doc_elinks


def create_date_Of_Documents(legal_docs):
    date_Of_Documents = []
    for i, c in enumerate(legal_docs.keys()):    
        dateOfDocument = legal_docs[c]['dateOfDocument']

        date_Of_Documents.append(dateOfDocument)
    
    return date_Of_Documents


def create_effectdate(legal_docs):
    effectDate = []
    for i, c in enumerate(legal_docs.keys()):
        if legal_docs[c]['effectDate'] == 'NA':
            effectDate.append(legal_docs[c]['effectDate'])
        else:
            try:
                effectDate.append(legal_docs[c]['effectDate'])
            except ValueError:
                effectDate.append("NA")

    return effectDate

def create_eurovoc_Descriptors(legal_docs):
    eurovoc_Descriptors = []
    for i, c in enumerate(legal_docs.keys()):    
        eurovocDescriptor = legal_docs[c]['eurovocDescriptor']

        eurovoc_Descriptors.append(eurovocDescriptor)

    return eurovoc_Descriptors

def create_subject_Matters(legal_docs):
    subject_Matters = []
    for i, c in enumerate(legal_docs.keys()):    
        subjectMatter = legal_docs[c]['subjectMatter']

        subject_Matters.append(subjectMatter)

    return subject_Matters


def create_authors(legal_docs):
    authors = []
    for i, c in enumerate(legal_docs.keys()):    
        author = legal_docs[c]['author']

        authors.append(author)

    return authors

def create_forms(legal_docs):
    forms = []
    for i, c in enumerate(legal_docs.keys()):    
        form = legal_docs[c]['form']

        forms.append(form)

    return forms

def create_additional_Informations(legal_docs):
    additional_Informations = []
    for i, c in enumerate(legal_docs.keys()):    
        additionalInformation = legal_docs[c]['additionalInformation']

        additional_Informations.append(additionalInformation)

    return additional_Informations

def create_authentic_Languages(legal_docs):
    authentic_Languages = []
    for i, c in enumerate(legal_docs.keys()):    
        authenticLanguage = legal_docs[c]['authenticLanguage']

        authentic_Languages.append(authenticLanguage)

    return authentic_Languages

def create_addressees(legal_docs):
    addressees = []
    for i, c in enumerate(legal_docs.keys()):    
        addressee = legal_docs[c]['addressee']

        addressees.append(addressee)

    return addressees

def create_document_contents(legal_docs):
    document_contents = []
    for i, c in enumerate(legal_docs.keys()):    
        eurovoc_split = legal_docs[c]['documentInformation']['documentContent']
        eurovoc_split = re.sub(r"[-!?@&*\(\)/>=.:;,|%\'\`\"\_\n\d+]", ' ', eurovoc_split).lower().lstrip()
        eurovoc_split = eurovoc_split.split()
        eurovoc_split = [word for word in eurovoc_split if not word in set(stop_words)]
        eurovoc_split = ' '.join(eurovoc_split)
        document_contents.append(eurovoc_split)

    return document_contents


def clean_up(text):

  text_out = []

  removal=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']

  #text = re.sub(r"[-!?@&*\(\)/>=.:;,|%\'\`\"\_\n\d+]", ' ', text).lower().lstrip()

  text = html.unescape(text)
  text = BeautifulSoup(text, "lxml").text

  stop_words = set(stopwords.words('english'))

  stop_words1= [str(item) for item in list(lexnlp.nlp.en.tokens.STOPWORDS)]

  stop_words2 = ['ec','eu','xml','de','article','accordance','official','journal','eur','lex',
                'european','commission','regulation','im','directive','annex','section','paragraph',
                'shall','party','policy','datum','information','member','union','germany',
                'spain','france','italy','ireland','greece','united','kingdom','poland','netherlands',
                'january','february','march','april','may','june','july','august','september',
                'october','november','december']

  stop_words1.extend(stop_words2)
  stop_words.extend(stop_words1)

  doc= nlp(text)

  for token in doc:
    if token.is_stop == False and len(token)>2 and token.pos_ not in stop_words and removal:
      lemma = token.lemma_
      text_out.append(lemma)

  text_join = ' '.join(text_out)

  return text_join


def main():

    #Loading original dataset to extract required data
    filename = "original_data/energy_legal_documents_english.p"
    infile = open(filename,'rb')
    legal_docs = pickle.load(infile)
    infile.close()

    #creating dataframe of the extracted data
    Legal_docs_df = pd.DataFrame(
    {'Celex_id': create_celex_ids(legal_docs),
     'Title': create_title(legal_docs),
     'Doc_elink': create_doc_elinks(legal_docs),
     'Date_Of_Document': create_date_Of_Documents(legal_docs),
     'Effective_date': create_effectdate(legal_docs),
     'Eurovoc_Descriptor': create_eurovoc_Descriptors(legal_docs),
     'Subject_Matter': create_subject_Matters(legal_docs),
     'Author': create_authors(legal_docs),
     'Form': create_forms(legal_docs),
     'Additional_Information': create_additional_Informations(legal_docs),
     'Authentic_Language': create_authentic_Languages(legal_docs),
     'Addressee': create_addressees(legal_docs),
     'Document_Content': create_document_contents(legal_docs)
    })

    #Calling cleaning function to clean the 
    Legal_docs_df['clean_Document_Content'] = Legal_docs_df['Document_Content'].apply(clean_up)

    #removing the with empty efective date rows
    Legal_docs_df = Legal_docs_df[Legal_docs_df['Effective_date'] != 'NA']

    #excluding data with incorrect date format
    Legal_docs_df = Legal_docs_df[Legal_docs_df['Effective_date'] != '1996-05-00, 1996-05-00, 1996-05-00']

    #Converting the effective date column to datetime format
    Legal_docs_df['Effective_date'] = pd.to_datetime(Legal_docs_df['Effective_date'])

    # Convert DataFrame to JSON file
    dict_records = Legal_docs_df.to_dict('records')
    with open('original_data/data_files_new.json', 'w') as f:
        json.dump(dict_records, f)


if __name__ == "__main__":
	main()


