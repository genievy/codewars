

def encode_resistor_colors(ohms_string: str, result=""):
    dicta = {0: 'black',
             1: 'brown',
             2: 'red',
             3: 'orange',
             4: 'yellow',
             5: 'green',
             6: 'blue',
             7: 'violet',
             8: 'gray',
             9: 'white'}

    s = ohms_string.rstrip(" ohms")
    if 'k' in s:
        s = s.replace('k', 'e+03')
    elif 'M' in s:
        s = s.replace('M', 'e+06')
    s = str(int(float(s)))
    s = s[:2] + str(s[2:].count("0"))
    for i in s:
        result += dicta.get(int(i)) + " "
    return result + "gold"

print(encode_resistor_colors("100 ohms"))


"""
COLORS = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white'}

def encode_resistor_colors(ohmS):
    ohmS = str(int(eval(ohmS.replace(' ohms','').replace('k','*1000').replace('M','*1000000'))))
    return "{} {} {} gold".format(COLORS[ohmS[0]], COLORS[ohmS[1]], COLORS[ str(len(ohmS[2:])) ] )
    
"""