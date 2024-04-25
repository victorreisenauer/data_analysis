import numpy as np
from data_manager import DataManager
from dataset import Dataset
from figure_builder import FigureBuilder


dm = DataManager()
fb = FigureBuilder()

ds1 = dm.build_dataset_from("240411_cont_staticPL_sample_1")
ds2 = dm.build_dataset_from("240412_cont_staticPL_sample 2")



fb.compare_pseudoColorPlots(ds1, ds2, showline=True)

