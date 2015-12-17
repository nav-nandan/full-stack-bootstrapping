#!/usr/bin/env python

import sys
import getopt
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import cross_validation
from sklearn import svm
from sklearn import metrics
import numpy as np
from scipy import sparse
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier


def multilabel_classification (training_instances, labels, test_instances = []):
    X_train = []
    X_test = test_instances
    y_train = []
    y_test = []

    if X_test == []:
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(training_instances, labels, test_size=0.4, random_state=0)
    else:
	   X_train, y_train = training_instances, labels

    classifier = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train, y_train)
    y_predicted = predict_multilabel(classifier, X_test)
    return y_predicted


def predict_multilabel (classifier, test_instances):
    target_names = ['funny', 'useful', 'cool']
    y_predicted = classifier.predict(test_instances)
    target_labels = []
    
    for item, labels in zip(test_instances, y_predicted):
        target_labels.append(', '.join(target_names[x] for x in labels))

    return target_labels


def get_score (gold_labels, predicted_labels):
    print metrics.classification_report(gold_labels, predicted_labels)


def predict (classifier, test_feature_index):
    y_predicted = classifier.predict(test_feature_index)
    return y_predicted


def train_classifier (feature_index, labels, split='true'):
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    
    if split == 'true':
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(feature_index, labels, test_size=0.4, random_state=0)
    else:
        X_train, y_train = feature_index, labels

    classifier = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

    if X_test == [] and y_test == []:
        return classifier
    else:
        y_predicted = predict(classifier, X_test)
        get_score(y_test, y_predicted)


def ngram_feature_extraction (training_instances, training_labels=[], test_instances=[]):
    ngram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\S+', min_df=1, binary=True)
    training_feature_index = np.array([])
    test_feature_index = np.array([])

    if len(test_instances) > 0:
        training_feature_index = ngram_vectorizer.fit_transform(training_instances, training_labels)
        test_feature_index = ngram_vectorizer.transform(test_instances)
    else:
        training_feature_index = ngram_vectorizer.fit_transform(training_instances, training_labels)

    return training_feature_index, test_feature_index


def combine_feature_index (feature_list):
    training_feature_index = []

    for index, feature in enumerate(feature_list):
        if index == 0:
            training_feature_index = feature.toarray()
        else:
            training_feature_index = np.hstack((training_feature_index, feature.toarray()))
            
    return sparse.csc_matrix(training_feature_index)


def parse_input_data (input_data):
    reviews = []
    sentiment_labels = []
    category_labels = []

    for review in input_data:
        if len(review) > 0:
            parsed_review = json.loads(review)
            text = ' '.join(parsed_review['text'].split('\n'))
            
            if parsed_review['stars'] > 3 :
                stars = 'positive'
            elif parsed_review['stars'] == 3:
                stars = 'neutral'
            else:
                stars = 'negative'

            category_label = []
            
            if parsed_review['votes']['funny'] > 0:
                category_label.append(0)
            if parsed_review['votes']['useful'] > 0:
                category_label.append(1)
            if parsed_review['votes']['cool'] > 0:
                category_label.append(2)

        reviews.append(text)
        sentiment_labels.append(stars)
        category_labels.append(category_label)

    return reviews, sentiment_labels, category_labels


if __name__== "__main__":
    opts, args = getopt.getopt(sys.argv[1:], '')

    input_data = open(args[0]).read().split('\n')

    reviews = []
    sentiment_labels = []
    category_labels = []
    test_instances = []

    if len(args) > 1:
        limit_training_set = int(args[1])
        reviews, sentiment_labels, category_labels = parse_input_data(input_data[0:limit_training_set])

        if len(args) == 2:
            training_feature_index, test_feature_index = ngram_feature_extraction(reviews, sentiment_labels)
            sentiment_classifier = train_classifier(training_feature_index, sentiment_labels)

        if len(args) > 2:
            test_instances = open(args[2]).read().split('\n')
            test_reviews, gold_sentiment_labels, gold_category_labels = parse_input_data(test_instances)
            target_names = ['funny', 'useful', 'cool']
            gold_categories = []

            for labels in gold_category_labels:
                gold_categories.append(', '.join(target_names[x] for x in labels))
            
            training_feature_index, test_feature_index = ngram_feature_extraction(reviews, sentiment_labels, test_instances)
            sentiment_classifier = train_classifier(training_feature_index, sentiment_labels, 'false')
            predicted_sentiment = predict(sentiment_classifier, test_feature_index)
            predicted_categories = multilabel_classification(training_feature_index, category_labels, test_feature_index)
            print 'actual sentiment : ', gold_sentiment_labels
            print 'predicted sentiment : ', predicted_sentiment[0:len(predicted_sentiment)-1]
            print 'actual categories : ', gold_categories
            print 'predicted categories : ', predicted_categories[0:len(predicted_categories)-1]
