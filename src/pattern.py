from functions import search_with_delete
from copy import deepcopy

#TODO: add preprocessing for all patterns
#TODO: add fact logic
#TODO: add concept set
#TODO: add runtime running
class Pattern:
    def __init__(self, message):
        self._message=message
        self._index = 0
        self._memorize_index = 0
        self.volley = [[]]*30
    
    def new_pattern(self, *patterns):
        self._index = 0
        self._memorize_index = 0
        return self.order(patterns)

    def order(self, *words, memorize = False, indexing=True):
        if memorize:
            self._memorize_index += 1
        if len(list(filter(lambda el: isinstance(el,bool),words))) == len(words):
            return len(list(filter(lambda el: not el,words))) < 1
        if len(list(filter(lambda el: isinstance(el,bool) and not el,words))) > 0:
            return False
        if len(words) < 1: return True
        message_text = self._message.get_text()[self._index:]
        words = [item for sublist in list(map(lambda x: x.split(), list(filter(lambda el: isinstance(el,str), words)))) for item in sublist]
        if len(message_text) <  len(words): return False
        for index in range(len(message_text)-len(words)+1):
            memo_pull = []
            sum_similarity = 0
            input_text = message_text[index:]
            for word_index, word in enumerate(words):
                if (isinstance(word, bool) and word) or input_text[word_index]==word:
                    sum_similarity+=1
                    if memorize:
                        memo_pull.append(input_text[word_index])
            if len(words) == sum_similarity:
                if indexing:
                    self._index+=index+word_index+1
                self.volley[self._memorize_index - 1] = memo_pull
                return True
        return False


    def choice(self, *words, memorize = False):
        if memorize:
            self._memorize_index += 1
        boolean_item = len(list(filter(lambda el: isinstance(el,bool),words)))
        if boolean_item > 0:
            return boolean_item[0]
        if len(words) < 1: return True
        message_text = self._message.get_text()[self._index:]
        for phrase in words:
            word_list = phrase.split()
            sum_similarity = len(list(filter(lambda el: el in message_text, word_list)))
            if sum_similarity > 0 and len(word_list)==sum_similarity:
                if memorize:
                    self.volley[self._memorize_index-1]=[message_text[index] for index in list(map(lambda el: message_text.index(el), word_list))]
                index = message_text.index(word_list[-1])
                self._index += index+1
                return True
        return False

    def option(self, *words, memorize = False):
        self.choice(*words, memorize=memorize)
        return True

    def wildcard(self, number, memorize = False):
        if number <=0:
            raise Exception("Does not working with negative numbers")
        message_text = self._message.get_text()[self._index:]
        min_number = min(number, len(message_text))
        if memorize:
            self._memorize_index += 1    
            self.volley[self._memorize_index-1] = message_text[:min_number]
        self._index+=min_number
        return True

    # TODO: need to implement with range    
    def wildcard_to(self, to_number, memorize = False):
        if to_number <=0:
            raise Exception("To number must be greater than zero")
        pass
    
    def nott(self, *excluded_words):
        if isinstance(excluded_words, bool):
            return not excluded_words
        return len(list(filter(lambda el: el in excluded_words, self._message.get_text()))) < 1

    def nottnot(self, *excluded_words):
        if isinstance(excluded_words, bool):
            return not excluded_words
        return len(list(filter(lambda el: el in excluded_words, self._message.get_text()[self._index:]))) < 1

    def unorder(self, *words, memorize = False):
        if memorize:
            self._memorize_index+=1
        sum_similarity = 0
        message_text = self._message.get_text()
        if search_with_delete(deepcopy(message_text), words):
            if memorize:
                self.volley[self._memorize_index-1] = [message_text[index] for index in list(map(lambda el: message_text.index(el), words))]
            sum_similarity += 1
            return True
        return False

    #TODO: add *ing, shuff*, n.me, s.ug*
    def partial_spelling(self, template):
        pass

    def set_memorize_start_index(self,index):
        self._memorize_index = index
    