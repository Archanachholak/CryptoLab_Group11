from datetime import datetime
from analysis.file_analysis import analyze_file


def write_log(option):
    with open("log.txt", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} - {option}\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("      Welcome to CryptoLabX")
    print("=" * 35)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n[Encrypt]")
            print("Coming Soon...")
            write_log("Encrypt")

        elif choice == "2":
            print("\n[Decrypt]")
            print("Coming Soon...")
            write_log("Decrypt")

        elif choice == "3":
            print("\n[Attack]")
            print("Coming Soon...")
            write_log("Attack")

        elif choice == "4":
            analyze_file()
            write_log("Analyze")

        elif choice == "5":
            print("\nThank you for using CryptoLabX!")
            print("Goodbye!")
            write_log("Exit")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
