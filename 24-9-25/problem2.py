# Problem-2.py
# Generate first 'a' odd numbers

def series_problem2(a):
    a = int(a)
    return [2*i + 1 for i in range(a)]

def main():
    a = int(input("Enter a: ").strip())
    result = series_problem2(a)
    print("Output:", ", ".join(map(str, result)))

if __name__ == "__main__":
    main()
