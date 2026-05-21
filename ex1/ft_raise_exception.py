#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int | None:
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    test_inputs = ["25", "abc", "100", "-50"]

    for input_str in test_inputs:
        print(f"Input data is '{input_str}'")
        try:
            temp = input_temperature(input_str)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
