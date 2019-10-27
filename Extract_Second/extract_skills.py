import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams

tokenizer = RegexpTokenizer(r'\w+')

textfile_path= r"C:\Users\Yiyang Zhou\Dropbox\summer intern 2017\keywords.txt"
keywords_file = open(textfile_path).read()
keywords_sample = "python\nvb\nc++"
keywords_sample2 = "big data\nmachine learning\ndata mining"


sentence = "I know python and vb. I also know big data, data mining and machine learning."
sentence_token = tokenizer.tokenize(sentence) 

textfile_path2 = r"C:\Users\Yiyang Zhou\Dropbox\summer intern 2017\Yiyang (Eric) Zhou Resume 2017 Fall.txt"
resume_file = open(textfile_path2).read()
resume_token = tokenizer.tokenize(resume_file)  


def remove_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return content
    print (content)
    
filtered_sentence = remove_stopwords(sentence_token)
filtered_resume = remove_stopwords(resume_token)
print (filtered_sentence)
print (filtered_resume)

"""the code to get bigrams:"""
def get_bigrams(input):
    n = 2
    result = []
    bigrams = ngrams(input, n)
    for grams in bigrams:
        x = "%s %s" % grams
        result.append(x)
    return (result)    
    print (result)

y = get_bigrams(sentence_token)
y2 = get_bigrams(resume_token)

"""the code to get threegrams:"""
def get_threegrams(input):
    n = 3
    result = []
    threegrams = ngrams(input, n)
    for grams in threegrams:
        x = "%s %s %s" % grams
        result.append(x)
    return (result)    
    print (result)

z = get_threegrams(sentence_token)


def extract_skills(a,b):
    count=0
    skills=[]
    for x in a:
        if x.lower() in b.lower():
            skills.append(x)
            count+=1
    return (skills,count)
    print (skills,count)


"""We can do some proprocessing such as stemming and removing punctuation to 
avaoid the result showing irrelevant infor such as 'and' and '.'."""
    
print (extract_skills(filtered_sentence, keywords_file))  #works well for extracting single term skills in a simple string
print (extract_skills(y, keywords_sample2))     #working fine
print (extract_skills(filtered_resume, keywords_file))    #need improvement, does not work very well 
print (extract_skills(y2, keywords_sample2))    #working well for bigrams
skill_match = set(tokenizer.tokenize(keywords_file.lower())).intersection(set(tokenizer.tokenize(resume_file.lower())))
print (skill_match)   #work very well for single term skills



"""some idea and testing"""

#this is a great example for term matching without iteration. 
checklist = ['A', 'FOO']
words = ['fAr', 'near', 'A']
matches = set(checklist).intersection(set(words))
print(matches)  # {'A'}

"""The code to get bigrams:"""
"""
def get_bigrams(myString):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(myString)
    stemmer = PorterStemmer()
    bigram_finder = BigramCollocationFinder.from_words(tokens)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)

    for bigram_tuple in bigrams:
        x = "%s %s" % bigram_tuple
        tokens.append(x)

    result = [' '.join([stemmer.stem(w).lower() for w in x.split()]) for x in tokens if x.lower() not in stopwords.words('english') and len(x) > 7]
    return result

x = get_bigrams(sentence)
print (x)
"""






