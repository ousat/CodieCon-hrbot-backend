from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
# from io import StringIO
from io import BytesIO
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
import nltk
from nltk.corpus import stopwords

class PdfConverter:

   def __init__(self, file_path):
       self.file_path = file_path
# convert pdf file to a string which has space among words
   def convert_pdf_to_txt(self):
       rsrcmgr = PDFResourceManager()
       retstr = BytesIO()
       codec = 'utf-8'  # 'utf16','utf-8'
       laparams = LAParams()
       device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
       fp = open(self.file_path, 'rb')
       interpreter = PDFPageInterpreter(rsrcmgr, device)
       password = ""
       maxpages = 0
       caching = True
       pagenos = set()
       for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
           # print(page)
           interpreter.process_page(page)
       fp.close()
       device.close()
       str = retstr.getvalue()
       retstr.close()
       return str
# convert pdf file text to string and save as a text_pdf.txt file
   def save_convert_pdf_to_txt(self):
       content = self.convert_pdf_to_txt()
       txt_pdf = open('text_pdf.txt', 'wb')
       txt_pdf.write(content.encode('utf-8'))
       txt_pdf.close()


def process_pdf(file_path):
    # print(file_path)
    pdfConverter = PdfConverter(file_path=file_path)
    text =pdfConverter.convert_pdf_to_txt()
    stop_words =set(stopwords.words('english'))
    text=text.replace("\u200b","")
    text=text.replace("\n","")
    text = re.sub(r'[^\x00-\x7F]','', text)
    text=text.lower()
    word_tokens = word_tokenize(text)
    new_word = []
    ps = PorterStemmer()
    for w in word_tokens:
        new_word.append(ps.stem(w))

    filtered_sentence = [w for w in new_word if not w in stop_words]
    ds=["javascript", "html", "css", "bootstrap3", "bootstrap4", "vue.js", "vue", "react", "angular.js", "angular", "ember", "emberjs", "web application", "web apps","express", "express.js", "jquery", "responsive", "web", "front end", "web-app", "js", "django", "full-stack", "full stack", "ui", "ux", "website", "php", "bootstrap", "mongo", "mysql", "python", "asp.net", "nginx", "docker", "load balancing", "rest api", "rest", "api", "gateway", "sockets", "elixir", "scala", "erlang", "ruby", "golang", "dom manipulation", "dom", "rust", "functional", "oracle", "mysql", "mariadb", "postgresql", "mssql", "sql", "oauth", "rabbitmq", "kafka", "elasticsearch", "apache", "graphql","java"]

    return list(set(intersection(ds,filtered_sentence)))


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def score_calculation(ans,user):
    stop_words =set(stopwords.words('english'))
    ans=ans.replace("\u200b","")
    ans=ans.replace("\n","")
    ans = re.sub(r'[^\x00-\x7F]','', ans)

    ans=ans.lower()

    ans=word_tokenize(ans)
    anss= []
    ps = PorterStemmer()
    for w in ans:
        anss.append(ps.stem(w))

    sent=[w for w in anss if not w in stop_words]


    user=user.replace("\u200b","")
    user=user.replace("\n","")
    user = re.sub(r'[^\x00-\x7F]','', user)

    user=user.lower()

    user=word_tokenize(user)

    userr= []
    ps = PorterStemmer()
    for k in user:
        userr.append(ps.stem(k))

    word1=[k for k in userr if not k in stop_words]

    a = 0
    for i in range(len(word1)):
        if len(get_word_synonyms_from_sent(word1[i], sent))==0:
            pass
        else:
             a=a +1

    synonims=a/len(set(sent))

    exact_key=len(set(intersection(word1,sent)))/len(set(sent))

    if max(synonims,exact_key)>0.2:
         return 1
    else:
        return 0


def get_word_synonyms_from_sent(word, sent):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in sent and lemma != word:
                word_synonyms.append(lemma)
    return word_synonyms
