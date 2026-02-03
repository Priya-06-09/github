VITAMINS = {
    "vitamin a": "Carrots, spinach, milk",
    "vitamin b": "Eggs, bananas, whole grains",
    "vitamin c": "Oranges, lemon, amla",
    "vitamin d": "Sunlight, fish, milk",
    "vitamin e": "Nuts, seeds, spinach"
}

def vitamin_help(v):
    return VITAMINS.get(v.lower(), "Eat balanced diet with fruits & vegetables")
