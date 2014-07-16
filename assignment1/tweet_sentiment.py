import sys
import json

def initDictFromFile(f, d):
    newDict = {} 
    for line in f:
      k, v  = line.split(d)
      newDict[k] = int(v)
    return newDict

def getMsgs(f):
    ls = [] 
    for line in f:
      j  = json.loads(line).get('text',"").split(" ")
      if j[0] != '':
          ls.append(j)
    return ls

def getSentiment(msgs, sLs):
    for msg in msgs:
        s = 0
        for w in msg:
            if w in sLs.keys():
                s += sLs[w]
        print s

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    afinnfile = sent_file
    scores = initDictFromFile(afinnfile, '\t')
    out = tweet_file
    msgLs = getMsgs(out)
    getSentiment(msgLs, scores)

if __name__ == '__main__':
    main()
