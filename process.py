from data import People

class CharacterInformation():

    def __init__(self, data):
        self.data = data
        self.max_len = CharacterInformation._max_len(data)
        self.all_chars= CharacterInformation._all_chars(data)
        self.all_names = CharacterInformation._all_names(data)
        self.char_indices, self.indices_char = CharacterInformation._create_dicts(self.all_chars)

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
    def _all_names(data):

        return data['name'].unique()

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
        pdb.set_trace()

        word_idx = {c: i + 1 for i, c in enumerate(vocab)}

        xs_and_ys = [Process._vectorize_one(statement, word_idx, truthy, max_word_len) for truthy, statement in clean_data]

        X = [x[0] for x in xs_and_ys]
        y = [x[1] for x in xs_and_ys]

        return X,y, word_idx

class Vectorize:

    def __init__(self, data, character_info):

        self.data = data
        self.character_info = character_info
        self.X, self.y = Vectorize._vectorize(data, character_info)

    @staticmethod
    def _vectorize(data,character_info):

        X = np.zeros((l_data, max_charlen, all_charlen), dtype=np.bool)
        y = np.zeros((l_data), dtype=np.int)

        for index, row in data.iterrows():

            name, male, female = row['name'], row['male'], row['female']

            gender_score = male - female

            for letter_index, letter in enumerate(name):
                X[index, letter_index, character_info.char_indices[letter]] = 1
            y[index] = gender_score

        return X,y

if __name__ ==  "__main__":
    data = People.read()
    character_info = CharacterInformation(data)
    X,y = Vectorize(data, character_info)



