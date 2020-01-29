
def largest_adjacent_sum(numbers):  # O(n) time, O(1) space
    include = exclude = 0
    for current in numbers:
        new_exclude = max(include, exclude)
        include = exclude + current
        exclude = new_exclude
        
    return max(include, exclude)

if __name__ == "__main__":
    largest_adjacent_sum([2, 4, 6, 2, 5])
