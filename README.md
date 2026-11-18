# SHA-256 Hash Generator and Comparator

## Overview

A Python-based project that generates SHA-256 cryptographic hashes and compares two text inputs to determine whether their hash values match.

This project demonstrates the fundamentals of cryptographic hashing using Python's built-in `hashlib` library.

## Features

- Accepts two text inputs from the user.
- Generates SHA-256 hashes for both inputs.
- Displays the generated hash values.
- Displays the length of each hash.
- Compares both hashes.
- Identifies whether the hash values match or differ.

## Technologies Used

- **Programming Language:** Python
- **Library:** hashlib
- **Hashing Algorithm:** SHA-256

## How It Works

1. The program prompts the user to enter two text inputs.
2. Both inputs are converted into bytes using `encode()`.
3. SHA-256 generates a hash for each input.
4. The `hexdigest()` method converts the hash values into hexadecimal strings.
5. The program compares both hashes and displays the result.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/lapulga10dani/SHA256-Hash-Generator.git
```

### 2. Navigate to the Project Directory

```bash
cd SHA256-Hash-Generator
```

### 3. Run the Python Script

```bash
python hash_function.py
```

## Example Output

```text
Enter your text: Hello
Original text1: Hello

Enter your text: Hello
Original text2: Hello

SHA-256 Hash: [Generated hash]
Hash Length: 64

SHA-256 Hash: [Generated hash]
Hash Length: 64

Hashes Match
```

## Key Learning Outcomes

- Understanding crypt
