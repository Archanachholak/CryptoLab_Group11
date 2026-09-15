#include <iostream>
#include <string>
#include <fstream>
#include <limits>

using namespace std;

double balance = 10000.0;

// Read credentials from a separate configuration file
bool loadCredentials(string& correctUsername, string& correctPin) {
    ifstream file("secure_application/src/credentials.txt");

    if (!file) {
        cout << "Unable to load authentication configuration.\n";
        return false;
    }

    getline(file, correctUsername);
    getline(file, correctPin);

    file.close();

    return !correctUsername.empty() && !correctPin.empty();
}


// Login
bool login() {
    string username;
    string pin;
    string correctUsername;
    string correctPin;

    if (!loadCredentials(correctUsername, correctPin)) {
        return false;
    }

    cout << "\n===== ATM LOGIN =====\n";

    cout << "Username: ";
    cin >> username;

    cout << "PIN: ";
    cin >> pin;

    // Generic error message prevents information leakage
    if (username != correctUsername || pin != correctPin) {
        cout << "Invalid username or PIN.\n";
        return false;
    }

    cout << "Login successful!\n";
    return true;
}


// Check balance
void checkBalance() {
    cout << "\nCurrent Balance: Rs. " << balance << "\n";
}


// Withdraw
void withdraw() {
    double amount;

    cout << "\nEnter withdrawal amount: ";

    if (!(cin >> amount)) {
        cout << "Invalid amount.\n";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return;
    }

    // Input validation
    if (amount <= 0) {
        cout << "Amount must be greater than zero.\n";
        return;
    }

    if (amount > balance) {
        cout << "Insufficient balance.\n";
        return;
    }

    balance -= amount;

    cout << "Withdrawal successful.\n";
    cout << "Remaining balance: Rs. " << balance << "\n";
}


// Deposit
void deposit() {
    double amount;

    cout << "\nEnter deposit amount: ";

    if (!(cin >> amount)) {
        cout << "Invalid amount.\n";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return;
    }

    // Input validation
    if (amount <= 0) {
        cout << "Amount must be greater than zero.\n";
        return;
    }

    balance += amount;

    cout << "Deposit successful.\n";
    cout << "Current balance: Rs. " << balance << "\n";
}


// Change PIN
void changePin() {
    string newPin;

    cout << "\nEnter new PIN: ";
    cin >> newPin;

    // PIN validation
    if (newPin.length() != 4) {
        cout << "PIN must contain exactly 4 digits.\n";
        return;
    }

    for (char c : newPin) {
        if (!isdigit(c)) {
            cout << "PIN must contain only digits.\n";
            return;
        }
    }

    cout << "PIN changed successfully.\n";
}


// ATM menu
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

        if (!(cin >> choice)) {
            cout << "Invalid choice.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

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


// Main
int main() {

    cout << "=============================\n";
    cout << "          ATM SYSTEM\n";
    cout << "=============================\n";

    while (true) {

        cout << "\n1. Login\n";
        cout << "2. Exit\n";
        cout << "Enter choice: ";

        int choice;

        if (!(cin >> choice)) {
            cout << "Invalid choice.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

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