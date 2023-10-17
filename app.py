import math

class ComplexApp:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def remove_data(self, value):
        if value in self.data:
            self.data.remove(value)

    def calculate_mean(self):
        if len(self.data) == 0:
            return None
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        if len(self.data) == 0:
            return None
        sorted_data = sorted(self.data)
        middle = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def calculate_standard_deviation(self):
        if len(self.data) < 2:
            return None
        mean = self.calculate_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diff) / (len(self.data) - 1)
        return math.sqrt(variance)

if __name__ == "__main__":
    app = ComplexApp()

    # Test 1: Add data points
    for i in range(20):
        app.add_data(i)

    # Test 2: Remove data points
    app.remove_data(10)

    # Test 3: Calculate mean
    mean = app.calculate_mean()

    # Test 4: Calculate median
    median = app.calculate_median()

    # Test 5: Calculate standard deviation
    std_deviation = app.calculate_standard_deviation()

    # Continue with more tests...

    # Print results
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_deviation}")
