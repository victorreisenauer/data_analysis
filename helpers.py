
import os
import numpy as np
import matplotlib.pyplot as plt

def iterate_over_files(directory_path, file_extension='.sp'):
    """
    Iterate over files in a directory with a specific file extension.

    Args:
        directory_path (str): Path to the directory containing the files.
        file_extension (str): File extension to filter files by (default: '.sp').

    Yields:
        str: Each filename in the directory with the specified extension.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            yield filename


def read_file_contents(file_path: str):
    """
    Read contents of a file and extract data after the 'DATA' line.

    Args:
        file_path (str): Path to the file.

    Returns:
        numpy.ndarray: Numpy array containing the extracted data.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_start_index = None
    for i, line in enumerate(lines):
        if "DATA" in line:
            data_start_index = i + 1
            break

    if data_start_index is not None:
        data_rows = [line.split() for line in lines[data_start_index:] if line.strip()]
        data_array = np.array(data_rows, dtype=float)
        return data_array
    else:
        return None


def build_data_dictionary(directory_path: str):
    """
    Build a dictionary mapping file names to numpy arrays of extracted data.

    Args:
        directory_path (str): Path to the directory containing the files.

    Returns:
        dict: Dictionary mapping filenames to numpy arrays of data.
    """
    data_dict = {}
    for filename in iterate_over_files(directory_path):
        file_path = os.path.join(directory_path, filename)
        data_array = read_file_contents(file_path)
        if data_array is not None:
            data_dict[filename] = data_array
    return data_dict




def filter_dict_by_bounds(input_dict: dict, lower_bound:int, upper_bound:int):
    """
    Filter a dictionary based on keys of the form "sXXp.sp" where XX is a two-digit number,
    returning a new dictionary containing only the key-value pairs where the two-digit number
    falls between the specified lower_bound and upper_bound (inclusive).

    Args:
        input_dict (dict): The input dictionary to filter.
        lower_bound (int): The lower bound of the two-digit number range.
        upper_bound (int): The upper bound of the two-digit number range.

    Returns:
        dict: A filtered dictionary containing key-value pairs where the two-digit number
              extracted from keys falls within the specified bounds.
    """
    filtered_dict = {}

    for key in input_dict:
        # Extract the two-digit number from the key
        if key.startswith('s') and key.endswith('p.sp') and len(key) == 7:
            try:
                # Extract the XX from the key (assuming the format is 'sXXp.sp')
                two_digit_number = int(key[1:3])
                # Check if the extracted number is within the specified bounds
                if lower_bound <= two_digit_number <= upper_bound:
                    filtered_dict[key] = input_dict[key]
            except ValueError:
                # Handle cases where the XX couldn't be converted to an integer
                continue
    
    return filtered_dict


