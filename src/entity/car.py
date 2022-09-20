
class Car:
    
    def __init__(self,record:dict):
        for k,v in record.items():
            setattr(self,k,v)
        
        self.record=record
   
    @staticmethod
    def dict_to_car(data:dict,ctx):
        print(data,ctx)
        return Car(record=data)


    


    
    def __str__(self):
        return f"{self.record}"