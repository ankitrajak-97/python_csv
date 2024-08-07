
import csv



class Vehicle:
    def __init__(self,company,model,color,year,cc,vtype):
        self.mfg_company=company
        self.model=model
        self.color=color
        self.mfg_year=year
        self.cubic_capacity=cc
        self.vehicle_type=vtype

    def csv_row(self):
        return [self.mfg_company,self.model,self.color,self.mfg_year,self.cubic_capacity,self.vehicle_type]    
    
    def getheaders(self):
        return ['Mfg_company','Model','Color','Mfg_year','CC','Vehicle_type']


class CSVWriter:
    def __init__(self, filename, fieldnames):
        self.filename = filename
        self.fieldnames = fieldnames

    def write_header(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def write_data(self, objects):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            for obj in objects:
                writer.writerow(obj.csv_row())


car1 = Vehicle('Tata','Hector','Black',2014,2000,'Petrol')
car2 = Vehicle('Hyundai','Creta','Blue',2015,2300,'Diesel')
car3 = Vehicle('Maruti','Dzire','Green',2014,1400,'Petrol')
car4 = Vehicle('Kia','Vans','Red',2000,1300,'Petrol')
print(car1.color)
csv_writer = CSVWriter('car.csv',Vehicle.getheaders(''))


csv_writer.write_header()


csv_writer.write_data([car1, car2, car3 , car4])

    



     

