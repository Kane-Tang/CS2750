import csv
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def csv_to_lists(path_filename):
    InputStoryid = []
    InputSentence1 = []
    InputSentence2 = []
    InputSentence3 = []
    InputSentence4 = []
    RandomFifthSentenceQuiz1 = []
    RandomFifthSentenceQuiz2 = []
    AnswerRightEnding = []
    with open(path_filename, 'r', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            InputStoryid.append(row['InputStoryid'])
            InputSentence1.append(row['InputSentence1'])
            InputSentence2.append(row['InputSentence2'])
            InputSentence3.append(row['InputSentence3'])
            InputSentence4.append(row['InputSentence4'])
            RandomFifthSentenceQuiz1.append(row['RandomFifthSentenceQuiz1'])
            RandomFifthSentenceQuiz2.append(row['RandomFifthSentenceQuiz2'])
            AnswerRightEnding.append(row['AnswerRightEnding'])
    return InputStoryid, InputSentence1, InputSentence2, InputSentence3, InputSentence4, RandomFifthSentenceQuiz1, RandomFifthSentenceQuiz2, AnswerRightEnding

def test_csv_to_lists(path_filename):
    InputStoryid = []
    InputSentence1 = []
    InputSentence2 = []
    InputSentence3 = []
    InputSentence4 = []
    RandomFifthSentenceQuiz1 = []
    RandomFifthSentenceQuiz2 = []
    with open(path_filename, 'r', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            InputStoryid.append(row['InputStoryid'])
            InputSentence1.append(row['InputSentence1'])
            InputSentence2.append(row['InputSentence2'])
            InputSentence3.append(row['InputSentence3'])
            InputSentence4.append(row['InputSentence4'])
            RandomFifthSentenceQuiz1.append(row['RandomFifthSentenceQuiz1'])
            RandomFifthSentenceQuiz2.append(row['RandomFifthSentenceQuiz2'])
    return InputStoryid, InputSentence1, InputSentence2, InputSentence3, InputSentence4, RandomFifthSentenceQuiz1, RandomFifthSentenceQuiz2

data_ids, data_s1, data_s2, data_s3, data_s4, data_q1, data_q2, data_ans = csv_to_lists('Supporting Materials/ROC-Story-Cloze-Data.csv')
val_ids, val_s1, val_s2, val_s3, val_s4, val_q1, val_q2, val_ans = csv_to_lists('Supporting Materials/ROC-Story-Cloze-Val.csv')
test_ids, test_s1, test_s2, test_s3, test_s4, test_q1, test_q2 = test_csv_to_lists('Supporting Materials/ROC-Story-Cloze-Test-Release.csv')

def sentence_to_words(sentence,stop_w):
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w in stop_w]
    return filtered_sentence

stop_words = set(stopwords.words('english'))
words = sentence_to_words(data_s1[0], stop_words)