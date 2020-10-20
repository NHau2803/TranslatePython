from googletrans import Translator
translator  = Translator()

def trans(text, dest):
        return translator.translate(text, dest).text 
        

for i in range(30):
        text = input("input text: ")
        result = trans(text, "en")
        if(result == text):
                result = trans(text, "vi")
        print("====> ", result)
        
