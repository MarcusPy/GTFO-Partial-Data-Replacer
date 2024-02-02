import os, shutil

cwd = os.getcwd()

to_move = [
    '118619220', #pls enter  bioscan
    '1037355625',
    
    '783998405', #bioscan done
    '837317542',
    
    '433306715', #checkpoint
    '463747234',
    
    '1068353540', #sentry no ammo
    
    '880505770', #sentry idle scan
]

try:
    os.mkdir(cwd + '\wem_backup')
except FileExistsError:
    pass

done = 0
for file in to_move:
    try:
        shutil.move(cwd + '\\' + file + '.wem', cwd + '\wem_backup')
        done += 1
    except:
        continue

print(f'[{done}/{len(to_move)}] Files have been moved successfully')