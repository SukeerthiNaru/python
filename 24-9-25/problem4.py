# Problem-4.py
# Get the total count of numbers in the list that are multiples of [1–9]

def count_multiples(nums):
    result = {i: 0 for i in range(1, 10)}  # dictionary keys 1–9
    for n in nums:
        for i in range(1, 10):
            if n % i == 0:
                result[i] += 1
    return result

def main():
    nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(nums)
    print(output)

if __name__ == "__main__":
    main()
