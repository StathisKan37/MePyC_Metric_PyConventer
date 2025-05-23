def length_function(x1, x2, x3):
    # Converting input to SI unit (meters)
    if x2 == 'Picometers (pm)':
        SI_unit = x1 / 1e12
    if x2 == 'Nanometers (nm)':
        SI_unit = x1 / 1e9
    if x2 == 'Micrometers (um)':
        SI_unit = x1 / 1e6
    if x2 == 'Millimeters (mm)':
        SI_unit = x1 / 1000
    if x2 == 'Centimeters (cm)':
        SI_unit = x1 / 100
    if x2 == 'Decimeters (dm)':
        SI_unit = x1 / 10
    if x2 == 'Meters (m)':
        SI_unit = x1
    if x2 == 'Kilometers (km)':
        SI_unit = x1 * 1000
    if x2 == 'Miles (mi)':
        SI_unit = x1 * 1609.344
    if x2 == 'Yards (yd)':
        SI_unit = x1 * 0.9144
    if x2 == 'Feet (ft)':
        SI_unit = x1 * 0.3048
    if x2 == 'Inches (in)':
        SI_unit = x1 * 0.0254
    if x2 == 'Nautical miles (Nm)':
        SI_unit = x1 * 1852

    # Converting SI unit (meters) to output unit
    if x3 == 'Picometers (pm)':
        return SI_unit * 1e12
    if x3 == 'Nanometers (nm)':
        return SI_unit * 1e9
    if x3 == 'Micrometers (um)':
        return SI_unit * 1e6
    if x3 == 'Millimeters (mm)':
        return SI_unit * 1000
    if x3 == 'Centimeters (cm)':
        return SI_unit * 100
    if x3 == 'Decimeters (dm)':
        return SI_unit * 10
    if x3 == 'Meters (m)':
        return SI_unit
    if x3 == 'Kilometers (km)':
        return SI_unit / 1000
    if x3 == 'Miles (mi)':
        return SI_unit / 1609.344
    if x3 == 'Yards (yd)':
        return SI_unit / 0.9144
    if x3 == 'Feet (ft)':
        return SI_unit / 0.3048
    if x3 == 'Inches (in)':
        return SI_unit / 0.0254
    if x3 == 'Nautical miles (Nm)':
        return SI_unit / 1852

def mass_function(x1, x2, x3):
    # Converting input to SI unit (kilograms)
    if x2 == 'Picograms (pg)':
        SI_unit = x1 / 1e12
    if x2 == 'Nanograms (ng)':
        SI_unit = x1 / 1e9
    if x2 == 'Micrograms (μg)':
        SI_unit = x1 / 1e6
    if x2 == 'Milligrams (mg)':
        SI_unit = x1 / 1e3
    if x2 == 'Grams (g)':
        SI_unit = x1 / 1e3
    if x2 == 'Kilograms (kg)':
        SI_unit = x1
    if x2 == 'Metric tons (t)':
        SI_unit = x1 * 1000
    if x2 == 'Ounces (oz)':
        SI_unit = x1 * 0.0283495
    if x2 == 'Pounds (lb)':
        SI_unit = x1 * 0.453592
    if x2 == 'Stones (st)':
        SI_unit = x1 * 6.35029
    if x2 == 'US tons (short tons)':
        SI_unit = x1 * 907.18474
    if x2 == 'UK tons (long tons)':
        SI_unit = x1 * 1016.04691

    # Converting SI unit (kilograms) to output unit
    if x3 == 'Picograms (pg)':
        return SI_unit * 1e12
    if x3 == 'Nanograms (ng)':
        return SI_unit * 1e9
    if x3 == 'Micrograms (μg)':
        return SI_unit * 1e6
    if x3 == 'Milligrams (mg)':
        return SI_unit * 1e3
    if x3 == 'Grams (g)':
        return SI_unit * 1e3
    if x3 == 'Kilograms (kg)':
        return SI_unit
    if x3 == 'Metric tons (t)':
        return SI_unit / 1000
    if x3 == 'Ounces (oz)':
        return SI_unit / 0.0283495
    if x3 == 'Pounds (lb)':
        return SI_unit / 0.453592
    if x3 == 'Stones (st)':
        return SI_unit / 6.35029
    if x3 == 'US tons (short tons)':
        return SI_unit / 907.18474
    if x3 == 'UK tons (long tons)':
        return SI_unit / 1016.04691
