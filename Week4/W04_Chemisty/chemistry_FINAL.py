# Benjamin Strong W04 Chemisty FINAL CSE111
# I added a .txt file with the periodic table data to read from.
# Then created two separate lists to zip into a dictionary. Hope this is okay. 
# This way made more sense to me so that I have the data of the periodic table in a separate file.
# Then stored the dictionary in the periodic_table_dict variable to call later. Testing file works great.

# Things I added:
# 1. I added a while loop to keep asking the user for new formulas till they say done
# 2. Added a dictionary of generally used chemical compounds so you can just enter the word and the program will find the associated value to 
# insert into the formula, water - H2O
# 3. I was having trouble with inputs and the testing so with ChatGPTs help I added a way to know when the program is being tested 
# It will then make the grams a base amount for testing. I don't know if that is the right way to do this, but it works :)
# 4. Added a try except for any input that can't be calculated into a compound formula (ChatGPT help a little bit with this one)

### All input from AI has been heavily parsed through by me and I wrote it out into my own code. ###

import os
from formula import parse_formula

chemicals = {
    # Everyday Compounds
    "water": "H2O",
    "sodium chloride": "NaCl",
    "sodium bicarbonate": "NaHCO3",   # baking soda
    "acetic acid": "CH3COOH",         # vinegar
    "glucose": "C6H12O6",
    "ethanol": "C2H5OH",
    "carbon dioxide": "CO2",
    "oxygen": "O2",
    "nitrogen": "N2",

    # Acids
    "hydrochloric acid": "HCl",
    "sulfuric acid": "H2SO4",
    "nitric acid": "HNO3",
    "phosphoric acid": "H3PO4",
    "carbonic acid": "H2CO3",

    # Bases
    "sodium hydroxide": "NaOH",
    "potassium hydroxide": "KOH",
    "ammonia": "NH3",
    "calcium hydroxide": "Ca(OH)2",

    # Salts and Minerals
    "calcium carbonate": "CaCO3",
    "sodium carbonate": "Na2CO3",
    "magnesium sulfate": "MgSO4",     # epsom salt
    "potassium nitrate": "KNO3",      # saltpetre
    "ammonium chloride": "NH4Cl",

    # Gases and Simple Hydrocarbons
    "methane": "CH4",
    "propane": "C3H8",
    "butane": "C4H10",
    "hydrogen": "H2",
    "ozone": "O3",

    # Organic Compounds
    "melatonin": "C13H16N2O2",
    "benzene": "C6H6"
}



def main():
    """Make the periodic dictionary. Get input from the user for a chemical compound then the grams, check to make sure
    the input it valid, then pass it through the parse_formula to get the formula to calculate"""
    
    periodic_table_dict = make_periodic_table()
    
    while True:

        user_input = input("Enter a chemical formula or name ('stop' to exit): ")
        if user_input.lower() == "stop":
            break

        chem_formula = ''

        if user_input.lower() in chemicals:
            chem_formula = chemicals[user_input.lower()]
            print(f"The compound for {user_input} is: {chem_formula}")

        # If the characters in user input is all letter or all numbers or all uppercase then we go on
        elif any(char.isupper() for char in user_input):
            chem_formula = user_input
            
        else:
            print(f"Sorry {user_input} is not accepted, try again please.")
            continue
        try:
            symbol_convert = parse_formula(chem_formula, periodic_table_dict)
            compute_molar_mass(symbol_convert, periodic_table_dict)
        except:
            print(f"Error: {user_input} isn't a valid compound chemical")
        

def make_periodic_table():
    """returns a dictionary that contains all of the elements in the periodic table
    where the keys are the chemical symbols and the values are lists of the name and atomic mass."""
    periodic_table_dict = {}

    list_of_elements = []
    list_of_name_and_mass = []

    with open("periodic_table.txt") as file:
        next(file)  # Skip the header line.
        for line in file:
            clean_line = line.split(",")
            elements = clean_line[0]
            name_and_mass = [clean_line[1], float(clean_line[2])]
            list_of_elements.append(elements.strip())
            list_of_name_and_mass.append(name_and_mass)

    periodic_table_dict = dict(zip(list_of_elements, list_of_name_and_mass))
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict) -> float:
    """Compute and return the total molar mass of all the elements listed in symbol_quantity_list."""

    # Added this for pytesting, ChatGPT helped out with this
    if "PYTEST_CURRENT_TEST" in os.environ:
        amount_in_grams = 25.04
    else:
        amount_in_grams = float(input("Enter amount in grams: "))
    molar_mass = 0

    for symbol, quantity in symbol_quantity_list:
        # Get the dictionaries key [symbol] and the second item in the value list [1]
        mass = periodic_table_dict[symbol][1]  # get atomic mass
        molar_mass += quantity * mass
    if molar_mass == 0:
        return 0

    moles = amount_in_grams / molar_mass

    print("-"*12)
    print(f"{molar_mass} grams/mole")
    print(f"{moles:.5f} moles")
    print("-"*12)
    return molar_mass

