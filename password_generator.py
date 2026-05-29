import secrets
import string
import argparse
import pyperclip

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    required = []

    if use_upper:
        chars += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(secrets.choice(string.digits))
    if use_symbols:
        chars += string.punctuation
        required.append(secrets.choice(string.punctuation))

    password = required + [secrets.choice(chars) for _ in range(length - len(required))]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='🔐 Secure Password Generator')
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('-n', '--count', type=int, default=1, help='Number of passwords')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('--copy', action='store_true', help='Copy first password to clipboard')

    args = parser.parse_args()

    print(f"\n🔐 Generated Password(s):\n")
    passwords = []
    for i in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
        passwords.append(pwd)
        print(f"  {i+1}. {pwd}")

    if args.copy:
        try:
            pyperclip.copy(passwords[0])
            print(f"\n  ✅ Password pertama disalin ke clipboard!")
        except:
            print(f"\n  ⚠️  Install pyperclip untuk fitur copy: pip install pyperclip")

    print(f"\n  Strength: {'🟢 Strong' if args.length >= 16 else '🟡 Medium' if args.length >= 12 else '🔴 Weak'}\n")

if __name__ == '__main__':
    main()