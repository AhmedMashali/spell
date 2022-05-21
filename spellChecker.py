from difflib import SequenceMatcher

def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def binarySearch(dictionary, word):
    first = 0
    last = len(dictionary) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if dictionary[midpoint] == word:
            return True
        else:
            if word < dictionary[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False

# finding closest  words if the word dose not exist by using sequenceMatcher
def closestWords(dictionary, word):
    values = [i*0 for i in range(5)]
    position = [i*0 for i in range(5)]
    for i in range(len(dictionary) - 1):
        sequence = SequenceMatcher(isjunk=None, a=word, b=dictionary[i]).ratio()
        for j in range(len(position)):
            if sequence > values[j]:
                values[j] = sequence
                position[j] = i
                break
    print(word,"is wrong,do yo mean:")
    for i in position:
        print(dictionary[i])
    print("\n")

def read_txt_file():
    openDictionary = open("Dictionary.txt", "r")
    dict= openDictionary.read().split()
    openDictionary.close()
    return dict

if __name__ == "__main__":
    dictionary = read_txt_file()
    mergeSort(dictionary)
    print("Enter a paragraph!")
    lines=[]
    while True:
        line=input().split()
        if line:
            lines.append(line)
        else:
            break
    #print(lines)
    for i in lines:
        for word in i:
                if not binarySearch(dictionary,word.lower()):
                    closestWords(dictionary,word.lower())
