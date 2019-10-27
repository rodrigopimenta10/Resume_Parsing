import re

#extract name
textfile_path2 = r"C:\Users\Yiyang Zhou\Dropbox\summer intern 2017\Yiyang (Eric) Zhou Resume 2017 Fall.txt"
resume_file = open(textfile_path2).read()

def extract_first_name(resume):
    name = resume.split('\n', 1)[0]
    first_name = name.split(' ', 1)[0]
    return (first_name)
    print (first_name)
    
def extract_last_name(resume):
    name = resume.split('\n', 1)[0]
    last_name = name.split(' ', 1)[-1]
    return (last_name)
    print (last_name)

extract_first_name(resume_file)
extract_last_name(resume_file)


