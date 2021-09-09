#!/bin/bash/python3

import json, random, pickle
import numpy as np
from keras.models import load_model
from TextProcessor import ProcessText

class IntentModel():
    model = load_model('language_model0.h5')
    intents = json.loads(open('jsonIntents.json').read())
    words = pickle.load(open('listWords.pkl','rb'))
    classes = pickle.load(open('listClasses.pkl','rb'))

    proctext = ProcessText()

    def bow(self, sentence, words, show_details=True):
        # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

        # tokenize the pattern
        sentence = self.proctext.clean_up_sentence(sentence)
        sentence_words = self.proctext.n_gram_split(sentence, n=2, string_mode=False, keep_original=True)
        print(sentence_words)

        # bag of words - matrix of N words, vocabulary matrix
        bag = [0]*len(words)
        firstbag = bag
        for s in sentence_words:
            print(s)
            for i,w in enumerate(words):
                # print(w)
                if w == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        print(firstbag)
        print(bag)
        return(np.array(bag))

    def predict_class(self, sentence, model):

        print("Checkpoint 1")
        print(sentence)
        p = self.bow(sentence, self.words,show_details=True)
        print("Checkpoint 2")
        res = model.predict(np.array([p]))[0]
        print(res)
        print("Checkpoint 3")
        # filter out predictions below a threshold
        ERROR_THRESHOLD = 0.25
        # ERROR_THRESHOLD = 0.10
        print("Checkpoint 4")
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        print(results)
        print("Checkpoint 5")
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        print("Checkpoint 6")
        return_list = []
        print("Checkpoint 7")
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        print("Checkpoint 8")
        return return_list

    def get_response(self, ints, intents_json):
        print("Checkpoint 9")
        print(ints)
        if ints != []:
            print("Checkpoint 10")
            print(ints[0])
            print("Checkpoint 11")
            print(ints[0]['intent'])
            print("Checkpoint 12")
            tag = ints[0]['intent']
            print("Checkpoint 13")
            list_of_intents = intents_json['intents']
            for i in list_of_intents:
                if(i['tag']== tag):
                    result = random.choice(i['responses'])
                    break
        else: 
            result = "I'm sorry I didn't understand that!"
        return result
