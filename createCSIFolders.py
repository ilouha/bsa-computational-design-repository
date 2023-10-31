import os

# Define the parent directory where you want to create the folders
base_directory = r"C:\Users\ilouh\Documents\GitHub\bsa-computational-design-repository\testingFolder\XXXXX.X_20_Materials & FFE" # Replace with your actual base directory path

# List of subgroups and subcategories
subgroups = [
    "01_General Requirements",
    "02_Existing Conditions",
    "03_Concrete",
    "04_Masonry",
    "05_Metals",
    "06_Wood, Plastics, and Composites",
    "07_Thermal and Moisture Protection",
    "08_Openings",
    "09_Finishes",
    "10_Specialties",
    "11_Equipment",
    "12_Furnishings",
    "13_Special Construction",
    "14_Conveying Equipment",
    "21_Fire Suppression",
    "22_Plumbing",
    "23_Heating, Ventilating, and Air Conditioning (HVAC)",
    "25_Integrated Automation",
    "26_Electrical",
    "27_Communications",
    "28_Electronic Safety and Security",
    "31_Earthwork",
    "32_Exterior Improvements",
    "33_Utilities",
    "34_Transportation",
    "35_Waterway and Marine Construction",
    "40_Process Interconnections",
    "41_Material Processing and Handling Equipment",
    "42_Process Heating, Cooling, and Drying Equipment",
    "43_Process Gas and Liquid Handling, Purification and Storage Equipment",
    "44_Pollution and Waste Control Equipment",
    "45_Industry-Specific Manufacturing Equipment",
    "46_Water and Wastewater Equipment",
    "48_Electrical Power Generation",
]

# Create folders
for subgroup in subgroups:

    directory = os.path.join(base_directory, subgroup)
    os.makedirs(directory, exist_ok=True)

print("Folders created successfully.")