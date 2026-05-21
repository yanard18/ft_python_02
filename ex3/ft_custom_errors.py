#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        test_plant_error()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    try:
        print("Testing WaterError...")
        test_water_error()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught {e.__class__.__bases__[0].__name__}: {e}")

    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught {e.__class__.__bases__[0].__name__}: {e}")

    print("\nAll custom error types work correctly!")
