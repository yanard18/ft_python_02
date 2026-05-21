#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    try:
        match operation_number:
            case 0:
                int("abc")
            case 1:
                (1 / 0)
            case 2:
                open("/non/existent/file")
            case 3:
                "abc" + 123
            case 4:
                print("Operation completed successfully!")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    except ZeroDivisionError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    except FileNotFoundError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    except TypeError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        

def test_error_types():
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)

    print("\nAll error types tested successfully!")



if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
