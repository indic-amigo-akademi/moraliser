import pickle
import re


class TextSpamClassifier:
    def __init__(self) -> None:
        with open("notebooks/spam_filter/model_spam.pickle", "rb") as handle:
            self.model = pickle.load(handle)
        with open("notebooks/spam_filter/vectorizer_spam.pickle", "rb") as handle:
            self.vectorizer = pickle.load(handle)

    def __preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        text = text.strip()
        text = text.split()
        text = " ".join(list(filter(lambda x: x not in ["", " "], text)))
        return text

    def predict_proba(self, X):
        val = self.__preprocess_text(X)
        val = self.vectorizer.transform([val])
        prob = self.model.predict_proba(val)[0][1]
        return prob


class TextProfanityClassifier:
    def __init__(self) -> None:
        with open("notebooks/profanity_filter/model_profanity.pickle", "rb") as handle:
            self.model = pickle.load(handle)
        with open(
            "notebooks/profanity_filter/vectorizer_profanity.pickle", "rb"
        ) as handle:
            self.vectorizer = pickle.load(handle)

    def __preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        text = text.strip()
        text = text.split()
        text = " ".join(list(filter(lambda x: x not in ["", " "], text)))
        return text

    def predict_proba(self, X):
        val = self.__preprocess_text(X)
        val = self.vectorizer.transform([val])
        prob = self.model.predict(val)[0]
        return prob
