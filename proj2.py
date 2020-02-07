#extract Data Function

def processGrams(fl):
    trainData={}
    unigramDict={}
    bigramDict={}
    trigramDict={}
    uniCount=0; biCount=0
    with open(fl, 'r') as Data:
        lines = [l.split() for l in Data]
        #lines.insert(0,['<s>'])
        #lines.append(['</s>'])
        #print(lines[1])

        #unigram
        for uline in range(len(lines)):
            # count into dictionary
            uni = [];
            # check if its first line, middle lines or last line
            if (uline == 0):
                uni = ['<s>'] + lines[uline]
            elif (uline == len(lines)-1):
                uni = lines[uline] + ['</s>']
            else:
                uni = lines[uline]
            for uword in range(len(uni)):
                val = 1; current = uni[uword]
                if (unigramDict.get((current))):
                    val = unigramDict.get((current)) + 1
                unigramDict.update({(current): val})
        #print(uniCount)
        #print(unigramDict)
        print(len(unigramDict))

        #bigrams
        for bline in range (len(lines)):
            bi=[];
            bi=['<s>']+lines[bline]+['</s>']
            for bword in range(len(bi)-1):
                val = 1; nword=bword+1;
                current=bi[bword]; next=bi[nword]
                if(bigramDict.get((current,next))):
                    val=bigramDict.get((current,next))+1
                bigramDict.update({(current,next):val})
       # print(bigramDict)
        print(len(bigramDict))

        # trigrams
        for tline in range(len(lines)):
            tri = [];
            tri = ['<s>']+['<s>'] + lines[tline] + ['</s>']+['</s>']
            for tword in range(len(tri) - 2):
                val = 1; nword = tword + 1; nnword=tword+2;
                current = tri[tword];  next = tri[nword]; nnext=tri[nnword]
                if (trigramDict.get((current, next, nnext))):
                    val = trigramDict.get((current, next, nnext)) + 1
                trigramDict.update({(current, next, nnext): val})
       # print(trigramDict)
        print(len(trigramDict))

def processProbs():
    print("hello")

processGrams("minCorpus.txt");