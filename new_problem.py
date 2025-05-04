import sys
from pathlib import Path

def create_files(problem_name):
    base_name = problem_name.lower().replace(" ", "_")
    solution_path = Path("solutions") / f"{base_name}.py"
    test_path = Path("tests") / f"test_{base_name}.py"

    # Create directories if they don't exist
    Path("solutions").mkdir(exist_ok=True)
    Path("tests").mkdir(exist_ok=True)

    # Create solution file
    if not solution_path.exists():
        solution_path.write_text(f"# Solution for {problem_name}\n\ndef {base_name}():\n    pass\n")

    # Create test file
    if not test_path.exists():
        test_path.write_text(
            f"# Test for {problem_name}\n"
            f"from solutions.{base_name} import {base_name}\n\n"
            f"def test_{base_name}():\n    assert {base_name}() is None\n"
        )

    print(f"Created solution and test files for: {problem_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_problem.py \"Two Sum\"")
    else:
        create_files(sys.argv[1])

