from helpers import build_data_dictionary, filter_dict_by_bounds
from graphic_creator import plot_data_arrays, plot_side_by_side_data
import numpy as np
from data_manager import DataManager
from dataset import Dataset
from figure_builder import FigureBuilder
import matplotlib.pyplot as plt


def plot_preliminary_tests():

    directory_path = '240405_preliminary PL testing of samples 1-20'
    data_dict = build_data_dictionary(directory_path)

    data_rp = filter_dict_by_bounds(data_dict, 1, 10)
    data_dj = filter_dict_by_bounds(data_dict, 11, 20)

    plot_side_by_side_data(data_rp, data_dj)

def compare_stages():
    data_dict= build_data_dictionary('240415_single_staticPL_samples 1 and 2 checkup')
    print(data_dict)
    plot_data_arrays(data_dict)

#compare_stages()



def plot_shift():
    dir_path = '240412_cont_staticPL_sample 2'
    data_dict = build_data_dictionary(dir_path)
    #print(data_dict)
    start = filter_dict_by_bounds(data_dict, 1, 3)
    end = filter_dict_by_bounds(data_dict, 88, 90)
    print(start)
    #plot_data_arrays(start)

    #plot_side_by_side_data(start, end)

# plot_preliminary_tests()


"""
DataFinder.fetch_data('240405_preliminary PL testing of samples 1-20')

"""
dm = DataManager()

ds1 = dm.build_dataset_from("240411_cont_staticPL_sample_1")

fb = FigureBuilder()

ds2 = dm.build_dataset_from("240412_cont_staticPL_sample 2")

fb.compare_pseudoColorPlots(ds1, ds2)

