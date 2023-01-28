from flask import request, jsonify
from chat.api import api_bp
import pickle
import re


class TextSpamClassifier():

    def __init__(self) -> None:
        with open('notebooks/spam_filter/model_spam.pickle', 'rb') as handle:
            self.model = pickle.load(handle)
        with open('notebooks/spam_filter/vectorizer_spam.pickle',
                  'rb') as handle:
            self.vectorizer = pickle.load(handle)

    def __preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        text = text.strip()
        text = text.split()
        text = ' '.join(list(filter(lambda x: x not in ['', ' '], text)))
        return text

    def predict_proba(self, X):
        val = self.__preprocess_text(X)
        val = self.vectorizer.transform([val])
        prob = self.model.predict_proba(val)[0][1]
        return prob


class TextProfanityClassifier():

    def __init__(self) -> None:
        with open('notebooks/profanity_filter/model_profanity.pickle',
                  'rb') as handle:
            self.model = pickle.load(handle)
        with open('notebooks/profanity_filter/vectorizer_profanity.pickle',
                  'rb') as handle:
            self.vectorizer = pickle.load(handle)

    def __preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        text = text.strip()
        text = text.split()
        text = ' '.join(list(filter(lambda x: x not in ['', ' '], text)))
        return text

    def predict_proba(self, X):
        val = self.__preprocess_text(X)
        val = self.vectorizer.transform([val])
        prob = self.model.predict(val)[0]
        return prob


@api_bp.route('/text-validate', methods=['POST'])
def text_chat_validate():
    message = request.form.get('message')
    tsc = TextSpamClassifier()
    tpc = TextProfanityClassifier()
    spam_text = "Not a spam!"
    prof_text = "No profane!"
    if tpc.predict_proba(message) != 0:
        prof_text = "Highly profane!"
    if tsc.predict_proba(message) > 0.8:
        spam_text = "Highly spam!"
    elif tsc.predict_proba(message) > 0.6:
        spam_text = "Slightly spam!"
    elif tsc.predict_proba(message) > 0.4:
        spam_text = "Less spam!"
    elif tsc.predict_proba(message) > 0.2:
        spam_text = "I don't think spam!"

    prof_prob = tpc.predict_proba(message)
    if prof_prob > 0.5:
        prof_text = "Profane text!"

    return jsonify({
        "success": True,
        "message": "Chat validation done!",
        "data": {
            "spam_text": f"{spam_text}",
            "prof_text": f"{prof_text}",
        },
    })
