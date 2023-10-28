import json
from coxeter.shapes import ConvexPolyhedron
import os

_DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

with open(os.path.join(_DATA_FOLDER, "polydata.json"), "r") as json_file:
    poly_data = json.load(json_file)


# Define characters and their respective ranges
def get_shortcodes(families=None, ranges=None, n_shapes=None):
    all_characters = [
        ("P", 1, 5),
        ("A", 1, 13),
        ("C", 1, 13),
        ("J", 1, 92),
        ("O", 1, 22),
    ]

    # Generate strings with the specified pattern
    result = []
    for char, min_length, max_length in all_characters:
        if char not in families:
            continue
        for num in range(min_length, max_length + 1):
            # Use f-strings to format the number as a two-digit string
            formatted_num = f"{num:02d}"
            result.append(f"{char}{formatted_num}")

    # Print the result
    if n_shapes is not None:
        return result[:n_shapes]
    return result


def findpoly(name):
    poly = poly_data.get(name)
    return ConvexPolyhedron(poly["vertices"]), poly["name"]
