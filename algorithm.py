from tabulate import tabulate
from utils import TableHeader, Measure
from sorting.insertionSort import InsertionSort
from sorting.mergeSort import MergeSort

def main():
    benchmark = False

    print('Sorting Algorithm:')
    head = TableHeader(benchmark)
    data = []

    data.append(Measure(benchmark).Name('Insertion-Sort').MeasureExecutionTime(InsertionSort).Results())
    data.append(Measure(benchmark).Name('Merge-Sort').MeasureExecutionTime(MergeSort).Results())

    print(tabulate(data, headers=head, tablefmt="grid"))
  
if __name__=="__main__":
    main()
