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
            if maxcount not in result_map:
                result_map[maxcount] = 1
            else:
                result_map[maxcount] += 1
            continue
        if row[2] not in result_map:
            result_map[row[2]] = float(row[3])
        else:
            result_map[row[2]] += float(row[3])
    print(result_map)

stats = open("performance_test_statistics.csv", "w")
stats.write("Length,AverageRuntime,MaxCount\n") # Add median runtime?

def seqCount(length):
    if length <= 200:
        return 20
    return 10

for key in result_map:
    if key.isnumeric():
        maxcount = 0
        if key + "maxcount" in result_map:
            maxcount = result_map[key + "maxcount"]
        avg = result_map[key]/(seqCount(int(key)) - maxcount)
        stats.write(key + "," + str(avg) + "," + str(maxcount) + "\n")

stats.close()