import re

def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens

# 1. Add 15 positive and 15 negative to your expand the knowledge base

positive_words = {
    'happy',
    'good',
    'joyful',
    'excited',
    'amazing',
    'fantastic',
    'cheerful',
    'delightful',
    'grateful',
    'loved',
    'hopeful',
    'inspired',
    'brilliant',
    'pleasant',
    'kind'
}
negative_words = {
   'sad',
    'bad',
    'angry',
    'upset',
    'terrible',
    'horrible',
    'depressed',
    'worried',
    'frustrated',
    'hurt',
    'miserable',
    'lonely',
    'disappointed',
    'annoyed',
    'mean'
}

# 2. print positive lexicon & negative lexicon:
print("Positive lexicon:", positive_words)
print("Negative lexicon:", negative_words)

# --- Interactive Sentiment Testing ---
print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Goodbye!")
        break

    tokens = clean_text(text)
    pos_count = sum(1 for t in tokens if t in positive_words)
    neg_count = sum(1 for t in tokens if t in negative_words)
    total = len(tokens)

# 3. Compute simple sentiment score (hint: positive - negative count)

    score = pos_count - neg_count

    # Determine sentiment label
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

# 4. print the output results
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")

# 5. Add a short reflection as comments at the bottom (2–3 sentences)
# This lexicon based sentiment analysis method is simple and easy to implement.
# It is useful for basic text analysis tasks, but it may not capture complex tasks.
