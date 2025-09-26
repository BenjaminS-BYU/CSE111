# Benjamin Strong CSE111 September 2025
# Things I added or changed:
# Changed some magic numbers to named constants for clarity like EARTH_ACCELERATION_OF_GRAVITY and WATER_DYNAMIC_VISCOSITY
# Added a function to convert kilopascals to psi and used it in main, also added tests for it in the test file
# Added both psi and kPa to the final output for user convenience
# Also added some comments for clarity such as the function docstrings and comments in main and 
# the other functions for what they do
# Added some return value checks to ensure no negative values are returned inappropriately



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
WATER_DENSITY = 998.2000000                 # density of water (998.2 kilogram / meter^3)
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500 # (meters / second^2)
WATER_DYNAMIC_VISCOSITY = 0.0010016 # (pascal second) (0.0010016 kilogram / (meter second))
PSI_UNITS = 0.1450377377 # (pounds per square inch) / (kilopascal)

def main():
    """Calculate the water pressure at a house given user inputs."""
    print("This program calculates the water pressure at a house.")
    print("Please enter the following information:")
    # Get user inputs.
    # All inputs are in metric units (meters, seconds, kilopascals).
    # The output pressure is in kilopascals and converted to psi for convenience.
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_psi = convert_to_psi(pressure)
    print(f"Pressure at house: {pressure_psi:.1f}psi or {pressure:.1f}kPa")

def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column in meters."""
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from a height of water in kilopascals."""
    p = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return p if p > 0 else 0

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss from a length of pipe in kilopascals."""
    numerator = -friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate the pressure loss from pipe fittings in kilopascals."""
    return (-0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number (unitless)."""
    r = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return r if r > 0 else 0

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate the pressure loss from a pipe diameter reduction in kilopascals."""
    k=(.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    p = (-k * WATER_DENSITY * (fluid_velocity ** 2) )/ 2000
    return p 

def convert_to_psi(kilopascals):
    """Convert kilopascals to pounds per square inch (psi) for user convenience."""
    return kilopascals * PSI_UNITS


if __name__ == "__main__":
    main()