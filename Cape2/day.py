import os
day = 1

def hari():
    global day
    os.system('cls' if os.name == 'nt' else 'clear')
    print('================')
    print('     projek   ')
    print('================')
    print('')
    print(f'====Day {day}====')
    print('Pilih kegiatan')
    print('1.')
    print('2')
    print('Masukkan pilihanmu:')
    kegiatan = input('> ')

    if kegiatan == '1':
        print('Kamu memilih kegiatan 1')
    elif kegiatan == '2':
        print('Kamu memilih kegiatan 2')
    else:
        print('Pilihan tidak valid')

    return

hari()










