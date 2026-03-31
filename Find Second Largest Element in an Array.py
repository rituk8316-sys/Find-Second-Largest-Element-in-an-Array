# Find second largest element in an array

def second_largest(arr):
    largest = second = arr[0]

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


# Input
array = [10, 25, 45, 30, 45, 50, 20]

# Function call
result = second_largest(array)

# Output
print("Second largest element is:", result)
