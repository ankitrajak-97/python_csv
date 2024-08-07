import main
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