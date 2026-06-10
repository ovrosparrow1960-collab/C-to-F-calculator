import streamlit as st

# --- Calculation Function ---
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# --- App Layout ---
def main():
    st.title("Temperature Converter")
    st.write("Convert Celsius (°C) to Fahrenheit (°F) instantly.")
    st.markdown("---")  # Visual separator line
    
    st.header("Input Temperature:")
    
    # Input box for Celsius
    celsius = st.number_input("Enter temperature in Celsius (°C)", value=0.0)
    
    # Conversion Button
    if st.button("Convert to Fahrenheit"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()