#!/usr/bin/env python3
"""
Secure Password Generator

This script generates secure random passwords with customizable options.
"""

import secrets
import string
import argparse

# Define a safe subset of special characters that work well in most contexts
SAFE_SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def generate_password(length=16, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_special=True):
    """
    Generate a secure random password.
    
    Args:
        length (int): Length of the password (default: 16)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_lowercase (bool): Include lowercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    
    Raises:
        ValueError: If length is less than 1 or no character types are selected
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Build character set based on options
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += SAFE_SPECIAL_CHARS
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    # Generate password using cryptographically secure random
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                     # Generate a 16-character password
  %(prog)s -l 20               # Generate a 20-character password
  %(prog)s -l 12 --no-special  # Generate without special characters
  %(prog)s -n 5                # Generate 5 passwords
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Length of the password (default: 16)'
    )
    
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    
    parser.add_argument(
        '--no-uppercase',
        action='store_false',
        dest='uppercase',
        help='Exclude uppercase letters'
    )
    
    parser.add_argument(
        '--no-lowercase',
        action='store_false',
        dest='lowercase',
        help='Exclude lowercase letters'
    )
    
    parser.add_argument(
        '--no-digits',
        action='store_false',
        dest='digits',
        help='Exclude digits'
    )
    
    parser.add_argument(
        '--no-special',
        action='store_false',
        dest='special',
        help='Exclude special characters'
    )
    
    args = parser.parse_args()
    
    # Validate number of passwords
    if args.number < 1:
        print("Error: Number of passwords must be at least 1")
        return 1
    
    try:
        for i in range(args.number):
            password = generate_password(
                length=args.length,
                use_uppercase=args.uppercase,
                use_lowercase=args.lowercase,
                use_digits=args.digits,
                use_special=args.special
            )
            print(password)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
