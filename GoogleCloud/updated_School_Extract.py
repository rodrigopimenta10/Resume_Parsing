def extract_university_two(resume):
    #Copy script
    return finalListSchools = ['University of Maryland']

def extract_School(resume):
    resume_file = resume
    resume_file2 = resume_file.lower()
    major_df = pandas.read_excel(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..','www','Parsing','majors.xlsx')))
    major_df.columns
    major_file = major_df['Majors'].values
    major_lower = [item.lower() for item in major_file]
    tokenizer = RegexpTokenizer(r'\w+')
    resume_token = tokenizer.tokenize(resume_file)
    resume_token2 = tokenizer.tokenize(resume_file2)
    major_distinct = []
    dictionary = {'Name': 5}
    regular_expression = re.compile(r"/BA|BS|B\.S|Bachelor of Science|Bachelor of Arts|BBA |B/A|Bachelor of Business Administration/", re.IGNORECASE)
    bach_major_result = re.search(regular_expression, resume_file)
    regular_expression_two = re.compile(r"minor|Minor", re.IGNORECASE)
    minor_result = re.search(regular_expression_two, resume_file)
    regular_expression_three = re.compile(r"Master|master", re.IGNORECASE)
    master_major_result = re.search(regular_expression_three, resume_file)
    regular_expression_four = re.compile(r"university", re.IGNORECASE)
    university_major_result = re.search(regular_expression_four, resume_file)
    updated_majors1 = []
    indexes_majors1 = []
    updated_majors2 = []
    indexes_majors2 = []
    updated_majors3 = []
    indexes_majors3 = []
    updated_majors4 = []
    indexes_majors4 = []

    university_df1 = pandas.read_excel(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..','www','Parsing','China_University.xlsx')))
    university_df2 = pandas.read_excel(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..','www','Parsing','India_University.xlsx')))
    university_df3 = pandas.read_excel(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..','www','Parsing','US_University.xlsx')))
    university_file1 = university_df1['Universities'].values
    university_file2 = university_df2['Universities'].values
    university_file3 = university_df3['Universities'].values
    university_lower1 = [item.lower() for item in university_file1]
    university_lower2 = [item.lower() for item in university_file2]
    university_lower3 = [item.lower() for item in university_file3]
    university_combined = university_lower1 + university_lower2 + university_lower3

    get_majors(resume_token2, major_lower)
    get_majors2(resume_token2, major_lower,major_distinct)
    get_majors_index(major_distinct,resume_file2,dictionary)
    get_bach_index(bach_major_result,resume_file)
    get_minor_index(minor_result,resume_file)
    get_master_index(master_major_result,resume_file)
    get_university_index(university_major_result,resume_file)
    print('BACH: ',get_bach_major(dictionary,resume_file,bach_major_result,updated_majors1,indexes_majors1))
    print('MASTER: ',get_master_major(dictionary,resume_file,master_major_result,updated_majors2,indexes_majors2))
    print('MINOR: ',get_minor(dictionary,resume_file,minor_result,updated_majors3,indexes_majors3))
    print('What is this: ',get_university_major(dictionary,resume_file,university_major_result,updated_majors4,indexes_majors4))

    #print('UNI: ',extract_university(resume_token2,university_combined))
    print('UNI: ',extract_university2(resume)

    print('GPA: ',extract_GPA(resume_file))
    schools = []
    school = {}
    school_info = {}
    major_info = {}

    #school_info['name'] = extract_university(resume_token2,university_combined)
    school_info['name'] = extract_university(resume)

    school_info['degreeLevel'] = 'Undergraduate'
    school['school'] = school_info
    school['gradDate'] = 'Jan 2012'
    GPA = extract_GPA(resume_file)
    if GPA != None:
        school['GPA'] = GPA
    else:
        school['GPA'] = 0

    major_info['major'] = get_university_major(dictionary,resume_file,university_major_result,updated_majors4,indexes_majors4)
    major_info['dept'] = '?'
    major_info['major/minor'] = 'Major'
    school['major'] = major_info
    schools.append(school)
    print('SCHOOL:  ',schools)

    return schools
#major, University, gpa
def get_bigrams(input):
    n = 2
    result = []
    bigrams = ngrams(input, n)
    for grams in bigrams:
        x = "%s %s" % grams
        result.append(x)
    return (result)


def get_threegrams(input):
    n = 3
    result = []
    threegrams = ngrams(input, n)
    for grams in threegrams:
        x = "%s %s %s" % grams
        result.append(x)
    return (result)

def get_fourgrams(input):
    n = 4
    result = []
    fourgrams = ngrams(input, n)
    for grams in fourgrams:
        x = "%s %s %s %s" % grams
        result.append(x)
    return (result)

def get_fivegrams(input):
    n = 5
    result = []
    fivegrams = ngrams(input, n)
    for grams in fivegrams:
        x = "%s %s %s %s %s" % grams
        result.append(x)
    return (result)

def get_sixgrams(input):
    n = 6
    result = []
    sixgrams = ngrams(input, n)
    for grams in sixgrams:
        x = "%s %s %s %s %s %s" % grams
        result.append(x)
    return (result)

def get_majors(a,b):
    majors=[]
    for x in a:
        if x in b:
            majors.append(x)
    return (majors)

def get_majors2(a,b,major_distinct):
    unigram_major = get_majors(a, b)
    bigram_major = get_majors(get_bigrams(a), b)
    threegram_major = get_majors(get_threegrams(a), b)
    combined_majors_list = unigram_major + bigram_major + threegram_major
    for i in combined_majors_list:
        if i not in major_distinct:
            major_distinct.append(i)
    return(major_distinct)

def get_majors_index(major_distinct,resume_file2,dictionary):
    for i, element in enumerate(major_distinct):
        x = resume_file2.find(element)
        dictionary[element] = x
    del dictionary['Name']
    return dictionary

def get_bach_index(bach_major_result,resume_file):
    if bach_major_result:
        bach_major_result = bach_major_result.group()
    if bach_major_result is not None:
        bach_major_index = resume_file.find(bach_major_result)
        return(bach_major_index)
    else:
        return 0

def get_minor_index(minor_result,resume_file):
   if minor_result:
       minor_result = minor_result.group()
   if minor_result is not None:
       minor_index = resume_file.find(minor_result)
   else:
       minor_index = 0
   return(minor_index)

def get_master_index(master_major_result,resume_file):
    if master_major_result:
        master_major_result = master_major_result.group()
    if master_major_result is not None:
        master_major_index = resume_file.find(master_major_result)
        return(master_major_index)
    else:
        return 0

def get_university_index(university_major_result,resume_file):
    if university_major_result:
        university_major_result = university_major_result.group()
    if university_major_result is not None:
        university_major_index = resume_file.find(university_major_result)
        return(university_major_index)
    else:
        return 0

def get_bach_major(dictionary,resume_file,bach_major_result,updated_majors1,indexes_majors1):
    bach_major_index = get_bach_index(bach_major_result,resume_file) - 100
    upper_bound = bach_major_index + 100
    for k, v in dictionary.items():
        if (bach_major_index < v < upper_bound):
            updated_majors1.append(k)
            indexes_majors1.append(v)
    return updated_majors1

def get_master_major(dictionary,resume_file,master_major_result,updated_majors2,indexes_majors2):
    master_major_index = get_master_index(master_major_result,resume_file)
    if master_major_index == 0:
        return []
    upper_bound = master_major_index +100
    for k, v in dictionary.items():
        if (master_major_index < v < upper_bound):
            updated_majors2.append(k)
            indexes_majors2.append(v)
    return updated_majors2
def get_minor(dictionary,resume_file,minor_result,updated_majors3,indexes_majors3):
    minor_index = get_minor_index(minor_result,resume_file)
    upper_bound = minor_index +100
    for k, v in dictionary.items():
        if (minor_index < v < upper_bound):
            updated_majors3.append(k)
            indexes_majors3.append(v)
    return updated_majors3

def get_university_major(dictionary,resume_file,university_major_result,updated_majors4,indexes_majors4):
    university_major_index = get_university_index(university_major_result,resume_file)
    if university_major_index == 0:
        return []
    upper_bound = university_major_index +100
    for k, v in dictionary.items():
        if (university_major_index < v < upper_bound):
            updated_majors4.append(k)
            indexes_majors4.append(v)
    return updated_majors4



def extract_major(majors_minors_all):
    majors_minors_all = updated_majors1 + updated_majors2 + updated_majors3 + updated_majors4
    majors_minors_final_list = list(dedupe(majors_minors_all))
    return (majors_minors_final_list)


#extract University:
def get_university(a,b):
    resume_university=[]
    for x in a:
        if x in b:
            resume_university.append(x)
    return (resume_university)

def extract_university(resume_token_lower,university_combined):
    unigram_university = get_university(resume_token_lower, university_combined)
    bigram_university = get_university(get_bigrams(resume_token_lower), university_combined)
    threegram_university = get_university(get_threegrams(resume_token_lower), university_combined)
    fourgram_university = get_university(get_fourgrams(resume_token_lower), university_combined)
    fivegram_university = get_university(get_fivegrams(resume_token_lower), university_combined)
    sixgram_university = get_university(get_sixgrams(resume_token_lower), university_combined)
    combined_university_extraction = list(bigram_university + threegram_university + fourgram_university + fivegram_university + sixgram_university)
    print('UNI: ', bigram_university,threegram_university,fourgram_university)
    return combined_university_extraction

#execution of extracting university:

#extract GPA:
def extract_GPA(resume):
    result = re.search(r'(GPA|gpa):( ?\d.\d{1,})',resume)
    if result:
        result = result.group(2)
        result = float(result)
    return (result)