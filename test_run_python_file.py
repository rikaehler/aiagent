from functions.run_python_file import run_python_file

def main():

    # expecting calculator usage instructions as result1
    print('Testing: run_python_file("calculator", "main.py")')
    result1 = run_python_file("calculator", "main.py")
    print(f"\n{result1}")
    print("-" * 40)

    # should run calculator [3+5] and return nasty rendered result2
    print('Testing: run_python_file("calculator", "main.py", ["3 + 5"])')
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"\n{result2}")
    print("-" * 40)

    # should run calculator tests successfully
    print('Testing: run_python_file("calculator", "tests.py")')
    result3 = run_python_file("calculator", "tests.py")
    print(f"\n{result3}")
    print("-" * 40)

    # expecting error return
    print('Testing: run_python_file("calculator", "../main.py")')
    result4 = run_python_file("calculator", "../main.py")
    print(f"\n{result4}")
    print("-" * 40)

    # expecting error return
    print('Testing: run_python_file("calculator", "nonexistent.py")')
    result5 = run_python_file("calculator", "nonexistent.py")
    print(f"\n{result5}")
    print("-" * 40)

    # expecting error return
    print('Testing: run_python_file("calculator", "lorem.txt")')
    result6 = run_python_file("calculator", "lorem.txt")
    print(f"\n{result6}")
    print("-" * 40)

if __name__ == "__main__":
    main()