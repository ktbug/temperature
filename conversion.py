def kelvin_to_celsius(temp):
    """Convert a temperature"""
    
	return temp - 273.15

def celsius_to_fahr(temp):
    """" Another one"""
	return temp*(9/5) +32

def kelvin_to_fahr(temp):
    """"Comment Again """
	temp_c = kelvin_to_celsius(temp)
	result = celsius_to_fahr(temp_c)
	return result
