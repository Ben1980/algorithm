from tabulate import tabulate
from utils import MeasureExecutionTime, RandomList
from sorting.insertionSort import InsertionSort

def main():
    NumberOfElements = 10000

    print('Sorting Algorithm:')
    head = ['Algorithm', 'Duration']
    data = []

    duration = MeasureExecutionTime(InsertionSort, RandomList(NumberOfElements))
    data.append(['Insertion-Sort', duration])

    print(tabulate(data, headers=head, tablefmt="grid"))
  
if __name__=="__main__":
    main()
