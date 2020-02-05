#extract Data Function

def readData(fl):
    trainData={}
    unigramList={}
    bigramList=[]
    trigramList=[]
    totalCount=0
    with open(fl, 'r') as Data:
        lines = [l.split() for l in Data]
        lines.insert(0,'<s>')
        lines.append('</s>')
        print(lines[1])
        #unigram
        for line in range(len(lines)):
            for word in lines[line]:
                  unigramList[word]={word}
                  trainData.update({'unigram':unigramList})
                  totalCount=totalCount+1
        print(len(unigramList))
        print(totalCount)
        print(unigramList)


readData("minCorpus.txt");