from translate import Translator

class Translator():

    translator_obj = Translator(from_lang="he", to_lang="en")


    def translate(self, toTrans):
    	return self.translator_obj.translate(toTrans)
   