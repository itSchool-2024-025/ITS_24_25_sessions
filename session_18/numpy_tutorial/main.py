# Installation check and import
try:
    import numpy as np
    print("NumPy successfully imported!")
except ImportError:
    print("Please install NumPy using 'pip install numpy'")

def print_hi():
    # Creating arrays with different methods
    arr = np.array([1, 2, 3])
    zeros = np.zeros((2, 3))  # 2x3 array of zeros
    ones = np.ones((3, 3))  # 3x3 array of ones
    range_arr = np.arange(0, 10, 2)  # 0 to 10, step of 2
    # Checking array attributes
    # print("Array:", arr, ones)
    # print("Shape:", arr.shape)
    # print("Size:", arr.size)
    # print("Dimensions:", arr.ndim)
    # print("Data type:", arr.dtype)
    # print("zeros ** arr:", zeros**arr)
    new_arr = ones*arr+ones
    print("ones * arr:", new_arr)
    print("new_arr sum: ", new_arr.sum())
    print("new_arr mean: ", new_arr.mean())
    print("new_arr min: ", new_arr.min())
    print("new_arr max: ", new_arr.max())
    print("new_arr std: ", new_arr.std())
    print("new_arr var: ", new_arr.var())

def sec_func():
    # Array indexing and slicing
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Array: \n", arr)
    print("Element at [0, 0]:", arr[0, 0])  # Accessing element
    print("First row:", arr[0, :])  # First row
    print("Last column:", arr[:, -1])  # Last column
    print("Subarray:", arr[2:, 1:])  # Subarray

def transp_arr():
    # Reshaping and transposing
    arr = np.arange(12)  # 1D array of 0 to 11
    reshaped = arr.reshape(3, 4)
    print("Original:", arr)
    print("Reshaped to 3x4:", reshaped)
    print("Transposed:", reshaped.T)

def load_num_data():
    data = np.loadtxt('numerical_data.csv', delimiter=',')
    print(data)

def load_mixed_data():
    data = np.genfromtxt('mixed_data.csv', delimiter=',', skip_header=1, dtype=None, encoding=None)
    print(data)
    print(data[1])

def get_arr_from_dict():
    # Creating arrays with different methods
    arr = np.array(
        [(1, 'drake', 2.2), (7, 'indiana', 4.1), (7, 'pippin', 4.5), (7, 'gollum', 4.0)]
        # dtype=[('id', 'i4'), ('name', 'U10'), ('km travelled', 'f4')]
    )

    print(arr)
    # print(arr['name'])
    print(arr.shape)
    print(arr.size)
    print(arr.ndim)
    print(arr.dtype)
    array = np.array(
        [(1, 'apple', 2.5), (2, 'banana', 3.5)],
        dtype=[('id', 'i4'), ('name', 'U10'), ('price', 'f4')])
    print(array)
    print(array['name'])  # Accessing 'name' column
    print(array.shape)


if __name__ == '__main__':
    # print_hi()
    # sec_func()
    # transp_arr()
    # load_num_data()
    # load_mixed_data()
    get_arr_from_dict()