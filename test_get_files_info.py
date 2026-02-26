from functions.get_files_info import get_files_info

def main():

    # test1, expecting results
    print('Testing: get_files_info("calculator", ".")')
    result1 = get_files_info("calculator", ".")
    print(f"\n{result1}")
    print("-" * 40)

    # test 2, expecting results
    print('Testing: get_files_info("calculator", "pkg")')
    result2 = get_files_info("calculator", "pkg")
    print(f"\n{result2}")
    print("-" * 40)

    # test 3, expecting error (outside the permitted working directory)
    print('Testing: get_files_info("calculator", "/bin")')
    result3 = get_files_info("calculator", "/bin")
    print(f"\n{result3}")
    print("-" * 40)

    # test 4, expecting error (outside the permitted working directory)
    print('Testing: get_files_info("calculator", "../")')
    result4 = get_files_info("calculator", "../")
    print(f"\n{result4}")
    print("-" * 40)

if __name__ == "__main__":
    main()