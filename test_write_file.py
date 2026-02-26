from functions.write_file import write_file

def main():
    # test1, expecting new filw
    print('Testing: write_file("calculator", "lorem.txt", "wait, this isn,t lorem ipsum")')
    result1 = write_file("calculator", "lorem.txt", "wait, this isn,t lorem ipsum")
    print(f"\n{result1}")
    print("-" * 40)

    # test2,
    print('Testing: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"\n{result2}")
    print("-" * 40)

    # test3, expecting error
    print('Testing: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"\n{result3}")
    print("-" * 40)

if __name__ == "__main__":
    main()