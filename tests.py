from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for running main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for running tests.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for running ../main.py (should be error):")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running nonexistent.py (should be error):")
    print(result)


if __name__ == "__main__":
    test()
