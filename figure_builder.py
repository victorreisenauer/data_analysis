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

    def pseudoColorPlot(self, dataset :Dataset, showline=False):

        plt.figure(figsize=(8, 6))
    
        x = dataset.give_sample_wavelengths()
        y = dataset.give_sample_numbers()
        z = dataset.give_sample_intensities()

        if showline:
            first_sample = dataset.give_first_sample()
            max_index = np.argmax(first_sample[2])
            max_wavelength = first_sample[1][max_index]
            plt.axvline(x=max_wavelength, color='r', linestyle='--')

        im = plt.pcolormesh(x, y, z)
        plt.colorbar(im)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    def compare_pseudoColorPlots(self, dataset1 :Dataset, dataset2 :Dataset, showline=False):
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))  # Create a figure with two subplots

        # Plot data from dataset1 (subplot 1)
        axes[0].set_title('Data from Dataset 1')  # Set title for subplot 1
        x1 = dataset1.give_sample_wavelengths()
        y1 = dataset1.give_sample_numbers()
        z1 = dataset1.give_sample_intensities()
        im1 = axes[0].pcolormesh(x1, y1, z1)
        plt.colorbar(im1, ax=axes[0])
        axes[0].set_xlabel('X')
        axes[0].set_ylabel('Y')

        if showline:
            self._add_showline(axes[0], dataset1)

        # Plot data from dataset2 (subplot 2)
        axes[1].set_title('Data from Dataset 2')  # Set title for subplot 2
        x2 = dataset2.give_sample_wavelengths()
        y2 = dataset2.give_sample_numbers()
        z2 = dataset2.give_sample_intensities()
        im2 = axes[1].pcolormesh(x2, y2, z2)
        plt.colorbar(im2, ax=axes[1])
        axes[1].set_xlabel('X')
        axes[1].set_ylabel('Y')

        if showline:
            self._add_showline(axes[1], dataset2)

        # Adjust layout and display the plots
        plt.tight_layout()
        plt.show()

    def _add_showline(self, ax, dataset: Dataset):
        first_sample = dataset.give_first_sample()
        max_index = np.argmax(first_sample[2])
        max_wavelength = first_sample[1][max_index]
        ax.axvline(x=max_wavelength, color='r', linestyle='--')
    
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
