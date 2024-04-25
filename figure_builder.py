from dataset import Dataset
import numpy as np
import matplotlib.pyplot as plt


class FigureBuilder:

    def plot_side_by_side(self, dataset1: Dataset, dataset2: Dataset):
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))  # Create a figure with two subplots

        # Plot data from dataset1 (subplot 1)
        axes[0].set_title('Data from Dataset 1')  # Set title for subplot 1
        for filename, data_array in sorted(dataset1.as_dict().items()):
            x_values = data_array[:, 0]
            y_values = data_array[:, 1]
            axes[0].plot(x_values, y_values, label=filename)
        axes[0].set_xlabel('X')
        axes[0].set_ylabel('Y')
        axes[0].legend()

        # Plot data from dataset2 (subplot 2)
        axes[1].set_title('Data from Dataset 2')  # Set title for subplot 2
        for filename, data_array in sorted(dataset2.as_dict().items()):
            x_values = data_array[:, 0]
            y_values = data_array[:, 1]
            axes[1].plot(x_values, y_values, label=filename)
        axes[1].set_xlabel('X')
        axes[1].set_ylabel('Y')
        axes[1].legend()

        # Adjust layout and display the plots
        plt.tight_layout()
        plt.show()

    def pseudoColorPlot(self, dataset :Dataset):

        plt.figure(figsize=(8, 6))
    
        x = dataset.give_sample_wavelengths()
        y = dataset.give_sample_numbers()
        z = dataset.give_sample_intensities()

        im = plt.pcolormesh(x, y, z)
        plt.colorbar(im)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()


    
    def quickPlot(self, dataset :Dataset):
        plt.figure(figsize=(8, 6))
        for filename, data_array in dataset.as_dict().items():
            x_values = data_array[:, 0]
            y_values = data_array[:, 1]
            plt.plot(x_values, y_values, label=filename)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()
