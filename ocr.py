import easyocr
import os

reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = []
path = './img'

for file in os.listdir(path):
    result.append('==========「' + file + '」==========')
    result += reader.readtext(os.path.join(path, file), detail = 0)


with open('./Vocabulary Handbook.txt', mode = 'w') as handbook:
    handbook.write('\n'.join(result))
    handbook.close()
