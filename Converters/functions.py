def metric_function(x1, x2, x3):
    # Converting input to SI unit (meters)
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
