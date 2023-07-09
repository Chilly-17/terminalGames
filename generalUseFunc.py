# some basic functions for type change, etc
def intify(input: str):
    try:
        output: int = int(input)
        return output
    except ValueError:
        div()
        print("Please only input numbers, not letters")
        return None


def div():
    print("")
