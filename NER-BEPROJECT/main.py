import spacy
import glob
import os
import pandas as pd
import numpy as np
from spacy import displacy
from html2image import Html2Image
pd.set_option('display.max_columns', None)
hti = Html2Image()
nlp=spacy.load('en_core_web_md')

# print(store_names)
def NER_maker(file):
    with open(file,encoding='utf-8') as f:
        text=f.read()
    doc=nlp(text)
    # texts=list(doc.sents)
    html = displacy.render(doc, style="ent",page=True)
    hti.screenshot(html_str=html,save_as='image.png')
    values=list(nlp.get_pipe('ner').labels)
    my_val=[]
    for sent in (doc.sents):
        for ent in sent.ents:
            my_val.append([np.NaN if val!=ent.label_ else ent.text for val in values])
    df=pd.DataFrame(my_val,columns=values)
    def highlight(val):
        color='' if type(val)!=str else 'aqua'
        return 'background-color:{}'.format(color)
    df.style.applymap(highlight)
    return df
def render_data(name):
    with open(name,encoding='utf-8') as f:
        text=f.read()
    doc=nlp(text)
    return doc
# my_df_ner=NER_maker(store_names[6])
# print(my_df_ner)
