#extract Data Function

def readData(fl):
    trainData={}
    unigramList={}
    bigramTuple=()
    trigramList=[]
    totalCount=0
    with open(fl, 'r') as Data:
        lines = [l.split() for l in Data]
        lines.insert(0,'<s>')
        lines.append('</s>')
        print(lines[1])

        #unigram
        for uline in range(len(lines)):
            for word in lines[uline]:
                  unigramList[word]={word}
                  trainData.update({'unigram':unigramList})
                  totalCount=totalCount+1
        print(len(unigramList))
        print(totalCount)
        print(unigramList)

        #bigrams
        for bline in range (len(lines)):
            d=lines[bline]
            for bword in range(len(lines[bline])):
                if (bword==len(lines[bline])-1):
                    nword=bword
                else:
                    nword=bword+1
                current=d[bword]
                next=d[nword]
                #print("-------",current)
                trainData[(current, next)]=0
        print(trainData)


readData("minCorpus.txt");