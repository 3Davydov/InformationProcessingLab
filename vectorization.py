from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import spacy
from sklearn.preprocessing import normalize

# Загрузка стоп-слов и пунктуации
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('russian'))
punctuation = set(string.punctuation)

def delete_trash_words(text):
    words = word_tokenize(text.lower())  # Привести к нижнему регистру и токенизировать
    filtered_words = [word for word in words if word not in stop_words and word not in punctuation]
    return " ".join(filtered_words)

def lemmatize(text, nlp):
    doc = nlp(text.lower())  # Привести к нижнему регистру и лемматизировать
    lemmatized_words = [token.lemma_ for token in doc if token.text not in punctuation and token.text not in stop_words]
    return " ".join(lemmatized_words)

def vectorize(documents):
    # Удаление предлогов и пунктуации
    preprocessed_documents = [ delete_trash_words(doc) for doc in documents ]

    nlp = spacy.load("ru_core_news_sm")
    preprocessed_documents = [ lemmatize(doc, nlp) for doc in preprocessed_documents ]

    # Создание объекта TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Применение TF-IDF к текстовым данным
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_documents)
    # Нормализация матрицы TF-IDF по длине документа
    tfidf_matrix = normalize(tfidf_matrix, norm='l2', axis=1)
   
    words = tfidf_vectorizer.get_feature_names_out()
    doc_names = ['Документ {}'.format(i+1) for i in range(len(preprocessed_documents))]
    return tfidf_matrix, words, doc_names
