# Define the Engine class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine

    def start(self):
        print(f"The {self.type_of_engine} engine is starting.")

# Define the Car class with composition
class Car:
    def __init__(self, make, model, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine  

    def start_car(self):
        print(f"{self.make} {self.model} is ready to go.")
        self.engine.start()  

engine = Engine("V8")
car = Car("Ford", "Mustang", engine)
car.start_car()  
