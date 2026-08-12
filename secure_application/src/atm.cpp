#include <iostream>
#include <string>

using namespace std;

// Vulnerability 1: Hardcoded credentials
const string CORRECT_USERNAME = "admin";
const string CORRECT_PIN = "1234";

double balance = 10000.0;

bool login() {
    string username;
    string pin;

    cout << "\n===== ATM LOGIN =====\n";

    cout << "Username: ";
    cin >> username;

    cout << "PIN: ";
    cin >> pin;

    if (username != CORRECT_USERNAME) {
        // Vulnerability 3: Information leakage
        cout << "Error: Username does not exist.\n";
        return false;
    }

    if (pin != CORRECT_PIN) {
        // Vulnerability 3: Information leakage
        cout << "Error: Username exists, but PIN is incorrect.\n";
        return false;
    }

    cout << "Login successful!\n";
    return true;
}

void checkBalance() {
    cout << "\nCurrent Balance: Rs. " << balance << "\n";
}

void withdraw() {
    double amount;

    cout << "\nEnter withdrawal amount: ";
    cin >> amount;

    // Vulnerability 2: Improper input validation
    if (amount <= balance) {
        balance -= amount;
        cout << "Withdrawal successful.\n";
        cout << "Remaining balance: Rs. " << balance << "\n";
    } else {
        cout << "Insufficient balance.\n";
    }
}

void deposit() {
    double amount;

    cout << "\nEnter deposit amount: ";
    cin >> amount;

    // Vulnerability 2: Improper input validation
    balance += amount;

    cout << "Deposit successful.\n";
    cout << "Current balance: Rs. " << balance << "\n";
}

void changePin() {
    string newPin;

    cout << "\nEnter new PIN: ";
    cin >> newPin;

    // No proper PIN validation in vulnerable version
    cout << "PIN changed successfully.\n";
}

void atmMenu() {
    int choice;

    while (true) {
        cout << "\n=============================\n";
        cout << "          ATM MENU\n";
        cout << "=============================\n";
        cout << "1. Check Balance\n";
        cout << "2. Withdraw\n";
        cout << "3. Deposit\n";
        cout << "4. Change PIN\n";
        cout << "5. Logout\n";
        cout << "Enter choice: ";

        cin >> choice;

        switch (choice) {
            case 1:
                checkBalance();
                break;

            case 2:
                withdraw();
                break;

            case 3:
                deposit();
                break;

            case 4:
                changePin();
                break;

            case 5:
                cout << "Logging out...\n";
                return;

            default:
                cout << "Invalid choice.\n";
        }
    }
}

int main() {
    cout << "=============================\n";
    cout << "          ATM SYSTEM\n";
    cout << "=============================\n";

    while (true) {
        cout << "\n1. Login\n";
        cout << "2. Exit\n";
        cout << "Enter choice: ";

        int choice;
        cin >> choice;

        if (choice == 1) {
            if (login()) {
                atmMenu();
            }
        }
        else if (choice == 2) {
            cout << "Thank you for using the ATM.\n";
            break;
        }
        else {
            cout << "Invalid choice.\n";
        }
    }

    return 0;
}