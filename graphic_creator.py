from helpers import build_data_dictionary, filter_dict_by_bounds
import numpy as np
import matplotlib.pyplot as plt



def plot_side_by_side_data(data_dict1: dict, data_dict2: dict):
    """
    Plot data arrays stored in two dictionaries side by side.

    Args:
        data_dict1 (dict): First dictionary mapping filenames to numpy arrays of data.
        data_dict2 (dict): Second dictionary mapping filenames to numpy arrays of data.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))  # Create a figure with two subplots

    # Plot data from data_dict1 (subplot 1)
    axes[0].set_title('Data from Dictionary 1')  # Set title for subplot 1
    for filename, data_array in data_dict1.items():
        x_values = data_array[:, 0]
        y_values = data_array[:, 1]
        axes[0].plot(x_values, y_values, label=filename)
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    axes[0].legend()

    # Plot data from data_dict2 (subplot 2)
    axes[1].set_title('Data from Dictionary 2')  # Set title for subplot 2
    for filename, data_array in data_dict2.items():
        x_values = data_array[:, 0]
        y_values = data_array[:, 1]
        axes[1].plot(x_values, y_values, label=filename)
    axes[1].set_xlabel('X')
    axes[1].set_ylabel('Y')
    axes[1].legend()

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()



def plot_data_arrays(data_dict: dict):
    """
    Plot data arrays stored in a dictionary.

    Args:
        data_dict (dict): Dictionary mapping filenames to numpy arrays of data.
    """
    plt.figure(figsize=(8, 6))
    for filename, data_array in data_dict.items():
        x_values = data_array[:, 0]
        y_values = data_array[:, 1]
        plt.plot(x_values, y_values, label=filename)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Data from .sp Files')
    plt.legend()
    plt.show()




