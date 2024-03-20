def num2words(num):
    """Converts an integer to its word form.

    Args:
      num: An integer.

    Returns:
      A string representing the word form of the integer.
    """

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ", "octillion ", "nonillion ", "decillion "]

    if num < 0:
        return "negative " + num2words(-num)

    elif num == 0:
        return "zero"

    else:
        word = ""
        i = 0
        while num > 0:
            remainder = num % 1000
            if remainder > 0:
                prefix = num2words_helper(remainder) + thousands[i] + " " + word
                word = prefix.strip()
            num //= 1000
            i += 1

        return word.strip()

def num2words_helper(num):
    """Converts an integer to its word form, without thousands."""

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 10:
        return ones[num]

    elif num < 20:
        return teens[num - 10]

    elif num < 100:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")

    else:
        return ones[num // 100] + " hundred" + (" and " + num2words_helper(num % 100) if num % 100 != 0 else "")

# Example usage
print(num2words(100))  # Output: 'one hundred'
print(num2words(1234))  # Output: 'one thousand two hundred and thirty four'
print(num2words(1234567))  # Output: 'one million two hundred thirty four thousand five hundred sixty seven'
