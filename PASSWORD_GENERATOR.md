# Password Generator

A secure command-line password generator written in Python that creates cryptographically strong random passwords.

## Features

- **Secure**: Uses Python's `secrets` module for cryptographically strong randomness
- **Customizable**: Configure password length and character types
- **Flexible**: Generate single or multiple passwords at once
- **Easy to use**: Simple command-line interface

## Requirements

- Python 3.6 or higher (uses built-in modules only)

## Usage

### Basic Usage

Generate a default 16-character password:
```bash
python3 password_generator.py
```

### Custom Length

Generate a password with specific length:
```bash
python3 password_generator.py -l 20
```

### Multiple Passwords

Generate multiple passwords at once:
```bash
python3 password_generator.py -n 5
```

### Character Type Options

Customize which character types to include:

```bash
# Without special characters
python3 password_generator.py --no-special

# Without digits
python3 password_generator.py --no-digits

# Only lowercase and digits
python3 password_generator.py --no-uppercase --no-special

# Combine options
python3 password_generator.py -l 24 -n 3 --no-special
```

## Command-Line Options

- `-l, --length`: Length of the password (default: 16)
- `-n, --number`: Number of passwords to generate (default: 1)
- `--no-uppercase`: Exclude uppercase letters
- `--no-lowercase`: Exclude lowercase letters
- `--no-digits`: Exclude digits
- `--no-special`: Exclude special characters
- `-h, --help`: Show help message

## Examples

```bash
# Generate a 20-character password
python3 password_generator.py -l 20

# Generate 5 passwords of 12 characters each
python3 password_generator.py -l 12 -n 5

# Generate a password without special characters
python3 password_generator.py --no-special

# Generate a simple alphanumeric password
python3 password_generator.py --no-special -l 16
```

## Security

This password generator uses Python's `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

The `secrets` module is more secure than the `random` module for password generation as it uses sources of randomness provided by the operating system.

## License

This project is part of the GitHub Skills Introduction course and is available under the MIT License.
