import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

# Sample text for NLP
text = "KP Oli, the Prime Minister of Nepal, gave a speech in Kathmandu last Tuesday. It was a rainy day."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

# Part of Speech (POS) Tagging
pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)

# Named Entity Recognition (NER)
named_entities = ne_chunk(pos_tags)
print("Named Entities:", named_entities)

# Removing stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words (without stopwords):", filtered_words)
