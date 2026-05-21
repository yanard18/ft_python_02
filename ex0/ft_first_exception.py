#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature() -> None:
    test_inputs = ["25", "abc"]

    for input_str in test_inputs:
        print(f"Input data is '{input_str}'")

        temp = input_temperature(input_str)
        if temp is not None:
            print(f"Temperature is now {temp}°C")
        print("")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
