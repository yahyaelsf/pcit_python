import time
import numpy as np


SIZE = 1_000_000


list1 = list(range(SIZE))
list2 = list(range(SIZE))

start_time = time.time()
result_list = [x + y for x, y in zip(list1, list2)]
list_time = time.time() - start_time
print(f"Time taken using standard Python List: {list_time:.6f} seconds")

array1 = np.arange(SIZE)
array2 = np.arange(SIZE)

start_time = time.time()
result_array = array1 + array2
numpy_time = time.time() - start_time
print(f"Time taken using NumPy Array: {numpy_time:.6f} seconds")


speed_factor = list_time / numpy_time
print(f"\nNumPy is approximately {speed_factor:.1f}x faster than Python List!")