from typing import List, Tuple


def phone_mnemonic(phone_number: str) -> List[str]:
    DIGIT_2_CHARACTERS = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
    }  # add '0': '0' and '1': '1'

    if len(phone_number) == 1:
        return [
            c for c in DIGIT_2_CHARACTERS[phone_number].split()
        ]  # remove `'.split()`

    mnemonics_from_first_digit = [c for c in DIGIT_2_CHARACTERS[phone_number[0]]]
    mnemonics_from_remaining_digits = phone_mnemonic(phone_number[1:])

    return [
        x + y
        for x in mnemonics_from_first_digit
        for y in mnemonics_from_remaining_digits
    ]


def phone_mnemonic_2(phone_number: str) -> List[str]:

    DIGIT_2_CHARACTERS: Tuple[str] = (
        "0",
        "1",
        "ABC",
        "DEF",
        "GHI",
        "JKL",
        "MNO",
        "PQRS",
        "TUV",
        "WXYZ",
    )

    mnemonics: List[str] = []
    partial_mnemonic: List[str] = ["0"] * len(phone_number)

    def _helper(digit_idx: int) -> None:
        if digit_idx == len(phone_number):
            # All digits [have been] processed,
            # so add `partial_mnemonic` to `mnemonics`.
            # (We add a copy since subsequent calls modify `partial_mnemonic`.)
            mnemonics.append(
                "".join(partial_mnemonic),
            )
        else:  # i.e. digit_idx < len(phone_number)
            # Try all possible characters for the digit at `phone_number[digit_idx]`.
            for c in DIGIT_2_CHARACTERS[int(phone_number[digit_idx])]:
                partial_mnemonic[digit_idx] = c
                _helper(digit_idx + 1)

    _helper(0)

    return mnemonics


if __name__ == "__main__":
    phone_number = "2276696"
    result = phone_mnemonic_2(phone_number)
