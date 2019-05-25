class Vehicle:
   name=" "
   max_speed=0
   number_of_cylinders=0
   def __str__(self):
       return "Vehicle_name="+self.name+', max_speed='+str(self.max_speed)+', number_of_cylinders='+str(self.number_of_cylinders)
class Car(Vehicle):
   def __init__(self,vehicle_name, vehicle_speed,number_Of_cylinders):
       self.name =vehicle_name
       self.max_speed =vehicle_speed
       self.number_of_cylinders=number_Of_cylinders
   def mutator(self,max):
       self.max_speed=max
   def accessor(self):
       print("Vehicle_name="+self.name+', max_speed='+str(self.max_speed)+', number_of_cylinders='+str(self.number_of_cylinders))
   def __str__(self):
       return "Vehicle_name="+self.name+', max_speed='+str(self.max_speed)+', number_of_cylinders='+str(self.number_of_cylinders)
class Airplane(Vehicle):
   def __init__(self,vehicle_name, vehicle_speed,number_Of_cylinders):
       self.name =vehicle_name
       self.max_speed =vehicle_speed
       self.number_of_cylinders=number_Of_cylinders
   def mutator(self,max):
       self.max_speed=max
   def accessor(self):
       print("Vehicle_name="+self.name+', max_speed='+str(self.max_speed)+', number_of_cylinders='+str(self.number_of_cylinders))
   def __str__(self):
       return "Vehicle_name="+self.name+', max_speed='+str(self.max_speed)+', number_of_cylinders='+str(self.number_of_cylinders)
if __name__ == "__main__":
   car_instance=Car("ford",100,5)
   print(car_instance)
   car_instance.mutator(200)
   print(car_instance.accessor())
   Airplane_instance=Airplane("kingfisher",300,7)
   print(Airplane_instance)
   Airplane_instance.mutator(500)
   print(Airplane_instance.accessor())
   Vehicle_instance=Vehicle()
   print(Vehicle_instance)
   if(car_instance.max_speed<Airplane_instance.max_speed):
       print("Airplane is speed")
   else:
       print("Car is speed")