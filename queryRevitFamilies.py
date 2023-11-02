import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import Document, FamilyItemFactory

# Open the current Revit document
doc = __revit__.ActiveUIDocument.Document

# Path to the family file
family_path = r"Z:\BIM Standards\02_Revit\Revit Families\BSA Revit Families\BSA  Titleblock 24 X 36 D No Grid No Dates.rfa"

# Load the family file into memory
family = doc.LoadFamily(family_path)

# Get the family symbol from the family file
family_symbol = family.GetFamilySymbolIds().First

# Get the category of the family symbol
category = doc.GetElement(family_symbol).Category

# Get the name of the category
category_name = category.Name

# Print the category name
print("Category:", category_name)


