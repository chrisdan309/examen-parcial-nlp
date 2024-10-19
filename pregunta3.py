
def read_lines(n):
    corpus = []

    with open('./corpus/eswiki-latest-pages-articles.txt') as f:
        for i in range(n):
            line = f.readline()
            corpus.append(line.lower())
    return corpus

def tokenize(corpus):
    import re
    tokens = []
    for line in corpus:
        tokens += re.findall(r'\b[a-zA-Z|\ñ]+\b', line)
    #tokens = list(set(tokens))
    return tokens

def lematizacion(tokens):
    new_tokens = []
    for token in tokens:
        if token.endswith('ces'):
            new_tokens.append(token[:-3])

        if token.endswith('s') or token.endswith('es'):
            new_tokens.append(token[:-1])
        else:
            new_tokens.append(token)
    return new_tokens

def remove_stopwords(tokens):
    stopwords = ['a','y','de','la','el','con','un','como','que','por','en','o','del',
                 'lo','para','ha','lo','se','al','e','una','su','entre','','m','n','desde'
                 ,'i','pero','no','ya','sobre','si']
 
    new_tokens = []
    for token in tokens:
        if token not in stopwords:
            new_tokens.append(token)
    return new_tokens

def filter_tokens(tokens, n):
    new_tokens = []
    
    token_counts = {}
    for token in tokens:
        if token in token_counts:
            token_counts[token] += 1
        else:
            token_counts[token] = 1
    # print(token_counts)
    for token in tokens:
        if token_counts[token] > n:
            new_tokens.append(token)
    return new_tokens

def preprocessing(corpus, n):
    tokens = tokenize(corpus)
    tokens = lematizacion(tokens)
    # print(tokens)
    tokens = remove_stopwords(tokens)
    # print(tokens)
    tokens = filter_tokens(tokens, n)
    return tokens


if __name__ == "__main__":
    corpus = read_lines(200)
    tokens = preprocessing(corpus, 5)
    print(set(tokens))

