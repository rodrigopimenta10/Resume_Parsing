from tkinter import *
from tkinter import filedialog as fd, ttk
from tkinter.ttk import *
import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams
import codecs
from docx import *
from io import StringIO
def openFile(*args):
    filename = fd.askopenfilename()
    location = str(filename)
    document = Document(location)
    s = ""
    for paragraph in document.paragraphs:
        s += str(paragraph.text.encode(errors='ignore'))
    print(s)
    print()
    #Extract phone number
    regular_expression = re.compile(r"\(?"  # open parenthesis
                                    r"(\d{3})?"  # area code
                                    r"\)?"  # close parenthesis
                                    r"[\s\.-]{0,2}?"  # area code, phone separator
                                    r"(\d{3})"  # 3 digit exchange
                                    r"[\s\.-]{0,2}"  # separator bbetween 3 digit exchange, 4 digit local
                                    r"(\d{4})",  # 4 digit local
                                    re.IGNORECASE)
    result = re.search(regular_expression, s)
    if result:
        result = result.groups()
        result = "-".join(result)
    print(result)

    print()


  #####
    #Extract majors
    


    #Extract skills
    textfile_path = r"/Users/rodrigopimenta/Desktop/keywords.txt"
    keywords_file = open(textfile_path).read()

    tokenizer = RegexpTokenizer(r'\w+')
    sentence_token = tokenizer.tokenize(s)

    def remove_stopwords(text):
        stopwords = nltk.corpus.stopwords.words('english')
        content = [w for w in text if w.lower() not in stopwords]
        return content
        print(content)

    filtered_sentence = remove_stopwords(sentence_token)
    #print(filtered_sentence)

    def get_bigrams(input):
        n = 2
        result = []
        bigrams = ngrams(input, n)
        for grams in bigrams:
            x = "%s %s" % grams
            result.append(x)
        return (result)
        print(result)

    y = get_bigrams(sentence_token)

    def get_threegrams(input):
        n = 3
        result = []
        threegrams = ngrams(input, n)
        for grams in threegrams:
            x = "%s %s %s" % grams
            result.append(x)
        return (result)
        print(result)

    z = get_threegrams(sentence_token)

    def extract_skills(a, b):
        count = 0
        skills = []
        for x in a:
            if x.lower() in b.lower():
                skills.append(x)
                count += 1
        return (skills, count)
        print(skills, count)

    (a,b) = extract_skills(sentence_token, keywords_file)

    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]

    a = remove_values_from_list(a, 'b')
    a = remove_values_from_list(a, 't')
    a = remove_values_from_list(a, 'at')
    a = remove_values_from_list(a, 'in')
    a = remove_values_from_list(a, 'to')
    a = remove_values_from_list(a, 'on')
    a = remove_values_from_list(a, 'n')
    a = remove_values_from_list(a, 'of')
    a = remove_values_from_list(a, 'a')
    a = remove_values_from_list(a, 'as')
    a = remove_values_from_list(a, 'I')
    a = remove_values_from_list(a, 'am')
    a = remove_values_from_list(a, 'by')
    a = remove_values_from_list(a, '5')
    a = remove_values_from_list(a, 'CA')


    # Extract email
    regular_expression = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
    result = re.search(regular_expression, s)
    if result:
        result = result.group()
    print(result)

    print()

    # Automatic search
    # print(sys.argv[0])
    if (s.find("Java") != -1):
        print("Searched term: Java was found")
    else:
        print("Searched term: Java was not found")
    print()

    #Print skills list
    print(a)

    print('Count:')
    print(b)



def win_deleted():
    print("window closed ")
    root.destroy()
    sys.exit()

root = Tk()
root.title("Catering Analytics")

s = Style()
s.configure('My.TFrame', background='grey')


mainframe = ttk.Frame(root, padding="12 12 12 12",style='My.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#mainframe.columnconfigure(0, weight=2)
#mainframe.rowconfigure(0, weight=2)
mainframe['borderwidth'] = 2
mainframe['relief'] = 'sunken'


ttk.Button(mainframe, text = "Open File" ,command = openFile).grid(column = 0,row = 2,columnspan=3,  padx = 3, pady = 3)

root.protocol("WM_DELETE_WINDOW", win_deleted)


root.mainloop()
