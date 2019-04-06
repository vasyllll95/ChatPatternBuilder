class Message:
    # TODO: divide into get_original_text and get_preprocessed_text
    def __init__(self, text, preprocessor=None):
        self.__text = text
        self.__preprocessor = preprocessor

    def set_new_input(self, text):
        self.__text = text

    def get_text(self):
        return self.__preprocessor(self.__text) if self.__preprocessor else self.__text.split()