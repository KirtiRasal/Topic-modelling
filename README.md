## Dynamic topic modeling

This repository contains the data preprocessing steps and 3 topic modeling algorithms have been applied on the data.

## Contents of the file

- The Input file 'data_files.json' is the required extracted data from pickle file, it is stored inside original data folder.
```
original_data/data_files.json
```

- The Input pickle consists of all the data in english, it is stored inside original data folder.
```
original_data/energy_legal_documents_english.p

```

- The processing python script is created to clean the dataset.
```
Data_preprocess.py

```

- The python script to visualize the eurvoc descriptors (keywords) fro the documents and check their trend

```
Eurovoc_descriptor_visualization.py

```

## Environment

We need a python environment for executing the cleaning files. Latest python version for 64 bit Windows 10 can be supportive to run these files.

## Installation

pip version 21.1.3

Install packages with pip: -r requirements.txt

The following command will install the packages according to the configuration file requirements.txt. 
Run the following command where requirements.txt file is located.

```
pip install -r requirements.txt

```

Download the spacy library

```
python -m spacy download en_core_web_sm

```

Run the Data_preprocess.py file using below command, it will create new cleaned documnets file and save in the original_data folder with name data_files.json

```
python Data_preprocess.py

```

Run the Eurovoc_descriptor_visualization.py  file using below command, it will create new graphs using eurovoc descriptors and save in the Graphs folder

```
python Eurovoc_descriptor_visualization.py

```