if __name__ == "__main__":
    main()




# My periodic_table.txt file just looks like this:

# SymbolNameAtomicMass
# Ac,Actinium,227
# Ag,Silver,107.8682
# Al,Aluminum,26.9815386
# Ar,Argon,39.948
# As,Arsenic,74.9216
# At,Astatine,210
# Au,Gold,196.966569
# B,Boron,10.811
# Ba,Barium,137.327
# Be,Beryllium,9.012182
# Bi,Bismuth,208.9804
# Br,Bromine,79.904
# C,Carbon,12.0107
# Ca,Calcium,40.078
# Cd,Cadmium,112.411
# Ce,Cerium,140.116
# Cl,Chlorine,35.453
# Co,Cobalt,58.933195
# Cr,Chromium,51.9961
# Cs,Cesium,132.9054519
# Cu,Copper,63.546
# Dy,Dysprosium,162.5
# Er,Erbium,167.259
# Eu,Europium,151.964
# F,Fluorine,18.9984032
# Fe,Iron,55.845
# Fr,Francium,223
# Ga,Gallium,69.723
# Gd,Gadolinium,157.25
# Ge,Germanium,72.64
# H,Hydrogen,1.00794
# He,Helium,4.002602
# Hf,Hafnium,178.49
# Hg,Mercury,200.59
# Ho,Holmium,164.93032
# I,Iodine,126.90447
# In,Indium,114.818
# Ir,Iridium,192.217
# K,Potassium,39.0983
# Kr,Krypton,83.798
# La,Lanthanum,138.90547
# Li,Lithium,6.941
# Lu,Lutetium,174.9668
# Mg,Magnesium,24.305
# Mn,Manganese,54.938045
# Mo,Molybdenum,95.96
# N,Nitrogen,14.0067
# Na,Sodium,22.98976928
# Nb,Niobium,92.90638
# Nd,Neodymium,144.242
# Ne,Neon,20.1797
# Ni,Nickel,58.6934
# Np,Neptunium,237
# O,Oxygen,15.9994
# Os,Osmium,190.23
# P,Phosphorus,30.973762
# Pa,Protactinium,231.03588
# Pb,Lead,207.2
# Pd,Palladium,106.42
# Pm,Promethium,145
# Po,Polonium,209
# Pr,Praseodymium,140.90765
# Pt,Platinum,195.084
# Pu,Plutonium,244
# Ra,Radium,226
# Rb,Rubidium,85.4678
# Re,Rhenium,186.207
# Rh,Rhodium,102.9055
# Rn,Radon,222
# Ru,Ruthenium,101.07
# S,Sulfur,32.065
# Sb,Antimony,121.76
# Sc,Scandium,44.955912
# Se,Selenium,78.96
# Si,Silicon,28.0855
# Sm,Samarium,150.36
# Sn,Tin,118.71
# Sr,Strontium,87.62
# Ta,Tantalum,180.94788
# Tb,Terbium,158.92535
# Tc,Technetium,98
# Te,Tellurium,127.6
# Th,Thorium,232.03806
# Ti,Titanium,47.867
# Tl,Thallium,204.3833
# Tm,Thulium,168.93421
# U,Uranium,238.02891
# V,Vanadium,50.9415
# W,Tungsten,183.84
# Xe,Xenon,131.293
# Y,Yttrium,88.90585
# Yb,Ytterbium,173.054
# Zn,Zinc,65.38
# Zr,Zirconium,91.224



