"""
@Author: Abdul Rehman
Created on: 08/8/2023

"""


class Cars:
    def __init__(self, *args, **kwargs):
        """
        Initialize a Cars object with provided arguments and keyword arguments.

        Args:
            *args: Variable positional arguments (make, model, year).
            **kwargs: Variable keyword arguments (color, price, mileage).
        """
        # Set attributes using provided arguments and keyword arguments
        self.make = args[0] if args else None
        self.model = args[1] if len(args) > 1 else None
        self.year = args[2] if len(args) > 2 else None
        self.color = kwargs.get('color', 'Unknown')  # Default to 'Unknown' if not provided
        self.price = kwargs.get('price', 'Unknown')  # Default to 'Unknown' if not provided
        self.mileage = kwargs.get('mileage', 'Unknown')  # Default to 'Unknown' if not provided

    def display(self):
        """
        Display the details of the car.
        """
        print("Vehicle Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(f"Mileage: {self.mileage}")


# Example Usage:
car1 = Cars('Toyota', 'Camry', 2020, color='Blue', price='$25,000', mileage='35,000')
car2 = Cars('Honda', 'Civic', 2018, color='Red', price='$20,000')
car3 = Cars('Ford', 'Focus', 2019, price='$18,000', mileage='28,000')

car1.display()
print("\n")
car2.display()
print("\n")
car3.display()
