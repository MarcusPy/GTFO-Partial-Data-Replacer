import os, re

settings = {
    'normal': {
        "a": 0.0,
        "r": 0.0,
        "g": 0.25,
        "b": 0.25
    },
    'infection': {
        "a": 0.0,
        "r": 0.1,
        "g": 0.0,
        "b": 0.1
    }
}
keys = list(settings.keys())

def FogSettingsDataBlock_Apply_Settings(path_input:str, path_output:str):
    if not os.path.exists(path_output):
        os.mkdir(path_output)
        
    for file in os.listdir(path_input):
        if file == 'FogSettingsDataBlock.py' or file == 'output':
            continue
        with open(os.path.join(path_input, file)) as data:
            data = data.read()
            infectious = data.find('"Infection": 0.0,')
            if infectious == -1:
                infectious = 1
            else:
                infectious = 0
            for k, v in settings[keys[infectious]].items():
                pattern = '"' + k + '": [0-9].[0-9]+'
                repl = '"' + k + '": ' + str(v)
                data = re.sub(pattern, repl, data)
            with open(os.path.join(path_output, file), 'w') as new:
                new.write(data)

path_input  = os.getcwd()
path_output = path_input + '\\output'

FogSettingsDataBlock_Apply_Settings(path_input, path_output)
