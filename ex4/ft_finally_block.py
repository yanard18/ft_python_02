#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    test_batches = [
        ("Testing valid plants...", ["Tomato", "Lettuce", "Carrots"]),
        ("Testing invalid plants...", ["Tomato", "lettuce"])
    ]

    for msg, plants in test_batches:
        print(msg)
        try:
            print("Opening watering system")
            for plant in plants:
                water_plant(plant)
        except PlantError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
            print(".. ending tests and returning to main")
        finally:
            print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
