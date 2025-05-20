import pyttsx3
import argparse

engine = pyttsx3.init()

def talk(text):
    length = len(text)
    # message body
    print(" ", end="")
    for i in range(length):
        # -----
        print("_", end="")
    print("")
    print("<", end="")
    print(text, end=">")
    print("")
    print(" ", end="")
    for i in range(length):
        # -----
        print("¯", end="")

    print("")

    #speakre

    # \
    #  \
    #   /¯¯¯¯¯¯\
    #   | *  * |
    #   | \__/ |
    #   \______/
    #
    print(" ", end="")
    print("  \\")
    print("    \\")
    print("     /¯¯¯¯¯¯\\")
    print("     | *  * |")
    print("     | \\__/ |")
    print("     \\______/")

    engine.say(text)
    engine.runAndWait()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="+")

    args = parser.parse_args()
    engine = pyttsx3.init()
    
    full = " ".join(args.text)
    talk(full)

if __name__ == "__main__":
    main()