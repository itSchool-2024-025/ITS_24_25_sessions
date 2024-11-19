import numpy as np
def read_with_loadtext_from_csv(csv_filepath):
    data = np.loadtxt(fname=csv_filepath, delimiter=",", skiprows=1)
    print(data)


def read_with_gen_from_text_from_csv(csv_filepath):
    data = np.genfromtxt(fname=csv_filepath, delimiter=",", skip_header=1, dtype=None)
    print(data)

def write_data_csv_file(csv_filepath):
    # Sample numerical data
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Save to CSV
    np.savetxt(csv_filepath, data, delimiter=',', fmt='%d')

def write_data_and_headers_to_csv_file(csv_filepath):
    # Sample data with floating-point values
    data = np.array([[1.5, 2.33, 3.45], [4.1, 5.56, 6.789], [7.0, 8.1, 9.999]])

    # Save with headers and custom float formatting
    np.savetxt(csv_filepath, data, delimiter=',', fmt='%.2f', header='Col1,Col2,Col3', comments='')


if __name__ == '__main__':
    # read_with_loadtext_from_csv("numerical_data.csv")
    # read_with_gen_from_text_from_csv("mixed_data.csv")
    write_data_csv_file("written_data_1.csv")
    write_data_and_headers_to_csv_file("written_data_2.csv")