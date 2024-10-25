# minipass/checker.py

import re

class PasswordChecker:
    def __init__(self):
        self.common_patterns = ["1234", "password", "qwerty", "abc123"]

    def check_strength(self, password):
        score = 0
        suggestions = []

        # Check for length
        if len(password) >= 8:
            score += 2
        else:
            suggestions.append("Increase length to at least 8 characters.")

        # Check for lowercase letters
        if re.search("[a-z]", password):
            score += 2
        else:
            suggestions.append("Add lowercase letters.")

        # Check for uppercase letters
        if re.search("[A-Z]", password):
            score += 2
        else:
            suggestions.append("Add uppercase letters.")

        # Check for numbers
        if re.search("[0-9]", password):
            score += 2
        else:
            suggestions.append("Add numbers.")

        # Check for special characters
        if re.search("[@#$%^&*!]", password):
            score += 2
        else:
            suggestions.append("Add special characters (@#$%^&*! etc.).")

        # Check for common patterns
        if any(pattern in password for pattern in self.common_patterns):
            score -= 2
            suggestions.append("Avoid common patterns like '1234', 'password', etc.")

        # Score should be between 0 and 10
        score = max(0, min(10, score))

        return score, suggestions