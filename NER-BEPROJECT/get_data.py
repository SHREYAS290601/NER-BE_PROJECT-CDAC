import os
from main import NER_maker,render_data
import glob
import spacy
from spacy_streamlit import visualize_ner
nlp=spacy.load('en_core_web_md')
store_names=[]
# !NEED TO SORT THIS ASAP
for files in (glob.glob('../Txt Files/*')):
    store_names.append(files)
store_names=sorted(store_names,key=lambda file:os.path.basename(files)[0:1])
dict_for_ner={}
dict_for_ner_top_10={}
for name in glob.glob("../Txt Files/*"):
    dict_for_ner[os.path.basename(name)[0:2]]=os.path.basename(name)[3:-4]
    dict_for_ner_top_10[os.path.basename(name)[0:1]]=os.path.basename(name)[2:-4]

take_name=input("Name of the personality")
# print(dict_for_ner_top_10)
def top_ten(take_name):
    for key,val in dict_for_ner_top_10.items():
        if val==take_name:
            return key
        else:
          pass
def ner_list(take_name):
    for key,val in dict_for_ner_top_10.items():
        if val==take_name:
            return key
        else:
          pass
key_10=int(top_ten(take_name))
key=int(ner_list(take_name))
df=NER_maker(store_names[key])
print(df.head())
doc=render_data(store_names[key])
print(doc)
# *Getting errors
# visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

