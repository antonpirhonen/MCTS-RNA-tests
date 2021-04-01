import csv
result_map = {}
with open("performance_test_results_many.csv") as csvfile:
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
    
stats = open("performance_test_many_statistics.csv", "w")
stats.write("Length,AverageRuntime,MedianRuntime,MaxCount\n")

def replaceNoneWithInf(num):
    if num == None:
        return float("inf")
    return num

def calculateMedian(arr):
    maxcount = arr.count(None)
    arr = list(map(replaceNoneWithInf, arr))
    arr.sort()
    l = len(arr)
    if maxcount >= l/2:
        return ">300"
    else:
        if l % 2 == 0:
            return str((arr[int(l/2)] + arr[int(l/2-1)]) / 2)
        else:
            return str(arr[int(l/2)])

for key in result_map:
    arr = result_map[key]
    maxcount = arr.count(None)
    avg = sum(filter(None, arr))/(len(arr) - maxcount) # average of finished runtimes 
    stats.write(key + "," + str(avg) + "," + calculateMedian(arr) + "," + str(maxcount) + "\n")

stats.close()