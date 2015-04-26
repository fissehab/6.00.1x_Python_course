def decode_shift_letter(current_ord, start, end, shift):
    if current_ord - shift < start:
        new_ord = (current_ord + 26) - shift
        return chr(new_ord)
    else:
        return chr(current_ord-shift)

def encode_shift_letter(current_ord, start, end, shift):
    if current_ord + shift > end:
        new_ord = (current_ord - 26) + shift
        return chr(new_ord)
    else:
        return chr(current_ord+shift)

def decode(input, shift):
    return modify_input(input, shift, decode_shift_letter)

def encode(input, shift):
    return modify_input(input, shift, encode_shift_letter)

def modify_input(input, shift, shift_letter):
    new_sentence = ''

    for letter in input:
        # we only encode letters, random characters like +!%$ are not encoded.
        # Lower and Capital letters are not stored near each other on the
        # ascii table
        lower_start = ord('a')
        lower_end = ord('z')
        upper_start = ord('A')
        upper_end = ord('Z')
        current_ord = ord(letter)

        if current_ord >= lower_start and current_ord <= lower_end:
            new_sentence += shift_letter(current_ord, lower_start, lower_end, shift)
        elif current_ord >= upper_start and current_ord <= upper_end:
            new_sentence += shift_letter(current_ord, upper_start, upper_end, shift)
        else:
            new_sentence += letter

    return new_sentence


def get_shift():
    try:
        shift = int(raw_input('What shift would you like to use?\n'))
    except ValueError:
        print 'Shift must be a number'
        shift = get_shift()

    if not (shift > 0 and shift <= 25):
        print 'Shift must be between 1 and 25'
        shift = get_shift()

    return shift

def main():
    try:
        task = int(raw_input('1) Encode \n'+ \
                             '2) Decode \n'))
    except ValueError:
        print 'Invalid task, try again!'
        main()

    shift = get_shift()
    input = raw_input('What message would you like to %s\n' % ('Encode' if task == 1 else 'Decode'))

    if task == 1:
        print encode(input, shift)
    elif task == 2:
        print decode(input, shift)

if __name__ == '__main__':
    main()