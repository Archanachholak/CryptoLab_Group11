from datetime import datetime

def write_log(option):
    with open("log.txt", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} - {option}\n")


while True:
    print("\n========== CryptoLabX ==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Encrypt : Coming Soon...")
        write_log("Encrypt")

    elif choice == "2":
        print("Decrypt : Coming Soon...")
        write_log("Decrypt")

    elif choice == "3":
        print("Attack : Coming Soon...")
        write_log("Attack")

    elif choice == "4":
        print("Analyze : Coming Soon...")
        write_log("Analyze")

    elif choice == "5":
        print("Thank you for using CryptoLabX!")
        write_log("Exit")
        break

    else:
        print("Invalid Choice")