from gensim.models import FastText

def getData():
    files =["1.txt","2.txt"]
    all_words =[]
    for x in files:
        f =  open(x,"r")
        data = f.read()
        data = data.split(" ")
        items = []
        numList = ["1","2","3","4","5","6","7","8","9","0"]
        for y in data:
            flag = 1
            for z in numList:
                if z in y:
                    flag = 0
                    break
            if flag == 1:
                if y not in items and y != "" and y !=" ":
                    y = y.replace(".","")
                    y =  y.replace(" ","")
                    if len(y) >2:
                        items.append(y)
        for y in items:
            if y not in all_words:
                all_words.append(y)
    print(len(all_words))
    return all_words

def main():
    words = getData()
    model = FastText(words, size=100, window=5, min_count=5, workers=4,sg=1)
    model.wv.save_word2vec_format('fastmodel.bin',binary=True)
main()


