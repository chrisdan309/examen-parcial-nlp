# Código inspirado en Modelos-lenguaje2.ipynb

def tokenize(text):
    return text.split()

class bigram():
    corpus = None
    vocab = None
    bigram_count = {}
    unigram_count = {}
    frequency_unigram_count = {}
    def __init__(self, corpus:list, vocab: list):
        self.corpus = corpus
        self.vocab = vocab
        for word in vocab:
            cont = 0
            for sentence in corpus:
                sentence_token = tokenize(sentence)
                if word in sentence_token:
                    cont += 1

            self.unigram_count[word] = cont
        
        for sentence in corpus:
            sentence_token = tokenize(sentence)
            for word in sentence_token:
                if word not in self.vocab:
                    if '<UNK>' not in self.vocab:
                        self.vocab.append('<UNK>')
                        self.unigram_count['<UNK>'] = 1
                    else:
                        self.unigram_count['<UNK>'] += 1

        self.unigram_count["<s>"] = len(corpus)
        self.unigram_count["</s>"] = len(corpus)

    def train(self):
        for sentence in corpus:
            sentence_token = tokenize(sentence)

            if ('<s>',sentence_token[0]) not in self.bigram_count.keys():
                    self.bigram_count[('<s>',sentence_token[0])] = 1
            else:
                self.bigram_count[('<s>',sentence_token[0])] += 1
            
            for i in range(len(sentence_token)-1):
                word_1 = sentence_token[i]
                word_2 = sentence_token[i+1]
                if (word_1, word_2) not in self.bigram_count.keys():
                    self.bigram_count[(word_1, word_2)] = 1
                else:
                    self.bigram_count[(word_1, word_2)] += 1

            if (sentence_token[-1],'</s>') not in self.bigram_count.keys():
                self.bigram_count[(sentence_token[-1],'</s>')] = 1
            else:
                self.bigram_count[(sentence_token[-1],'</s>')] += 1

    def good_turing(self):
        self.frequency_unigram_count[0] = 1
        unigramas = []
        for value in self.unigram_count.values():
            unigramas.append(value)

        unigramas = sorted(list(set(unigramas)))
        for key in unigramas:
            count = 0
            for value in self.unigram_count.values():
                if key == value:
                    count += 1
            self.frequency_unigram_count[key] = count

if __name__ == "__main__":    
    corpus = ["all models are wrong",
                "a model is wrong",
                "some models are useful"]

    vocab = ['<s>','</s>','a','all','are','model','models','some','useful','wrong']
    print("Corpus")
    print(corpus)
    bigrama = bigram(corpus, vocab)
    bigrama.train()
    print("\nunigramas:")
    print(bigrama.unigram_count)
    
    bigrama.good_turing()
    print("\nGood-Turing")
    print(bigrama.frequency_unigram_count)