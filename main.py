from quicksort import quicksort

def main():
    numbers = [22,3,19,10,11,5,7,80,65,1,43,2]
    n = len(numbers)
    quicksort(numbers,0,n-1)
    print(numbers)
if __name__ == "__main__":
    main()