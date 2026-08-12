# ATM Security Analysis Report

## 1. Application
ATM System developed in C++.

## 2. SAST Tool
Tool: Cppcheck
Version: 2.13.0

Cppcheck was used to perform static analysis of the C++ source code.

## 3. Vulnerability 1: Hardcoded Credentials

### Location
secure_application/src/atm.cpp

### Description
The username and PIN are directly stored in the source code.

### Evidence
The source code contains:
CORRECT_USERNAME = "admin"
CORRECT_PIN = "1234"

### Risk
Anyone who obtains the source code can see the credentials.

### Recommendation
Credentials should not be hardcoded in the source code.

## 4. Vulnerability 2: Improper Input Validation

### Location
withdraw() and deposit() functions.

### Description
The application does not properly validate whether the entered amount is positive.

### Test
A negative withdrawal amount such as -5000 was entered.

### Result
The application accepted the negative value and incorrectly modified the balance.

### Risk
An attacker may manipulate the balance using invalid input.

### Recommendation
Validate that the amount is greater than zero before processing.

## 5. Vulnerability 3: Information Leakage

### Location
login() function.

### Description
The application gives different error messages for an invalid username and an incorrect PIN.

### Test
Wrong username:
"Username does not exist."

Correct username with wrong PIN:
"Username exists, but PIN is incorrect."

### Risk
The messages reveal whether a username exists.

### Recommendation
Use a generic login error message such as:
"Invalid username or PIN."

## 6. SAST Results

Cppcheck 2.13.0 was executed on atm.cpp.

The scan reported missing standard system includes and checker information. These were informational findings and did not directly identify the three vulnerabilities above.

## 7. Conclusion

The ATM application was manually tested for three security vulnerabilities:
1. Hardcoded credentials
2. Improper input validation
3. Information leakage

Cppcheck was also used for static analysis of the C++ source code.
