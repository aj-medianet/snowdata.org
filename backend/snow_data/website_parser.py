from urllib.request import urlopen
from bs4 import BeautifulSoup
import spacy
nlp = spacy.load('en_core_web_sm')


# strip webpage of all html and return plain text
def get_plain_text(url):
    print("url: ", url)
    website = url
    html = urlopen(website).read()
    soup = BeautifulSoup(html, "html.parser")  # gets rid of html stuff
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ''.join(chunk for chunk in chunks if chunk)
    return text


# returns a similarity score between two texts
def compare_plain_texts(text1, text2):
    text1 = nlp(text1)
    text2 = nlp(text2)
    sim = text1.similarity(text2)
    print(sim)
    return sim

