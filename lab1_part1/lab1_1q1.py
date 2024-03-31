import time
import matplotlib.pyplot as plt

# Iterative approach to find sum of first N natural numbers
def sum_iterative(N):
    result = 0
    for i in range(1, N+1):
        result += i
    return result

# Recursive approach to find sum of first N natural numbers
def sum_recursive(N):
    if N == 0:
        return 0
    return N + sum_recursive(N-1)

# Function to measure time taken for both approaches
def measure_time(func, N):
    start_time = time.time()
    func(N)
    return time.time() - start_time

# Varying values of N
Ns = range(1, 1001, 100)  # Change step size as needed

# Measure time taken for both approaches for varying Ns
iterative_times = [measure_time(sum_iterative, N) for N in Ns]
recursive_times = [measure_time(sum_recursive, N) for N in Ns]

# Plotting
plt.plot(Ns, iterative_times, label='Iterative')
plt.plot(Ns, recursive_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Time taken to find sum of first N natural numbers')
plt.legend()
plt.show()
