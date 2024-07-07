CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
 
def convert_to_celsius(temp):   
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(temp):    
    return temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
         
            temp  = float(input("Enter the temperature to convert:"))                 

            scale = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
            
            if scale == 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp:.2f}°F.")
            elif scale == 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}°F is {converted_temp:.2f}°C.")
            else:
                print("Invalid temperature. Please enter a numeric value.")

            cont = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

      

if __name__ == "__main__":
    main()