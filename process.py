from data import People

class Process():

    data = People.read()

    @staticmethod
    def _max_len(data):

        """
        Returns he length of the longest name

        """
        return data['name'].str.len().max()

    @staticmethod
    def _all_chars(data):

        """

        Returns all characters in dataset

        """

        names = data['name']

        s = set()
        for name in names:
            s |= set(str(name))

        return sorted(s)

    @staticmethod
    def _create_dicts(all_chars_sorted):

        char_indices = {}
        indices_char = {}

        for i, c in enumerate(all_chars_sorted):
            char_indices[c] = i
            indices_char[i] = c

        return char_indices, indices_char

    @staticmethod
    def _vectorize(clean_data, vocab, max_word_len):
        X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
        y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                X[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1

        # Reserve 0 for masking via pad_sequences

        vocab_size = len(vocab) + 1

        word_idx = {c: i + 1 for i, c in enumerate(vocab)}

        xs_and_ys = [Process._vectorize_one(statement, word_idx, truthy, max_word_len) for truthy, statement in clean_data]

        X = [x[0] for x in xs_and_ys]
        y = [x[1] for x in xs_and_ys]

        return X,y, word_idx

    @staticmethod
    def _vectorize_one(statement, vocab_dict, truthy, max_word_len):

        """

        Converts one sentence and one truthy value into an x and y vector respectively

        """

        X = [vocab_dict[word] for word in statement]

        y = np.zeros(len(Truth.to_int))

        y[truthy] = 1

        return X,y

    @staticmethod
    def data_init(json_data):

        """

        Combines all the previous methods to clean and vectorize data

        """

        clean_data = Process._clean_data_and_split_statement(json_data)
        all_words, max_word_len = Process._all_words(clean_data)
        X,y, word_index = Process._vectorize(clean_data, all_words, max_word_len)

        X = pad_sequences(X, maxlen = max_word_len),

        return Data(
                data = data,
                clean_data = clean_data,
                words = all_words,
                word_index = word_index,
                vocab_size = len(all_words) + 1,
                max_word_len = max_word_len,
                X = X,
                y = y)


class Data():

    """

    A struct to hold all the vectorized data information

    """

    def __init__(self,

            data,
            clean_data,
            words,
            word_index,
            vocab_size,
            max_word_len,
            X,
            y):
        """
        data
            The original untouched data
        clean_data
            The cleaned data
        word_index
            mapping from words to indexes
        vocab_size
            Amount of words in vocab
        max_word_len
            The maximum length of a statement
        X
            The statements as vectors
        y
            The truth values as vectors
        """

        self.data = data
        self.clean_data = clean_data
        self.word_index = word_index
        self.vocab_size = vocab_size
        self.max_word_len = max_word_len
        self.X = X
        self.y = y

    def __getitem__(self, key):

        return getattr(self, key)





if __name__ ==  "__main__":
    x = Process()
    d = Process.data

    res = Process._all_chars(d)
    print (res)
