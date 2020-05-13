import sys

# Output one dotted decimal number, 0-255
def dotd(v):
    if v == 1:
        return '?d'
    elif v == 2:
        return '?d?d'
    elif v == 3:
        return '?1?d?d'
    # TODO: support 192.168.1 and 10.1 syntax.
    # These pattern expands like this: 192.168.0.1 and 10.0.0.1
    # 0 is inserted at the left out dotted decimal parts.
    return ''

# Loop through all combinations of 1-3 digits for all four
# dotted decimal parts (a, b, c, d).
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                # Make ?1 mean 1 or 2. Three digit
                # IPv4 dotted decimal parts starts
                # with 1 or 2, like 192 or 254.
                mask = ''
                mask += dotd(a) + '.'
                mask += dotd(b) + '.'
                mask += dotd(c) + '.'
                mask += dotd(d) 
                if '?1' in mask:
                    print('12,' + mask)
                else:
                    print(mask)
