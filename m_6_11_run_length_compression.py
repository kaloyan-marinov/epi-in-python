def encoding(s: str) -> str:
    result = []

    i = 0
    while i < len(s):
        character = s[i]
        count = 0
        while s[i] == character:
            count += 1
            i += 1
            if i == len(s):
                break

        result.extend([str(count), character])

    return "".join(result)


def decoding(s: str) -> str:
    result = []

    i = 0
    while i < len(s):
        # Read off the repetition count.
        j = i
        while s[j].isdigit():
            j += 1
            count = int(s[i:j])

        # Update `result`.
        result += s[j] * count

        i = j + 1

    return "".join(result)


if __name__ == "__main__":
    encoded_s = "16h25q25f14m8q45p9c21u11y15b16d23h8y3k29n20p16a12d20y17b26m14x15h23f29b3h21t25c19q3o28f25n17z22j6i8w29y15u20g29p11r14t20q16p1m18l15w13v22s14d21x72w25j9q27r17g5l16x2c14r20h29s27u8m17s25b14u29x5g28s10u14z27x4h17a29s22k7p22m26r14c29t16j16h1n28z14f16v27x5y10r25k12v23z26n3d27y1s10j11n5t16f16l20v25u12q3e20p27i23e7v28b9d4k1d15z23b10o21l16t14q29z23m5y12h3e3v14t27v13a23w26b15w"

    s = decoding(encoded_s)

    s = "hhhhhhhhhhhhhhhhqqqqqqqqqqqqqqqqqqqqqqqqqfffffffffffffffffffffffffmmmmmmmmmmmmmmqqqqqqqqpppppppppppppppppppppppppppppppppppppppppppppcccccccccuuuuuuuuuuuuuuuuuuuuuyyyyyyyyyyybbbbbbbbbbbbbbbddddddddddddddddhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyykkknnnnnnnnnnnnnnnnnnnnnnnnnnnnnppppppppppppppppppppaaaaaaaaaaaaaaaaddddddddddddyyyyyyyyyyyyyyyyyyyybbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmmmmmmmmxxxxxxxxxxxxxxhhhhhhhhhhhhhhhfffffffffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbhhhtttttttttttttttttttttcccccccccccccccccccccccccqqqqqqqqqqqqqqqqqqqoooffffffffffffffffffffffffffffnnnnnnnnnnnnnnnnnnnnnnnnnzzzzzzzzzzzzzzzzzjjjjjjjjjjjjjjjjjjjjjjiiiiiiwwwwwwwwyyyyyyyyyyyyyyyyyyyyyyyyyyyyyuuuuuuuuuuuuuuuggggggggggggggggggggppppppppppppppppppppppppppppprrrrrrrrrrrttttttttttttttqqqqqqqqqqqqqqqqqqqqppppppppppppppppmllllllllllllllllllwwwwwwwwwwwwwwwvvvvvvvvvvvvvssssssssssssssssssssssddddddddddddddxxxxxxxxxxxxxxxxxxxxxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwjjjjjjjjjjjjjjjjjjjjjjjjjqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrggggggggggggggggglllllxxxxxxxxxxxxxxxxccrrrrrrrrrrrrrrhhhhhhhhhhhhhhhhhhhhsssssssssssssssssssssssssssssuuuuuuuuuuuuuuuuuuuuuuuuuuummmmmmmmsssssssssssssssssbbbbbbbbbbbbbbbbbbbbbbbbbuuuuuuuuuuuuuuxxxxxxxxxxxxxxxxxxxxxxxxxxxxxgggggssssssssssssssssssssssssssssuuuuuuuuuuzzzzzzzzzzzzzzxxxxxxxxxxxxxxxxxxxxxxxxxxxhhhhaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssskkkkkkkkkkkkkkkkkkkkkkpppppppmmmmmmmmmmmmmmmmmmmmmmrrrrrrrrrrrrrrrrrrrrrrrrrrcccccccccccccctttttttttttttttttttttttttttttjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhnzzzzzzzzzzzzzzzzzzzzzzzzzzzzffffffffffffffvvvvvvvvvvvvvvvvxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyrrrrrrrrrrkkkkkkkkkkkkkkkkkkkkkkkkkvvvvvvvvvvvvzzzzzzzzzzzzzzzzzzzzzzznnnnnnnnnnnnnnnnnnnnnnnnnndddyyyyyyyyyyyyyyyyyyyyyyyyyyysjjjjjjjjjjnnnnnnnnnnntttttffffffffffffffffllllllllllllllllvvvvvvvvvvvvvvvvvvvvuuuuuuuuuuuuuuuuuuuuuuuuuqqqqqqqqqqqqeeeppppppppppppppppppppiiiiiiiiiiiiiiiiiiiiiiiiiiieeeeeeeeeeeeeeeeeeeeeeevvvvvvvbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddkkkkdzzzzzzzzzzzzzzzbbbbbbbbbbbbbbbbbbbbbbboooooooooolllllllllllllllllllllttttttttttttttttqqqqqqqqqqqqqqzzzzzzzzzzzzzzzzzzzzzzzzzzzzzmmmmmmmmmmmmmmmmmmmmmmmyyyyyhhhhhhhhhhhheeevvvttttttttttttttvvvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaawwwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbwwwwwwwwwwwwwww"
    encoding(s)
