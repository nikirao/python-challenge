import os
import csv
import string
import re

paragraph_path=os.path.join('.','paragraph_1.txt')

def parse_text(file_path):

    #function to read the file and return sentence and word counts

    with open(file_path,'r') as text_reader:
        text=text_reader.read()
        word_count=text.split()
        sentence_count=re.split("(?<=[.!?]) +",text)
        combine_list=[word_count, sentence_count]
        return combine_list

#initializing count objects
letter_count=[]
words_in_sentences_count=[]

#Calling function to parse text
paragraph_list=parse_text(paragraph_path)

#counting letters in words
for word in paragraph_list[0]:
    letter_count.append(len(word))

#counting words in sentences
for sentence in paragraph_list[1]:
    words_in_sentences=sentence.split()
    words_in_sentences_count.append(len(words_in_sentences))


print("Paragraph Analysis")
print("--------------------------------")
print("Approximate word count: "+str(len(paragraph_list[0])))
print("Approximate sentence count: "+str(len(paragraph_list[1])))
print("Approximate letter count per word: "+str(sum(letter_count)/len(paragraph_list[0])))
print("Approximate sentence length in words: "+str(sum(words_in_sentences_count)/len(paragraph_list[1])))
