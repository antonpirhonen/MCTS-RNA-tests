import csv
result_map = {}
with open("performance_test_results.csv") as csvfile:
    reader = csv.reader(csvfile)
    print(reader.__next__())
    # Sequence,SecondaryStructure,Length,Runtime,GCcontent,GCdistance,StructureDistance
    i = 0
    for row in reader:
        i+=1
        print("Length: " + row[2] + " Runtime: " + row[3])
        if row[3] == "0.0":
            print("Max runtime reached for a sequence of length: " + row[2] + " at line " + str(i))
            maxcount = row[2]+"maxcount"
            if row[2] not in result_map:
                result_map[row[2]] = [None]
            else:
                result_map[row[2]].append(None)
            continue
        if row[2] not in result_map:
            result_map[row[2]] = [float(row[3])]
        else:
            result_map[row[2]].append(float(row[3]))
    
stats = open("performance_test_statistics.csv", "w")
stats.write("Length,AverageRuntime,MedianRuntime,MaxCount\n") # Add median runtime?

def replaceNoneWithInf(num):
    if num == None:
        return float("inf")
    return num

def calculateMedian(arr):
    maxcount = arr.count(None)
    arr = list(map(replaceNoneWithInf, arr))
    arr.sort()
    print("Array: ", arr)
    if maxcount >= 5:
        return ">60"
    else:
        return str((arr[4] + arr[5]) / 2)

for key in result_map:
    arr = result_map[key]
    maxcount = arr.count(None)
    avg = sum(filter(None, arr))/(len(arr) - maxcount) # average of < 60s runtimes 
    stats.write(key + "," + str(avg) + "," + calculateMedian(arr) + "," + str(maxcount) + "\n")

stats.close()