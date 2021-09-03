import math

import pandas as pd
import re
import numpy as np
from scipy import stats


def read_text(path, cols=None):
    """

    :param path: Pfad zur Textdatei
    :return: Dataframe mit Spalten
    """
    df = pd.read_csv(path, sep="\s+", comment='#',names=cols, header=None)

    return df


def get_header(p):
    with open(p, 'r') as f:
        lines = f.readlines()

    header_lines = [l for l in lines if l[0] == '#']

    return header_lines


def parse_header(hlines, p_mode='columns'):
    if p_mode == 'columns':
        cols = [c for c in hlines if "Column" in c]

        i = 0
        nr = []
        col_names = []
        for c in cols:
            # Lese die Spalten ein
            col_string, col_name = c.split(':')
            # entferne Leerzeichen und Steuerzeichen wie Zeilenumbrüche
            col_name = col_name.strip()

            # entferne die Zeichen vor den Spaltennummern
            col_string = col_string.strip('# Column')

            # Versuche die Nummer direkt zu laden (funktioniert nicht bei Angaben <von-bis>)
            try:
                nr.append(int(col_string))

            except ValueError:
                nr_start, nr_stop = col_string.split('-')

                pattern = "\((.*?)\)"
                substring = re.search(pattern, col_name).group(1)
                cols_to_add = substring.split(',')

                strings = []
                for s in cols_to_add:
                    s = s.strip()
                    r = col_name + f' | {s}'
                    strings.append(r)

                numbers_to_add = range(int(nr_start), int(nr_stop)+1)

                nr.extend(numbers_to_add)

                col_name = strings
            finally:
                if type(col_name) == list:
                    col_names.extend(col_name)
                else:
                    col_names.append(col_name)


        retvals = [nr, col_names]

    return retvals


def get_shortforms_of_columns(columns, dictionary):
    col_list = []
    for c in columns:
        for k in dictionary.keys():
            if k.find(c) != -1:
                col_list.append(dictionary[k])

            elif 'Average orientation (phi1, PHI, phi2)' in c and \
                    'Average orientation (phi1, PHI, phi2)' in k:
                if 'degrees' in c and 'degrees' in k:
                    unit = c.split('|')[1].strip()
                    col_list.append(f'{dictionary[k]}-{unit}')

                if 'radians' in c and 'radians' in k:
                    unit = c.split('|')[1].strip()
                    col_list.append(f'{dictionary[k]}-{unit}')

            elif 'Average Position' in c and 'Average Position' in k:
                unit = c.split('|')[1].strip()
                col_list.append(f'{dictionary[k]}-{unit}')

    return col_list


def export_to_excel(data, path, mode='w', sheet='data'):
    with pd.ExcelWriter(path, mode=mode) as writer:
        data.to_excel(writer, sheet_name=sheet)


def get_classified_data(x, n_classes=5):
    sorted_data = np.sort(x)

    grenzen = [(sorted_data[-1] / n_classes) * i for i in range(1, n_classes+1)]

    idx_array = [np.where(sorted_data < g)[0][-1] for g in grenzen]

    ret_val = idx_array

    return ret_val


def get_number_of_classes(data, mode):
    n = len(data)
    if mode == 'sr':
        classes = int(math.sqrt(n))
    elif mode == 'rice':
        classes = int(2*(n**(1/3)))
    elif mode == 'sturges':
        classes = int(math.log(n, 2) + 1)
    elif mode == 'fd':
        iqr = stats.iqr(data, interpolation = 'midpoint')
        classes = int(2*iqr/(n**(1/3)))
    else:
        raise NotImplementedError

    return classes





