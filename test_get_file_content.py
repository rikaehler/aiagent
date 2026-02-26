from functions.get_file_content import get_file_content

def main():
    '''
    # test1, expecting results
    print('Testing: get_files_info("calculator", "lorem.txt")')
    result1 = get_file_content("calculator", "lorem.txt")
    print(f"\n{result1}")
    print("-" * 40)
    '''
    # test 2, expecting results
    print('Testing: get_files_info("calculator", "main.py")')
    result2 = get_file_content("calculator", "main.py")
    print(f"\n{result2}")
    print("-" * 40)

    # test 3, expecting results
    print('Testing: get_files_info("calculator", "pkg/calculator.py")')
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(f"\n{result3}")
    print("-" * 40)

    # test 4, expecting error 
    print('Testing: get_files_info("calculator", "/bin/cat")')
    result4 = get_file_content("calculator", "/bin/cat")
    print(f"\n{result4}")
    print("-" * 40)

    # test 5, expecting error
    print('Testing: get_files_info("calculator", "pkg/does_not_exist.py")')
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"\n{result5}")
    print("-" * 40)
    

if __name__ == "__main__":
    main()