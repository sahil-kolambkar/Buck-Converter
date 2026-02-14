# Input parameters
I = 1.9  # Current
K = 0.99  # Duty Cycle
Vin = 24  # Input voltage
Vo = Vin * K  # Output voltage of Buck Converter
I_del = (I / 100) * 5  # Delta I = 5% of I
V_del = (Vo / 100) * 5  # Delta Vo = 5% of Vo

# Function to parse inductor value with unit prefix
def parse_inductor_value(value_str):
    # Define unit prefixes and their corresponding multipliers
    prefixes = {
        'p': 1e-12,  # pico
        'n': 1e-9,   # nano
        'u': 1e-6,   # micro
        'µ': 1e-6,   # micro (alternative symbol)
        'm': 1e-3,  # milli
        '': 1,       # no prefix (base unit)
        'k': 1e3,    # kilo
        'M': 1e6,    # mega
        'G': 1e9     # giga
    }
    
    # Extract the numeric part and the unit prefix
    for i, char in enumerate(value_str):
        if not char.isdigit() and char != '.':
            break
    numeric_part = value_str[:i]
    unit_prefix = value_str[i:].strip()
    
    # Convert to float and apply the multiplier
    try:
        numeric_value = float(numeric_part)
        multiplier = prefixes.get(unit_prefix, 1)  # Default to 1 if prefix is unknown
        return numeric_value * multiplier
    except ValueError:
        raise ValueError(f"Invalid inductor value: {value_str}")

# Input inductor value with unit (e.g., 12m, 12u, 9n, etc.)
L_input = input("Enter inductor value : ")
L = parse_inductor_value(L_input)  # Convert to henry

# Calculate switching frequency (f)
f = (Vo * (Vin - Vo)) / (I_del * L * Vin)

# Capacitor sizing
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

# Display results with appropriate units
from math import log10, floor

f_formatted = format_value(f, 'Hz')
C_formatted = format_value(C, 'F')

print(f"Switching Frequency (f): {f_formatted}")
#print(f"Capacitor (C): {C_formatted}")