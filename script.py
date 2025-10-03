import csv, sys, statistics, time

start = time.time()

csv_file, col_index = sys.argv[1], int(sys.argv[2])

with open(csv_file, encoding="utf-16") as f:
    reader = csv.reader(f)
    values = [float(row[col_index]) for row in reader if row]

print("File: ", csv_file)
print("Column:", col_index)
print("Average:", sum(values)/len(values))
print("Median:", statistics.median(values))
print("\n\n")

end = time.time()
print("Execution time:", end - start, "seconds")
