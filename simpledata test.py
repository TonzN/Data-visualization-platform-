import pandas as pd
import numpy as np
import random

testdata = np.random.randint(0, 20, 5)      

available_formats = {
    "Array": "Array"
}
 
class dataobject:
    def __init__(self, format):
        if format in available_formats:
            self.format = format
        else:
            raise TypeError("Format is not supported!")
    
    def __Arr_To_Df(self, data, column_names = False):
        if isinstance(column_names, (list, np.ndarray)):
            return pd.DataFrame(data, columns=column_names)
        return pd.DataFrame(data)
            
    def create(self, data, is_proccessed=False, column_names = False):
        if is_proccessed:
            pass
        else:
            if available_formats[self.format] == "Array":
                if isinstance(data, np.ndarray):
                    if not column_names:
                        self.dataframe = self.__Arr_To_Df(data)
                    else:
                        if not isinstance(column_names, (list, np.ndarray)):
                            column_names = np.array([column_names])
                        self.dataframe = self.__Arr_To_Df(data, column_names)
                else:
                    raise TypeError("Array must be a numpy ndarray")
        
columns = ["numbers"]
test = dataobject(format="Array")
test.create(testdata, column_names=columns)
print(test.dataframe["numbers"].values)
