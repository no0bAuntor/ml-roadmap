def meanDeterminer(data):
    mean= sum(data)/len(data)
    return mean

def varianceDeterminer(data):
    mean= meanDeterminer(data)
    variance= sum((x-mean)**2 for x in data)/len(data)
    return variance


data=input("Enter the data: ")
data= [int(x) for x in data.split()]


print("Mean:", meanDeterminer(data)) 

print("Variance:", varianceDeterminer(data))