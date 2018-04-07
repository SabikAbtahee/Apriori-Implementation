import sys


def file():
    sys.stdin=open('apriori.txt','r')
    sys.stdout=open('output.txt','w')

def combinations(iterable, r):
   
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    
    yield tuple(pool[i] for i in indices)
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r: 
                break
        else: 
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def check(i,x):
    if(i in x):
        return True
    else:
        return False

def calculation(items,transactions):
    counts={}
    dicteKey=""
    
    for i in range(1,len(items)+1):
        com = combinations(items,i)
        for c in com:
            for j in range(0,len(transactions),1):
                x=transactions[j].split()
                for i in c:
                  ans=check(i,x)
                  if(ans==False):
                      break
                if(ans==True):
                    
                    dicteKey=""
                    for i in c:
                       dicteKey+=i+","
                    if(dicteKey in counts):
                        counts[dicteKey]+=1
                    else:
                        counts[dicteKey]=1
    return counts
        
     
def printCount(newDictionary):
        for i, k in newDictionary.items():
            print(i,k)
            print(" ")

def statistics(countsAll,minimumSupport):
    newDictionary={}
    highestLength=0

    for i, k in countsAll.items():
        i=str(i).replace(',',"")
        newDictionary[i]=k
        if(newDictionary[i]<minimumSupport):
            del(newDictionary[i])
   
    printCount(newDictionary)
   
    for i, k in newDictionary.items():
        if(len(i)>highestLength):
            highestLength=len(i)
        
    
    last=highestLength

    while(highestLength!=2):
        
        for i, k in newDictionary.items():
            first=0
            last=highestLength-2
            
            if(len(i)>highestLength-2):
                
                x=len(i)
                while(x>=highestLength-2):
                   
                    cal=newDictionary[i]/newDictionary[i[first:last]]
                    print(i[first:last],"=>",i,cal*100,"% Chance")
                    print("")
                    first+=2
                    last+=2
                    x-=2
        highestLength-=2
        
        
def run():
    content = sys.stdin.readlines()
    transactionCount = int(content[0])
    
    minimumSupport=int(content[len(content)-1])
   
    transactions=[]
    items=[]
    
    for i in range(1,transactionCount+1,1):
       
            transactions.append(content[i])
        
    
    for i in range(1,transactionCount+1,1):
        for line in content[i].split():
            if(line not in items):
                items.append(line)
        items.sort()
    
    ans=calculation(items,transactions)

    statistics(ans,minimumSupport)
    
    

def main():
    file()
    run()
    
if __name__ == "__main__":
    main()
    