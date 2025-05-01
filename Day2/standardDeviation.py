def stdDev(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance**0.5

data=input("Enter value: ");
data=[int(x) for x in data.split()]

print(f"Standard Deviation: {stdDev(data)}")