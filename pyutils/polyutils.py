import json
from coxeter.shapes import ConvexPolyhedron
import os

_DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

with open(os.path.join(_DATA_FOLDER, "polydata.json"), "r") as json_file:
    poly_data = json.load(json_file)


def findpoly(name):
    poly = poly_data.get(name)
    return ConvexPolyhedron(poly["vertices"]), poly["name"]
