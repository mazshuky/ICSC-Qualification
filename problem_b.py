import sys


def cake_calculator(flour: int, sugar: int) -> list:
    """
    Calculates the maximum number of cakes that can be made and the leftover ingredients.

    Args:
        flour: An integer larger than 0 specifying the amount of available flour.
        sugar: An integer larger than 0 specifying the amount of available sugar.

    Returns:
        A list of three integers:
        [0] the number of cakes that can be made
        [1] the amount of leftover flour
        [2] the amount of leftover sugar

    Raises:
        ValueError: If inputs flour or sugar are not positive.
    """
    # WRITE YOUR CODE HERE

    # Validate that both flour and sugar are positive integers
    if flour <= 0 or sugar <= 0:
        raise ValueError("Flour and sugar must be positive integers.")

    # Calculate the maximum number of cakes that can be made
    cakes = min(flour // 100, sugar // 50)

    # Calculate the remaining flour and sugar after making cakes
    remaining_flour = flour - cakes * 100
    remaining_sugar = sugar - cakes * 50

    # Return the result as a list: [number of cakes, leftover flour, leftover sugar]
    return [cakes, remaining_flour, remaining_sugar]



# --- Main execution block. DO NOT MODIFY  ---
if __name__ == "__main__":
    try:
        # 1. Read input from stdin
        flour_str = input().strip()
        sugar_str = input().strip()

        # 2. Convert inputs to appropriate types
        flour = int(flour_str)
        sugar = int(sugar_str)

        # 3. Call the cake calculator function
        result = cake_calculator(flour, sugar)

        # 4. Print the result to stdout in the required format
        print(f"{result[0]} {result[1]} {result[2]}")

    except ValueError as e:
        # Handle errors during input conversion or validation
        print(f"Input Error or Validation Failed: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        # Handle cases where not enough input lines were provided
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)