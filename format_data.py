from scipy.interpolate import KroghInterpolator

def data_to_matrix():
    self.x_values = [key for key in self.data_dict.keys()]
    self.y_values =[val[0] for val in self.data_dict.values()]
    return self.x_values , self.y_values

dict1= {1:[2,3], 3:[4,5]}
data_to_function(dict1)
