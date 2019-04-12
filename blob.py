# -*- coding: utf-8 -*-
import json
from textblob.classifiers import NaiveBayesClassifier
import pickle

training_set = open("train.json", "r", encoding="utf-8")
testing_set = open("test.json", "r", encoding="utf-8")

cl = NaiveBayesClassifier(training_set, format="json")
print(cl.accuracy(testing_set, format="json"))
pickle_file = open('news.obj','wb')
pickle.dump(cl, pickle_file)
pickle_file.close()

training_set.close()
testing_set.close()