# Expected outcome:
# periodic_table_dict = { # type: ignore
#         # symbol: [name, atomic_mass]
#         "Ac": ["Actinium", 227],
#         "Ag": ["Silver", 107.8682],
#         "Al": ["Aluminum", 26.9815386],
#         "Ar": ["Argon", 39.948],
#         "As": ["Arsenic", 74.9216],
#         "At": ["Astatine", 210],
#         "Au": ["Gold", 196.966569],
#         "B": ["Boron", 10.811],
#         "Ba": ["Barium", 137.327],
#         "Be": ["Beryllium", 9.012182],
#         "Bi": ["Bismuth", 208.9804],
#         "Br": ["Bromine", 79.904],
#         "C": ["Carbon", 12.0107],
#         "Ca": ["Calcium", 40.078],
#         "Cd": ["Cadmium", 112.411],
#         "Ce": ["Cerium", 140.116],
#         "Cl": ["Chlorine", 35.453],
#         "Co": ["Cobalt", 58.933195],
#         "Cr": ["Chromium", 51.9961],
#         "Cs": ["Cesium", 132.9054519],
#         "Cu": ["Copper", 63.546],
#         "Dy": ["Dysprosium", 162.5],
#         "Er": ["Erbium", 167.259],
#         "Eu": ["Europium", 151.964],
#         "F": ["Fluorine", 18.9984032],
#         "Fe": ["Iron", 55.845],
#         "Fr": ["Francium", 223],
#         "Ga": ["Gallium", 69.723],
#         "Gd": ["Gadolinium", 157.25],
#         "Ge": ["Germanium", 72.64],
#         "H": ["Hydrogen", 1.00794],
#         "He": ["Helium", 4.002602],
#         "Hf": ["Hafnium", 178.49],
#         "Hg": ["Mercury", 200.59],
#         "Ho": ["Holmium", 164.93032],
#         "I": ["Iodine", 126.90447],
#         "In": ["Indium", 114.818],
#         "Ir": ["Iridium", 192.217],
#         "K": ["Potassium", 39.0983],
#         "Kr": ["Krypton", 83.798],
#         "La": ["Lanthanum", 138.90547],
#         "Li": ["Lithium", 6.941],
#         "Lu": ["Lutetium", 174.9668],
#         "Mg": ["Magnesium", 24.305],
#         "Mn": ["Manganese", 54.938045],
#         "Mo": ["Molybdenum", 95.96],
#         "N": ["Nitrogen", 14.0067],
#         "Na": ["Sodium", 22.98976928],
#         "Nb": ["Niobium", 92.90638],
#         "Nd": ["Neodymium", 144.242],
#         "Ne": ["Neon", 20.1797],
#         "Ni": ["Nickel", 58.6934],
#         "Np": ["Neptunium", 237],
#         "O": ["Oxygen", 15.9994],
#         "Os": ["Osmium", 190.23],
#         "P": ["Phosphorus", 30.973762],
#         "Pa": ["Protactinium", 231.03588],
#         "Pb": ["Lead", 207.2],
#         "Pd": ["Palladium", 106.42],
#         "Pm": ["Promethium", 145],
#         "Po": ["Polonium", 209],
#         "Pr": ["Praseodymium", 140.90765],
#         "Pt": ["Platinum", 195.084],
#         "Pu": ["Plutonium", 244],
#         "Ra": ["Radium", 226],
#         "Rb": ["Rubidium", 85.4678],
#         "Re": ["Rhenium", 186.207],
#         "Rh": ["Rhodium", 102.9055],
#         "Rn": ["Radon", 222],
#         "Ru": ["Ruthenium", 101.07],
#         "S": ["Sulfur", 32.065],
#         "Sb": ["Antimony", 121.76],
#         "Sc": ["Scandium", 44.955912],
#         "Se": ["Selenium", 78.96],
#         "Si": ["Silicon", 28.0855],
#         "Sm": ["Samarium", 150.36],
#         "Sn": ["Tin", 118.71],
#         "Sr": ["Strontium", 87.62],
#         "Ta": ["Tantalum", 180.94788],
#         "Tb": ["Terbium", 158.92535],
#         "Tc": ["Technetium", 98],
#         "Te": ["Tellurium", 127.6],
#         "Th": ["Thorium", 232.03806],
#         "Ti": ["Titanium", 47.867],
#         "Tl": ["Thallium", 204.3833],
#         "Tm": ["Thulium", 168.93421],
#         "U": ["Uranium", 238.02891],
#         "V": ["Vanadium", 50.9415],
#         "W": ["Tungsten", 183.84],
#         "Xe": ["Xenon", 131.293],
#         "Y": ["Yttrium", 88.90585],
#         "Yb": ["Ytterbium", 173.054],
#         "Zn": ["Zinc", 65.38],
#         "Zr": ["Zirconium", 91.224]
#     }