# Input parameters
I = 1.9  # Current
K = 0.9  # Duty Cycle
f = 30000  # Switching Frequency
Vin = 24
Vo = Vin * K  # Output Voltage of Buck Converter
I_del = (I / 100) * 5  # Delta I = 5% of I
V_del = (Vo / 100) * 5  # Delta Vo = 5% of Vo

# Capacitor Sizing
L = (Vo * (Vin - Vo)) / (I_del * f * Vin)

# Inductor Sizing
C = I_del / (8 * f * V_del)

# Function to format value with appropriate unit prefix
def format_value(value, unit):
    prefixes = ['p', 'n', 'u', 'm', '', 'k', 'M', 'G']
    exponents = [-12, -9, -6, -3, 0, 3, 6, 9]
    
    if value == 0:
        return f"0 {unit}"  # Handle zero case
    
    # Find the appropriate prefix
    exponent = floor(log10(abs(value)) / 3) * 3
    exponent = max(min(exponent, 9), -12)  # Clamp to valid range
    idx = min(range(len(exponents)), key=lambda i: abs(exponents[i] - exponent))
    prefix = prefixes[idx]
    
    # Scale the value
    scaled_value = value / (10 ** exponents[idx])
    
    # Format the output
    return f"{scaled_value:.4f} {prefix}{unit}"

# Display L and C with appropriate units
from math import log10, floor

L_formatted = format_value(L, 'H')
C_formatted = format_value(C, 'F')

print(f"Inductor (L): {L_formatted}")
print(f"Capacitor (C): {C_formatted}")