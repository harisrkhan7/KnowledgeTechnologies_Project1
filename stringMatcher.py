def initialiseSoundexDictionary():
    soundexDictionary = {}

    soundexDictionary['a'] = 0
    soundexDictionary['e'] = 0
    soundexDictionary['h'] = 0
    soundexDictionary['i'] = 0
    soundexDictionary['o'] = 0
    soundexDictionary['u'] = 0
    soundexDictionary['w'] = 0
    soundexDictionary['y'] = 0
    
    soundexDictionary['b'] = 1
    soundexDictionary['p'] = 1 
    soundexDictionary['f'] = 1
    soundexDictionary['v'] = 1
    
    soundexDictionary['c'] = 2
    soundexDictionary['g'] = 2
    soundexDictionary['j'] = 2
    soundexDictionary['k'] = 2
    soundexDictionary['q'] = 2
    soundexDictionary['s'] = 2
    soundexDictionary['x'] = 2
    soundexDictionary['z'] = 2
    
    soundexDictionary['d'] = 3
    soundexDictionary['t'] = 3
    
    soundexDictionary['l'] = 4
    
    soundexDictionary['m'] = 5
    soundexDictionary['n'] = 5
    
    soundexDictionary['r'] = 6

    return soundexDictionary

soundexDictionary = initialiseSoundexDictionary()
Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'
,'q','r','s','t','u','v','w','x','y','z']

def needlmanWunsch(t, s):
    """ 
        needlmanWunsch(s, t) -> global edit distance
        global edit distance is the score to transform the strings 
        t to s. The higher the score, the better it is. 
    """
    insertionCost = -1
    deletionCost = -1
    replacementCost = -1
    matchCost = 1

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    
    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i * deletionCost
   
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i * insertionCost
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = matchCost
            else:
                cost = replacementCost

            dist[row][col] = max(dist[row-1][col] + deletionCost,      # deletion
                                 dist[row][col-1] + insertionCost,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
    
    return dist[row][col]




def smithWaterman(t, s):
    """ 
        smithWaterman(s, t) -> ldist
        ldist is the Local Edit distance from the strings
        t to s. 
    """
    insertionCost = -1
    deletionCost = -1
    replacementCost = -1
    matchCost = 1

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    
    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = 0
   
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = 0
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = matchCost
            else:
                cost = replacementCost

            dist[row][col] = max(0,
                                 dist[row-1][col] + deletionCost,      # deletion
                                 dist[row][col-1] + insertionCost,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
    
    return max(map(max, dist))

"""Convert a sourceString to a soundex String 
Removes duplicates and zeros as well
"""
def soundexConvertString(sourceString):
    soundexFullArray = replaceSoundexValues(sourceString)
    "print(soundexFullArray)"

    soundexDuplicateCleanedArray = removeDuplicates(soundexFullArray)
    "print(soundexDuplicateCleanedArray)"

    zeroRemovedArray = removeZeros(soundexDuplicateCleanedArray)
    "print(zeroRemovedArray)"

    soundexFinalArray = []
    soundexFinalArray.append(sourceString[0])
    soundexFinalArray.extend(zeroRemovedArray)
    "print(soundexFinalArray)"

    lengthNArray = truncateToLengthN(soundexFinalArray,4)

    
    soundexString = "".join(str(elm) for elm in lengthNArray) # Python power

    return soundexString

    
    
"""Removes multiple successive occurences of the same value from an array
and also drops the first index"""
def removeDuplicates(fullArray):
    "Cleaned array with first index removed"
    duplicateCleanedArray = []
    for i in range(1,len(fullArray)):
        nextSoundIndex = i + 1
        if(nextSoundIndex<len(fullArray)):
            if(fullArray[i] != fullArray[nextSoundIndex]):
                duplicateCleanedArray.append(fullArray[i])
    duplicateCleanedArray.append(fullArray[len(fullArray)-1])
    return duplicateCleanedArray


"""Replaces the string characters with their equivalent soundex values
Returns an int array with replaced values."""
def replaceSoundexValues(sourceString):
    soundexFullArray = []
    for alphabet in sourceString:
        if(alphabet in Alphabets):
            soundexFullArray.append(soundexDictionary[alphabet])
    return soundexFullArray
    
def removeZeros(sourceString):
    zeroRemovedArray = []
    for value in sourceString:
        if(value != 0):
            zeroRemovedArray.append(value)
    return zeroRemovedArray

def truncateToLengthN(sourceString,N):
    lengthNArray = []
    i = 0
    for value in sourceString:
        if(i>(N-1)):
            break
        lengthNArray.append(value)
        i+=1
    return lengthNArray

        