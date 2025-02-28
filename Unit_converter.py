import streamlit as st
import pandas as pd

def main():
    st.title("Unit Converter")
    st.write("### by MOIZ MANSOORI")    

    # Defining the conversion categories and their units
    categories = {
        "Length": {
            "Nanometer": 1e-9,
            "Micrometer": 1e-6,
            "Millimeter": 1e-3,
            "Centimeter": 1e-2,
            "Meter": 1,
            "Kilometer": 1e3,
            "Inch": 0.0254,
            "Foot": 0.3048,
            "Yard": 0.9144,
            "Mile": 1609.34,
            "Nautical mile": 1852
        },
        "Mass": {
            "Microgram": 1e-9,
            "Milligram": 1e-6,
            "Gram": 1e-3,
            "Kilogram": 1,
            "Metric ton": 1e3,
            "Ounce": 0.0283495,
            "Pound": 0.453592,
            "Stone": 6.35029,
            "US ton": 907.185,
            "Imperial ton": 1016.05
        },
        "Area": {
            "Square millimeter": 1e-6,
            "Square centimeter": 1e-4,
            "Square meter": 1,
            "Hectare": 10000,
            "Square kilometer": 1e+6,
            "Square inch": 0.00064516,
            "Square foot": 0.092903,
            "Square yard": 0.836127,
            "Acre": 4046.86,
            "Square mile": 2.59e+6
        },
        "Data Transfer Rate": {
            "Bit per second": 1,
            "Kilobit per second": 1e3,
            "Megabit per second": 1e6,
            "Gigabit per second": 1e9,
            "Terabit per second": 1e12,
            "Byte per second": 8,
            "Kilobyte per second": 8e3,
            "Megabyte per second": 8e6,
            "Gigabyte per second": 8e9,
            "Terabyte per second": 8e12
        },
        "Digital Storage": {
            "Bit": 1,
            "Kilobit": 1e3,
            "Megabit": 1e6,
            "Gigabit": 1e9,
            "Terabit": 1e12,
            "Petabit": 1e15,
            "Byte": 8,
            "Kilobyte": 8e3,
            "Megabyte": 8e6,
            "Gigabyte": 8e9,
            "Terabyte": 8e12,
            "Petabyte": 8e15
        },
        "Energy": {
            "Joule": 1,
            "Kilojoule": 1e3,
            "Calorie": 4.184,
            "Kilocalorie": 4184,
            "Watt hour": 3600,
            "Kilowatt hour": 3.6e6,
            "Electronvolt": 1.602e-19,
            "British thermal unit": 1055.06,
            "US therm": 1.055e+8,
            "Foot-pound": 1.35582
        },
        "Frequency": {
            "Hertz": 1,
            "Kilohertz": 1e3,
            "Megahertz": 1e6,
            "Gigahertz": 1e9,
            "Terahertz": 1e12,
            "RPM": 1/60
        },
        "Fuel Economy": {
            "Miles per gallon (US)": 1,
            "Miles per gallon (UK)": 1.20095,
            "Kilometer per liter": 0.425144,
            "Liter per 100 kilometers": lambda x: 235.215/x, 
            "Miles per liter": 0.264172
        },
        "Plane Angle": {
            "Degree": 1,
            "Gradian": 0.9,
            "Milliradian": 0.057296,
            "Minute of arc": 1/60,
            "Radian": 57.2958,
            "Second of arc": 1/3600
        },
        "Pressure": {
            "Pascal": 1,
            "Kilopascal": 1e3,
            "Megapascal": 1e6,
            "Bar": 1e5,
            "Pound per square inch": 6894.76,
            "Torr": 133.322,
            "Millimeter of mercury": 133.322,
            "Atmosphere": 101325,
            "Inch of mercury": 3386.39
        },
        "Speed": {
            "Centimeter per second": 0.01,
            "Meter per second": 1,
            "Kilometer per hour": 0.277778,
            "Foot per second": 0.3048,
            "Mile per hour": 0.44704,
            "Knot": 0.514444,
            "Speed of light": 299792458
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K"
        },
        "Time": {
            "Nanosecond": 1e-9,
            "Microsecond": 1e-6,
            "Millisecond": 1e-3,
            "Second": 1,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800,
            "Month": 2.628e+6,
            "Year": 3.154e+7,
            "Decade": 3.154e+8,
            "Century": 3.154e+9
        },
        "Volume": {
            "Milliliter": 1e-6,
            "Cubic centimeter": 1e-6,
            "Liter": 1e-3,
            "Cubic meter": 1,
            "Gallon (US)": 0.00378541,
            "Quart (US)": 0.000946353,
            "Pint (US)": 0.000473176,
            "Cup (US)": 0.000236588,
            "Fluid ounce (US)": 2.9574e-5,
            "Gallon (UK)": 0.00454609,
            "Quart (UK)": 0.00113652,
            "Pint (UK)": 0.000568261,
            "Cup (UK)": 0.000284131,
            "Fluid ounce (UK)": 2.84131e-5
        }
    }

    category = st.sidebar.selectbox("Select category", list(categories.keys()))
    
    col1, col2 = st.columns(2)
    
    # Get units for selected category
    units = list(categories[category].keys())
    
    with col1:
        st.subheader("From")
        from_unit = st.selectbox("From Unit", units, key="from_unit")
        input_value = st.number_input("Enter value", value=1.0, format="%.10f", key="input")
    
    with col2:
        st.subheader("To")
        to_unit = st.selectbox("To Unit", units, key="to_unit")
        
    if category == "Temperature":

        if input_value is not None:
            result = convert_temperature(input_value, from_unit, to_unit)
            
            with col2:
                st.success(f"{result:.10g}")
    elif category == "Fuel Economy" and (callable(categories[category][from_unit]) or callable(categories[category][to_unit])):
        
        if input_value is not None:
            result = convert_fuel_economy(input_value, from_unit, to_unit, categories[category])
            
            with col2:
                st.success(f"{result:.10g}")
    else:
        
        if input_value is not None:
            from_factor = categories[category][from_unit]
            to_factor = categories[category][to_unit]
            
            result = input_value * (from_factor / to_factor)
            
            with col2:
                st.success(f"{result:.10g}")
    
    # Display conversion formula
    st.markdown("---")
    st.subheader("Conversion Formula:")
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            st.write("°F = (°C × 9/5) + 32")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            st.write("°C = (°F - 32) × 5/9")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            st.write("K = °C + 273.15")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            st.write("°C = K - 273.15")
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            st.write("K = (°F - 32) × 5/9 + 273.15")
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            st.write("°F = (K - 273.15) × 9/5 + 32")
    elif category == "Fuel Economy":
        if from_unit == "Liter per 100 kilometers" or to_unit == "Liter per 100 kilometers":
            if from_unit == "Liter per 100 kilometers":
                st.write(f"{to_unit} = 235.215 / (L/100km)")
            else:
                st.write(f"L/100km = 235.215 / ({from_unit})")
        else:
            from_factor = categories[category][from_unit]
            to_factor = categories[category][to_unit]
            st.write(f"1 {from_unit} = {from_factor/to_factor:.10g} {to_unit}")
    else:
        from_factor = categories[category][from_unit]
        to_factor = categories[category][to_unit]
        st.write(f"1 {from_unit} = {from_factor/to_factor:.10g} {to_unit}")

    st.markdown("---")
    st.subheader(f"Common {category} Conversions")
    
    if category == "Temperature":

        temps = [-40, 0, 20, 37, 100, 212] if from_unit == "Celsius" else \
               [-40, 32, 68, 98.6, 212, 400] if from_unit == "Fahrenheit" else \
               [233.15, 273.15, 293.15, 310.15, 373.15, 485.15]
        
        common_conversions = {}
        for temp in temps:
            row = {}
            for unit in units:
                if unit != from_unit:
                    row[unit] = convert_temperature(temp, from_unit, unit)
            common_conversions[f"{temp} {from_unit}"] = row
        
        df = pd.DataFrame(common_conversions).T
        st.dataframe(df)
    elif category == "Fuel Economy":

        base_values = [5, 10, 15, 20, 25, 30]
        
        common_conversions = {}
        for base in base_values:
            converted_values = {}
            for unit in units:
                if unit != from_unit:
                    converted_values[unit] = convert_fuel_economy(base, from_unit, unit, categories[category])
            
            common_conversions[f"{base} {from_unit}"] = converted_values
        
        df = pd.DataFrame(common_conversions).T
        st.dataframe(df)
    else:
        common_conversions = {}
        base_values = [0.1, 0.5, 1, 2, 5, 10, 100]
        
        for base in base_values:
            converted_values = {}
            for unit in units:
                if unit != from_unit:
                    from_factor = categories[category][from_unit]
                    to_factor = categories[category][unit]
                    converted_values[unit] = base * (from_factor / to_factor)
            
            common_conversions[f"{base} {from_unit}"] = converted_values
        
        df = pd.DataFrame(common_conversions).T
        st.dataframe(df)

def convert_temperature(value, from_unit, to_unit):
    
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value
    
    if to_unit == "Fahrenheit":
        return celsius * 9/5 + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return celsius

def convert_fuel_economy(value, from_unit, to_unit, units_dict):
    """ For fuel economy, we need to handle L/100km specially
        First convert to MPG (US) as base unit """
    if from_unit == "Liter per 100 kilometers":
        mpg_us = 235.215 / value
    else:
        from_factor = units_dict[from_unit]
        mpg_us = value / from_factor
    
    # Then convert from MPG (US) to target
    if to_unit == "Liter per 100 kilometers":
        return 235.215 / mpg_us
    else:
        to_factor = units_dict[to_unit]
        return mpg_us * to_factor

if __name__ == "__main__":
    main()