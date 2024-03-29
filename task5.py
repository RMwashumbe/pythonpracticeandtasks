#You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#A valid credit card from ABCD Bank has the following characteristics:
# ► It must start with a 4, 5  or 6.
# ► It must contain exactly 16  digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.

# Input Format
# The first line of input contains an integer N.
# The next N lines contain credit card numbers.

# Constraints
# 0 < N < 100

# Output Format
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

import re


def validate_credit_card(card_number):
    # Check if the card number starts with 4, 5, or 6 and consists of exactly 16 digits
    if re.match(r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$', card_number):
        # Remove hyphens if present
        card_number = card_number.replace('-', '')

        # Check if there are no more than 3 consecutive repeated digits
        if not re.search(r'(\d)\1{3}', card_number):
            return 'Valid'

    return 'Invalid'


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        card_number = input().strip()
        print(validate_credit_card(card_number))
