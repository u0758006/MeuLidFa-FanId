from argparse import ArgumentParser
import re
import csv
import io
from urllib.request import urlopen
from os import makedirs
from os.path import join

mai_lukdui = re.compile('（.+?）')


def main():
    miang = '/ngienbun-ngiliau'
    makedirs(miang, exist_ok=True)
    with open(join(miang, 'meu.txt'), 'wt') as meu_dong:
        with open(join(miang, 'fa.txt'), 'wt') as fa_dong:
            for hang in ngin():
                for meu, fa in zip(
                    hang['客語標音'].split('\n'), hang['客家語'].split('\n')
                ):
                    meu = meu.strip()
                    fa = fa.strip()
                    if meu:
                        print(mai_lukdui.sub('', meu), file=meu_dong)
                        print(fa, file=fa_dong)


def ngin():
    github_bangtsi = ('https://raw.githubusercontent.com/'
                      'i3thuan5/Elearning-Hakka/main/csv_imtong/')
    jintsing_sului = [
        f'{github_bangtsi}da3-2.csv',
        f'{github_bangtsi}da3-1.csv',
        f'{github_bangtsi}daw.csv',
    ]
    for bangtsi in jintsing_sului:
        with urlopen(bangtsi) as tong:
            with io.StringIO(tong.read().decode('utf-8')) as tsuliau:
                yield from csv.DictReader(tsuliau)


if __name__ == '__main__':
  main()
