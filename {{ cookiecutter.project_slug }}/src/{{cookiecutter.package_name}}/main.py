
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def gpu_intensive_calculation(x: int) -> int:
    # Placeholder for an operation that would be GPU-accelerated
    result = x * x  # Simulating a GPU-intensive task
    return result


if __name__ == "__main__":
    print(add(2, 2))
