import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('trainingSkills.txt', sep='|', names=['Category', 'Input'])
# df.head() to print first 4 lines of our data

# Now, we change the category names (s for skill and e for education) into numbers
df.loc[df["Category"] == 's', "Category",] = 0
df.loc[df["Category"] == 'e', "Category",] = 1
# print(df)

# TESTING SOME STUFF HERE
# df_y=df["Category"]
# df_x=df["Input"]
#
# x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0)

y_train = df["Category"]
x_train = df["Input"]

# print(x_train)
# print(y_train)

cv = CountVectorizer()

x_trainCV = cv.fit_transform(x_train)
a = x_trainCV.toarray()

#print(a[0])
#print(cv.inverse_transform(a[0]))

nb = MultinomialNB()
y_train = y_train.astype('int')
nb.fit(x_trainCV,y_train)

df2 = pd.read_csv('toTest.txt')
x_testCV = cv.transform(df2)

prediction = nb.predict(x_testCV)
my_input = df2.to_csv()
my_str = my_input[1:]
my_str = my_str.replace('\n','')
if prediction[0]==0:
    print(my_str+" is part of SKILLS")
else:
    print(my_str+" is part of EDUCATION")
