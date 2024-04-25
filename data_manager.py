import os
import numpy as np
from dataset import Dataset

class DataManager:
    dataset_dir = 'datasets'

    """
    A class for finding and fetching data from a dataset directory.

    Attributes:
        None

    Methods:
        fetch_data: Fetches the data from the dataset directory based on the input string.
        iterate_over_files: Iterate over files in a directory with a specific file extension.
        read_file_contents: Read contents of a file and extract data after the 'DATA' line.
        build_data_dictionary: Build a dictionary mapping file names to numpy arrays of extracted data.
        filter_dict_by_bounds: Filter a dictionary based on keys of the form "sXXp.sp" where XX is a two-digit number.
        
    """

    def __init__(self, directory='datasets'):
        self.directory = directory

    def fetch_raw_data(self, input_string):
        matching_dir = self.__check_for_matches(input_string, self.directory)
        
        directory_path = os.path.join(self.directory, matching_dir)
        data_dict = self.__build_data_dictionary(directory_path)
        
        return data_dict
    
    def build_dataset_from(self, input_string):
        data_dict = self.fetch_raw_data(input_string)
        data_dict = dict(sorted(data_dict.items(), key=lambda x: x[0]))
        dataset = Dataset.from_dict(data_dict)
        return dataset
    

    def filter_dataset_by_bounds(self, dataset, lower_bound, upper_bound):
        filtered_dict = self.__filter_dict_by_bounds(dataset.as_dict(), lower_bound, upper_bound)
        filtered_dataset = Dataset.from_data(filtered_dict)
        return filtered_dataset
    
    def __check_for_matches(self, input_string, dataset_dir):
        matching_dirs = [dir for dir in os.listdir(dataset_dir) if input_string in dir]
        if len(matching_dirs) > 1:
            raise ValueError('Input string matches multiple directories')
        elif len(matching_dirs) == 0:
            raise ValueError('Input string does not match any directories')
        return matching_dirs[0]
    
    def __iterate_over_files(self, directory_path, file_extension='.sp'):
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
    
    def __read_file_contents(self, file_path: str):
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
    
    def __build_data_dictionary(self, directory_path: str):
        """
        Build a dictionary mapping file names to numpy arrays of extracted data.

        Args:
            directory_path (str): Path to the directory containing the files.

        Returns:
            dict: Dictionary mapping filenames to numpy arrays of data.
        """
        data_dict = {}
        for filename in self.__iterate_over_files(directory_path):
            index = self.__extract_index(filename)
            file_path = os.path.join(directory_path, filename)
            data_array = self.__read_file_contents(file_path)
            if data_array is not None:
                data_dict[index] = data_array
        return data_dict
    
    def __extract_index(self, filename: str):
        try:
            return int(filename[filename.index('.')-3:filename.index('.')])
        except ValueError:
            raise ValueError("Filename does not contain a valid index")
    
    def __filter_dict_by_bounds(self, input_dict: dict, lower_bound:int, upper_bound:int):
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
                if lower_bound <= key <= upper_bound:
                    filtered_dict[key] = input_dict[key]
        
        return filtered_dict
    

    def rename_files(self, input_string, new_string):
        matching_dir = self.__check_for_matches(input_string, self.directory)
        
        directory_path = os.path.join(self.directory, matching_dir)
        file_extension = os.path.splitext(new_string)[1]
        
        # Get a list of all files in the directory
        files = os.listdir(directory_path)
        
        # Sort the files in alphabetical order
        files.sort()
        
        # Rename the files
        for i, filename in enumerate(files):
            # Get the file extension
            old_extension = os.path.splitext(filename)[1]
            
            # Create the new file name with the increasing numbering
            new_filename = f"{new_string}_{i+1:03d}{old_extension}"
            # Rename the file
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
