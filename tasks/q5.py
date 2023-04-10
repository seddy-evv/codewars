"""A friend of mine takes the sequence of all numbers from 1 to n
(where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all
numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (n is always strictly greater than 0)
and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in
increasing order of the "a".

It happens that there are several possible (a, b). The function returns an
empty array (or an empty string) if
no possible numbers are found which will prove that my friend has not told
the truth! (Go: in this case return nil).

Examples:
removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
or

in C:
removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of
Pair pointers, each one also allocated."""


def remov_nb(n):
    total = 0
    list_high = []
    list_low = []
    for i in range(n + 1):
        total += i
    for i in range(n, 0, - 1):
        z = (total - i)//i
        if i * z == (total - i - z):
            list_low.append((z, i))
            list_high.append((i, z))
    list_high.reverse()
    return list_low + list_high


"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in 
a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that 
fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3"""


def rgb(r, g, b):
    def dec_to_hexa(n):
        if n < 0:
            n = 0
        elif n > 255:
            n = 255

        hex_str = hex(n).replace("0x", "")
        if len(hex_str) == 1:
            hex_str = "0" + hex_str

        return hex_str.upper()

    hex_code = ""
    hex_code += dec_to_hexa(r)
    hex_code += dec_to_hexa(g)
    hex_code += dec_to_hexa(b)
    return hex_code


if __name__ == '__main__':
    print(remov_nb(26))
    print(rgb(255, 255, 255))
