def sum_and_average(numbers):
    """Find the sum and average of a list of numbers using inner functions.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        tuple: Sum and average of the numbers in the list.
    """
    def calculate_sum():
        """Calculate the sum of the list."""
        return sum(numbers) if numbers else 0

    def calculate_average():
        """Calculate the average of the list."""
        return sum(numbers) / len(numbers) if numbers else 0

    return calculate_sum(), calculate_average()


if __name__ == '__main__':
    result = sum_and_average([1, 2, 3, 4, 5])
    print(result)  # Sollte (15, 3.0) zurückgeben