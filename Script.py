import os
import shutil
import datetime

Desktop = 'C:\\users\\rahman\\Desktop\\'
Archive = 'C:\\DesktopArchiver\\'

os.chdir(Desktop)

Exceptions = []

print('''---------------------------------------------------------
Desktop Archiver 2.0''')
while True:
    Action = input('''---------------------------------------------------------
Set exceptions as arguments or leave '/' to beggin.
---------------------------------------------------------
>>> ''')
    print('---------------------------------------------------------')
    if Action == '/':
        break
    else:
        if len(Action) == 0:
            continue
        else:
            Entries = Action.split()
            for Entry in Entries:
                if os.path.isdir(Entry):
                    for Item in os.listdir(Desktop):
                        if Item.lower() == Entry.lower():
                            Target = Item
                            break
                    Exceptions.append(Target)
                    print(f'Applied\t\t[{Target}]')
                else:
                    print(f'Error\t\t[{Entry}]')
try:
    os.mkdir(Archive+datetime.datetime.now().strftime("%y.%m.%d"))
except:
    pass
Items = os.listdir(Desktop)
for Item in Items:
    if os.path.isfile(Item):
        shutil.move(Item, Archive+datetime.datetime.now().strftime("%y.%m.%d")+'\\')
        print(f'Archived\t[{Item}]')
    else:
        print(f'Error\t\t[{Item}]')
if len(Exceptions) != 0:
    print('---------------------------------------------------------\nApplying exceptions.\n---------------------------------------------------------')
    for Exception in Exceptions:
        shutil.move(Exception, Archive+datetime.datetime.now().strftime("%y.%m.%d")+'\\')
        print(f'Archived\t[{Exception}]')
    print('---------------------------------------------------------')
else:
    print('---------------------------------------------------------\nNo exception to be applied.\n---------------------------------------------------------')