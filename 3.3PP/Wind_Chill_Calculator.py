"""
Wind Chill Calculator 3.3PP
"""

__author__ = "Samuel Morriss"

def calculate_wind_chill(air_temp:float, wind_speed:float) -> float:
    """
    Function to Calculate wind chill.
    """
    return round(13.12 + (0.6215 * air_temp) - (11.37 * pow(wind_speed, 0.16)) + (0.3965 * air_temp * pow(wind_speed, 0.16)), 2)


def main():
    air_temp_1 = 0
    wind_speed_1 = 20
    
    air_temp_2 = -5
    wind_speed_2 = 40
    
    print("Wind Chill Calculation")
    print()
    
    print(f"Wind chill for case 1 is: T={air_temp_1}°C and V={wind_speed_1} km/h: {calculate_wind_chill(air_temp_1, wind_speed_1)}°C")
    print(f"Wind chill for case 2 is: T={air_temp_2}°C and V={wind_speed_2} km/h: {calculate_wind_chill(air_temp_2, wind_speed_2)}°C")
    print()
    
    air_temp = float(input("What is the ambient air temperature? (°C) "))
    wind_speed = float(input("What is the current wind speed? (km/h) "))
    print()
    
    print(f"The current wind chill temperature is: {calculate_wind_chill(air_temp, wind_speed)}°C")


if __name__ == "__main__":
    main()