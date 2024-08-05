import System
import clr

# Import RevitAPI
# clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import ICollection
from System.Collections.Generic import List

# Import DocumentManager and TransactionManager
# clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = __revit__.ActiveUIDocument.Document


# Overriding graphics of element to change their colors
# Getting the Solid Fill
all_patterns = FilteredElementCollector(doc).OfClass(FillPatternElement).ToElements()
solid_fill = [i for i in all_patterns if i.GetFillPattern().IsSolidFill][0]
color_fill = Color(255, 0, 0)

override_graphics = OverrideGraphicSettings()
override_graphics.SetSurfaceForegroundPatternId(solid_fill.Id)
override_graphics.SetSurfaceForegroundPatternColor(color_fill)

active_view = doc.ActiveView

# Applying graphic override to the previously retrieved elements (WHICH YOU MUST ALREADY HAVE RETRIEVED!).
tr = Transaction(doc, "Override Graphics")
for element in elements:
    # Converting the ID which is currently a numpy.Int to and Element ID
    # element_id = ElementId(id_of_element_in_Int_format)
    # element = doc.GetElement(element_id)
    tr.Start()
    active_view.SetElementOverrides(element.Id, override_graphics)
    tr.Commit()
