import re
import os
import math
import requests
import hashlib

# Check if password is common
def check_common_passwords(password):
    file_path = os.path.join(os.path.dirname(__file__), "common_passwords.txt")
    with open(file_path, "r") as file:
        common_passwords = file.read().splitlines()
    return password in common_passwords

# Calculate password entropy
def calculate_entropy(password):
    unique_chars = len(set(password))
    entropy = len(password) * math.log2(unique_chars)
    return entropy

# Check if password is leaked (using Have I Been Pwned API)
def check_pwned_password(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        hashes = response.text.splitlines()
        for h in hashes:
            hash_suffix, count = h.split(":")
            if hash_suffix == suffix:
                return int(count)  # Password found in breaches
    return 0  # Password is safe

# Analyze password security
def analyze_password(password):
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    entropy = calculate_entropy(password)
    pwned_count = check_pwned_password(password)

    strength_score = sum([has_upper, has_lower, has_digit, has_special]) + (length >= 12)
    
    strength = "Weak"
    if strength_score == 5 and entropy >= 50 and pwned_count == 0:
        strength = "Strong"
    elif strength_score >= 3 and entropy >= 35:
        strength = "Moderate"

    return {
        "length": length,
        "contains_upper": has_upper,
        "contains_lower": has_lower,
        "contains_digit": has_digit,
        "contains_special": has_special,
        "entropy": entropy,
        "pwned_count": pwned_count,
        "common": check_common_passwords(password),
        "strength": strength
    }
