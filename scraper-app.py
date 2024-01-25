import requests
from bs4 import BeautifulSoup

wiki_page = requests.get('https://en.wikipedia.org/wiki/London')


# HTML parser 
wiki_page = BeautifulSoup(wiki_page.content, 'html.parser')




# Find p tags inside wiki body containers 

wiki_page_body = wiki_page.find(id="bodyContent").find_all("p")



# Extracting the text from the result set

corpus = []

for item in wiki_page_body:
    corpus.append(item.text)


corpus_text = ''

for i in corpus:
    corpus_text = corpus_text + ' ' + i


# Tokenization 

corpus_text = corpus_text.replace('.', ' ')
corpus_text = corpus_text.replace('(', ' ')
corpus_text = corpus_text.replace(')', ' ')
corpus_text = corpus_text.lower()   
corpus_text = corpus_text.split()


# Word frequencies

corpus_word_feq = {}


for word in corpus_text:

    if word not in corpus_word_feq:
        corpus_word_feq[word] = 1
    else:
        corpus_word_feq[word] += 1    



sorted_items_desc = sorted(corpus_word_feq.items(), key=lambda item: item[1], reverse=True)
sorted_dict_desc = dict(sorted_items_desc)


for word, count in sorted_dict_desc.items():
    print(f'Word: {word}, Frequency: {count} ')









