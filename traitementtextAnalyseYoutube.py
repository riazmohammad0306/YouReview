# Importation des modules nécessaires

import pandas as pd
import re
import string
import fasttext
from nltk.corpus import stopwords
from nltk import word_tokenize
from textblob import TextBlob,Blobber
# from textblob_fr import PatternAnalyzer,PatternTagger


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from joblib import dump,load

# tb = Blobber(pos_tagger= PatternTagger(),analyzer=PatternAnalyzer())


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time



def ScraperComment(url):
    # Selenium automates tasks in web browser
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
    driver.get(url)
    time.sleep(5)

    # To continuously scroll until the max height
    prev_h = 0
    while True: 
        # On doit automatiser le fait de scroller la page jusqu'au bas (height of the page) pour le chargement des commentaires. 
        # Selenium nous donne la facilité de run un script
        height = driver.execute_script("""
            function getActualHeight() {
                return Math.max(
                    Math.max(document.body.scrollHeight, document.documentElement.scrollHeight), 
                    Math.max(document.body.offsetHeight, document.documentElement.offsetHeight), 
                    Math.max(document.body.clientHeight, document.documentElement.clientHeight), 
                );
            }
            return getActualHeight();
        """)
        driver.execute_script(f"window.scrollTo({prev_h}, {prev_h + 250})")
        
        # This one is needed to give the page the time to load before moving to next scroll
        time.sleep(2)
        prev_h += 250
        if prev_h >= height: 
            break

    # Convert webpage to BS
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    # On the html file the title is in the container id and h1 tag
    title_text_div = soup.select_one('#container h1')
    # print(title_text_div.text)
    title = title_text_div and title_text_div.text

    # On the html file comments are in the context_
    comment_div = soup.select("#content #content-text")
    comment_list = [x.text for x in comment_div]
    # print(title, comment_list)
    df_liste2 = pd.DataFrame(comment_list,columns=['text'])
    return df_liste2
    #import fasttext
    #import re
#
    #PRETRAINED_MODEL_PATH = '/tmp/lid.176.bin'
    #model = fasttext.load_model(PRETRAINED_MODEL_PATH)
#
    #
    #list_lang = []
    #for sentences in comment_list: 
    #    
    #    sentences = sentences.rstrip()
    #    sentences = sentences.rstrip("\n")
    #    sentences = re.sub(r'[^\w\s]','',sentences)
    #    predictions = model.predict(sentences)
    #    list_lang.append(predictions)
    #



if __name__ == "__main__": 
    urls = [
        "https://www.youtube.com/watch?v=ZSESkoRez40",
    ]
    #https://www.youtube.com/watch?v=ZSESkoRez40
    #https://www.youtube.com/watch?v=RYk8vv4vPME liste 3
    # for url in urls: 
    df_com = ScraperComment(urls[0])


def traitement(x):
    x=x.replace('\n',' ')
    x=' '.join(word.strip(string.punctuation) for word in x.split())
    x=x.lower()
    return x

# wget -O /tmp/lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
PRETRAINED_MODEL_PATH = '/tmp/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

def get_lang(sentences):
    
    predictions = model.predict(sentences)
    return predictions[0][0][-2:].upper()


stop_words_fr = set(stopwords.words('french'))
stop_words_en = set(stopwords.words('english'))

def remove_stopwords(line):
    word_tokens = word_tokenize(line)
    ligne_filtre = [w for w in word_tokens if not w in stop_words_en]
    return ' '.join(ligne_filtre)


df_com['text']=df_com['text'].apply(lambda x: traitement(x))

df_com['lang']=df_com['text'].apply(lambda x: get_lang(x))

df_com=df_com[df_com['lang']=='EN']

df_com['polarite']=df_com['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

df_com['pol_cat']=0

df_com['pol_cat'][df_com.polarite>0]=1
df_com['pol_cat'][df_com.polarite<0]=-1
df_com['pol_cat'][df_com.polarite==0]=0

df_com['stop_text']=df_com['text'].apply(lambda x: remove_stopwords(x))
df_com
model = load('ModelAnalyseYoutube.joblib')

X = df_com['stop_text']

yp = model.predict(X)
print(yp)