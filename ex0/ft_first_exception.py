#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int | None:
    return int(temp_str)


def test_temperature() -> None:
    test_inputs = ["25", "abc"]

    for input_str in test_inputs:
        print(f"Input data is '{input_str}'")
        try:
            temp = input_temperature(input_str)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
