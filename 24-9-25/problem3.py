# Problem-3.py
# If a is odd -> first a odd numbers
# If a is even -> first (a-1) odd numbers

def series_problem3(a):
    a = int(a)
    count = a if a % 2 == 1 else max(1, a-1)
    return [2*i + 1 for i in range(count)]

def main():
    a = int(input("Enter a: ").strip())
    result = series_problem3(a)
    print("Output:", ", ".join(map(str, result)))

if __name__ == "__main__":
    main()
