from translate import Translator


class HebrewTranslator:
    translator_obj = Translator(from_lang="he", to_lang="en")

    def translate(self, toTrans):
        return self.translator_obj.translate(toTrans)
