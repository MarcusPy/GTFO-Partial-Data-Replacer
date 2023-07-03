import os, re

# replacements with formatting brackets {} must be raw - 'r' prefix before the quotation marks
strings = {
    '457619842'  : r'{0}',
    '869'        : r'{0}',
    '1994337092' : r'{0}',
    '3025634811' : r'{0}',
    '802'        : r'>HEAT {0}',
    '850'        : r'Swipe: {0}',
    '840'        : r'<color=red>[{0}]</color>',
    '849'        : r'{0} <color=red>REQUIRED</color>',
    '3046473959' : r'{0} <color=purple><size=70%>({1})</size></color>',
    '353087154'  : r'COMPLETE {0} HIGH SECTORS',
    '3923959063' : r'COMPLETE {0} EXTREME SECTORS',
    '841'        : '<color=green>No Alarm</color>',
    '1086'       : '',
    '969'        : '',
    '41'         : '',
    '1392'       : '',
    '1616762565' : '',
    '14'         : 'HEAT:',
    '615262857'  : 'HIGH SECTORS:',
    '1110'       : 'HIGH',
    '1111'       : 'HIGH',
    '1134'       : 'HIGH',
    '1701962716' : 'HIGH',
    '1729980802' : 'HIGH',
    '1864567361' : 'HIGH',
    '3928479961' : 'EXTREME SECTORS:',
    '1112'       : 'EXTREME',
    '1133'       : 'EXTREME',
    '319600558'  : 'EXTREME',
    '2091204054' : 'EXTREME',
    '2466992430' : 'EXTREME',
    '3356421220' : 'EXTREME',
    '3089373346' : 'OVERLOAD',
}
keys = list(strings.keys())

def TextDataBlock_Apply_Settings(path_input:str, path_output:str):
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    for file in os.listdir(path_input):
        pid = re.search('[0-9]+', file)
        if pid.group() in keys:
            with open(os.path.join(path_input, file), encoding='utf-8') as data:
                data = data.read()
                pattern = '"English": ".*"'
                repl = '"English": "' + strings[pid.group()] + '"'
                data = re.sub(pattern, repl, data)
                with open(os.path.join(path_output, file), 'w', encoding='utf-8') as new:
                    new.write(data)

path_root   = os.getcwd()
path_input  = path_root + '\input'
path_output = path_root + '\output'

TextDataBlock_Apply_Settings(path_input, path_output)