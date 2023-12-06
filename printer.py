
def print_twice(s):
    print(s)
    print(s)

def print_reversed(s):
    print(s[::-1])


if __name__ == "__main__":
    s = input()
    print_reversed(s)
    print_twice(s)