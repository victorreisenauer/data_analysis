import numpy as np

class Dataset:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data)
    

    @classmethod
    def from_array(cls, data: np.ndarray):
        new_data = {}
        for i in range(len(data)):
            new_data[i+1] = data[i]
        return cls(new_data)
    
        
    def as_dict(self) -> dict:
        return dict(sorted(self.data.items(), key=lambda x: x[0]))
    
    def as_array(self)-> np.ndarray:
        return np.array(list(self.data.values()))
    
    def give_sample_numbers(self):
        return np.array(list(self.data.keys()))
    
    def give_sample_intensities(self):
        return self.as_array()[:, :, 1]
    
    def give_sample_wavelengths(self):
        return self.as_array()[:, :, 0]
    
    def give_first_sample(self):
        """
        Returns the first sample from the dataset.

        Returns:
            tuple: A tuple containing the sample number, the wavelength column, and the intensity column.
        
        Example: num, xvals, yvals = ds2.give_last_sample()
        """
        return (self.give_sample_numbers()[0], self.as_array()[0][:, 0], self.as_array()[0][:, 1])
    
    def give_last_sample(self):
        return (self.give_sample_numbers()[0], self.as_array()[0][:, 0], self.as_array()[0][:, 1])
        
    
    

    

    