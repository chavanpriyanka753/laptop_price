import pickle
import numpy as np
from flask import jsonify

class laptop_price():
    def __init__(self, data):
        self.data = data

    def load_model(self):
        with open(r'artifacts/model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self):
        self.load_model()

        Company	= self.data['Company']
        TypeName = self.data['TypeName']
        Ram	= int(self.data['Ram'])
        Weight = float(self.data['Weight'])
        Touchscreen	= self.data['Touchscreen']
        HD = self.data['HD']
        IPS	= self.data['IPS']
        Cpu_Brand = self.data['Cpu_Brand']
        HDD	= int(self.data['HDD'])
        SSD	= int(self.data['SSD'])
        Gpu_Brand = self.data['Gpu_Brand']
        Os = self.data['Os']
        Resolution = self.data['Resolution']
        Screen_size = float(self.data['Screen_size'])

        x_res = int(Resolution.split('*')[0])
        y_res = int(Resolution.split('*')[1])

        ppi = ((x_res**2) + (y_res**2))**0.5 / Screen_size

        if Company == 'Dell':
            Company = 0
        elif Company == 'Lenovo':
            Company = 1
        elif Company == 'HP':
            Company = 2
        elif Company == 'Asus':
            Company = 3
        elif Company == 'Acer':
            Company = 4
        elif Company == 'MSI':
            Company = 5
        elif Company == 'Toshiba':
            Company = 6
        elif Company == 'Apple':
            Company = 7
        elif Company == 'Samsung':
            Company = 8
        elif Company == 'Razer':
            Company = 9
        elif Company == 'Mediacom':
            Company = 10
        elif Company == 'Microsoft':
            Company = 11
        elif Company == 'Xiaomi':
            Company = 12
        elif Company == 'Vero':
            Company = 13
        elif Company == 'Chuwi':
            Company = 14
        elif Company == 'Google':
            Company = 15
        elif Company == 'Fujitsu':
            Company = 16
        elif Company == 'LG':
            Company = 17
        elif Company == 'Huawei':
            Company = 18

        if TypeName == 'Notebook':
            TypeName = 0
        elif TypeName == 'Gaming':
            TypeName = 1
        elif TypeName == 'Ultrabook':
            TypeName = 2
        elif TypeName == '2 in 1 Convertible':
            TypeName = 3
        elif TypeName == 'Workstation':
            TypeName = 4
        elif TypeName == 'Netbook':
            TypeName = 5

        if Cpu_Brand == 'Intel Core i7':
            Cpu_Brand = 0
        elif Cpu_Brand == 'Intel Core i5':
            Cpu_Brand = 1
        elif Cpu_Brand == 'Other Intel Processor':
            Cpu_Brand = 2
        elif Cpu_Brand == 'Intel Core i3':
            Cpu_Brand = 3
        elif Cpu_Brand == 'AMD Processor':
            Cpu_Brand = 4 

        if Gpu_Brand  == 'Intel':
            Gpu_Brand = 0
        elif Gpu_Brand == 'Nvidia':
            Gpu_Brand = 1
        elif Gpu_Brand == 'AMD':
            Gpu_Brand = 2

        if Os  == 'Windows':
            Os = 0
        elif Os == 'Nvidia':
            Os = 1
        elif Os == 'Others/No OS/Linux':
            Os = 2

        if Touchscreen == 'YES':
            Touchscreen = 1
        else:
            Touchscreen = 0

        if HD == 'YES':
            HD = 1
        else:
            HD = 0

        if IPS == 'YES':
            IPS = 1
        else:
            IPS = 0 
        
        array = np.array([Company, TypeName, Ram, Weight, Touchscreen, HD, IPS, ppi, Cpu_Brand, HDD, SSD, Gpu_Brand, Os])
        array = array.reshape(1, 13)
        result = int((self.model.predict(array)[0]))
        return result
