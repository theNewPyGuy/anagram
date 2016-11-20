def reverse(s):
    newA = []
    for i in range(0, len(s)):
        newA.append(s[(len(s)-(i+1))])
    return newA

def SplitA(word):
    Array = []
    for i in word:
        Array.append(i)
    return Array

def w2F(path, data):
    File = open(path, 'a')
    File.write(data)
    File.close()

def rMF(path, di):
    print path, di
    File = open(path, 'r')
    r = []
    if not di:
        for name in File.read().split('\n'):
            r.append(name)
        File.close()
        return r
    else:
        #print "else"
        for line in File.read().split('\n'):
            
            #print line.split('\t')[0]
            if line.split('\t')[0] == 'US':
                #print line.split('\t')
                w2F('us.txt', line)

def toString(Array):
    string = ""
    for i in Array:
        string += i
    return string

def englishWords():
    words = open('words.txt')
    english = {}
    for word in words.read().split('\n'):
        english[word] = "english"
    words.close()
    return english

def isEnglish(word):
    if word in english:
        
        return True
    
def Mirror(s):
    NewImage = []
    for i in s:
        NewImage.append(i)
    return NewImage
