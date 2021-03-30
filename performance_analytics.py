import csv
result_map = {}
with open("performance_test_results.csv") as csvfile:
    reader = csv.reader(csvfile)
    print(reader.__next__())
    # Sequence,SecondaryStructure,Length,Runtime,GCcontent,GCdistance,StructureDistance
    i = 0
    for row in reader:
        i+=1
        if i > 370:
            break
        print("Length: " + row[2] + " Runtime: " + row[3])
        if row[3] == "0.0":
            print("Max runtime reached for a sequence of length: " + row[2] + " at line " + str(i))
            row[3] = "60"
        if row[2] not in result_map:
            result_map[row[2]] = float(row[3])
        else:
            result_map[row[2]] += float(row[3])
    print(result_map)