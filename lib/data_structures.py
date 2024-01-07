from statistics import mean

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}"
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food["cuisine"] == cuisine][0]


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    levels = [food["heat_level"] for food in spicy_foods]
    return mean(levels)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


def sort_by_heat(spicy_foods):
    return sorted(spicy_foods, key=lambda food: food.get("heat_level"))


print_spiciest_foods(spicy_foods)
print(sort_by_heat(spicy_foods))
