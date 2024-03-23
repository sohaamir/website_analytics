# pip install spacy
# python -m spacy download en_core_web_sm

import json
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Define your list of scientific words - asked ChatGPT to generate a list of scientific words from the .json file
scientific_words = set([
    "neuroscience", "psychiatry", "psychology", "programming", "mental", "learning", 
    "disorders", "cognitive", "computational", "behavioral", "neurocomputational", 
    "modelling", "neuroimaging", "decision", "therapy", "biomedical", "modelling", 
    "cognitive", "therapy", "neurotransmitters", "neuroethics", "neurodynamics", 
    "phd", "research", "academic", "university", "brain", "health", "science", 
    "imaging", "mri", "fmri", "spectroscopy", "behavior", "neural", "neurons", 
    "neurological", "physiological", "psychopharmacology", "haemodynamic", 
    "neurocognitive", "metacognitive", "diagnosis", "psychopathology", "neurotransmitters"
])  # Extend this list based on further detailed analysis or specific context of your project.


# Load words from the original JSON file
with open('../data/words.json') as f:
    word_counts = json.load(f)

# Initialize containers for scientific words and names
scientific = {}
names = {}

for word, count in word_counts.items():
    # Check if the word is in the predefined list of scientific words
    if word in scientific_words:
        scientific[word] = count
        continue
    
    # Use spaCy's NER to check if the word is a name
    doc = nlp(word)
    for ent in doc.ents:
        if ent.label_ in ["PERSON"]:
            names[word] = count
            break
    else:  # The word is not recognized as a name
        continue

# Write scientific words to a new JSON file
with open('../data/scientific_words.json', 'w') as f:
    json.dump(scientific, f, indent=4)

# Write names to another new JSON file
with open('../data/names.json', 'w') as f:
    json.dump(names, f, indent=4)