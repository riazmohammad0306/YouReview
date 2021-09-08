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
    print(comment_list)

def traitement(x):
    x=x.replace('\n',' ')
    x=' '.join(word.strip(string.punctuation) for word in x.split())
    x=x.lower()
    return x
    
    

if __name__ == "__main__": 
    urls = [
        "https://www.youtube.com/watch?v=0XJg74qnvxE",
    ]


    # for url in urls: 
    ScraperComment(urls[0])




