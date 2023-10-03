feet_per_meter = 3.28084
inches_per_foot = 12
feet_per_continent = 2


def meters_to_feet(meter: float) -> float:
    return meter * feet_per_meter

def meters_to_inches(meter: float) -> float:
    return meter * feet_per_meter * inches_per_foot

def meters_to_continent(meter: float) -> float:
    return meter * feet_per_meter / feet_per_continent


def inches_to_meters(inches: float) -> float:
    return inches / inches_per_foot / feet_per_meter

def inches_to_feet(inches: float) -> float:
    return inches / inches_per_foot

def inches_to_continent(inches: float) -> float:
    return inches / inches_per_foot / feet_per_continent


def feet_to_meters(feet: float) -> float:
    return feet / feet_per_meter

def feet_to_inches(feet: float) -> float:
    return feet * inches_per_foot

def feet_to_continent(feet: float) -> float:
    return feet / feet_per_continent


def continent_to_meters(continent: float) -> float:
    return continent * feet_per_continent / feet_per_meter

def continent_to_inches(continent: float) -> float:
    return continent * feet_per_continent * inches_per_foot

def continent_to_feet(continent: float) -> float:
    return continent * feet_per_continent
