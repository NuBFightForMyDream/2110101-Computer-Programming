# Prog-12: COVID-19: The Latest Wave

import numpy as np

def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:, 1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0], 1))
    return {'new_cases': new_cases,
            'norm_data': norm,
            'province_names': d[1:, 0],
            'dates': d[0, 1:]}

def max_new_cases_date(data):
    sum = np.sum(data['new_cases'], axis=0)
    return (data['dates'][np.argmax(sum)], np.max(sum))

def max_new_cases_province(data, beg_date, end_date):
    beg_d = list(data['dates']).index(beg_date)
    end_d = list(data['dates']).index(end_date)
    sum = np.sum(data['new_cases'][:, beg_d:end_d+1], axis=1)
    return (data['province_names'][np.argmax(sum)], np.max(sum))

def max_new_cases_province_by_dates(data):
    out = np.ndarray((len(data['dates']), 3), dtype=object)
    Max_cases_province = data['province_names'][np.argmax(data['new_cases'], axis=0)]
    Max_cases = np.max(data['new_cases'], axis=0)
    out[:, 0] = data['dates'][:]
    out[:, 1] = Max_cases_province[:]
    out[:, 2] = Max_cases[:]
    return out

def most_similar(data, province):
    province_ind = list(data['province_names']).index(province)
    Excluded_province = data['province_names'][data['province_names'] != province]
    Main = data['norm_data'][province_ind, :]
    Excluded = data['norm_data'][data['province_names'] != province]
    delta_square = (Main - Excluded) ** 2
    sum = np.sum(delta_square, axis=1)
    return Excluded_province[np.argmin(sum)]

def most_similar_province_pair(data):
    province_Tile = np.tile(data['province_names'], len(data['province_names']))
    province_Repeat = np.repeat(data['province_names'], len(data['province_names']), axis=0)
    Excluded_province_Tile = province_Tile[province_Tile != province_Repeat]
    Excluded_province_Repeat = province_Repeat[province_Tile != province_Repeat]
    Tile = np.tile(data['norm_data'], (len(data['norm_data']), 1))
    Repeat = np.repeat(data['norm_data'], len(data['norm_data']), axis=0)
    Excluded_Tile = Tile[province_Tile != province_Repeat]
    Excluded_Repeat = Repeat[province_Tile != province_Repeat]
    delta_square = (Excluded_Tile - Excluded_Repeat) ** 2
    sum = np.sum(delta_square, axis=1)
    return (Excluded_province_Repeat[np.argmin(sum)],
            Excluded_province_Tile[np.argmin(sum)])

def most_similar_in_period(data, province, beg_date, end_date):
    province_ind = list(data['province_names']).index(province)
    Excluded_province = data['province_names'][data['province_names'] != province]
    beg_d = list(data['dates']).index(beg_date)
    end_d = list(data['dates']).index(end_date)
    Main = data['norm_data'][province_ind, beg_d:end_d+1]
    Excluded = data['norm_data'][data['province_names'] != province]
    n_d = end_d - beg_d + 1
    st_ind = len(data['dates']) - n_d + 1
    ind_X = np.array([np.arange(n_d)])
    ind_Y = np.array([np.arange(st_ind)]).T
    ind = ind_X + ind_Y
    Excluded = Excluded[:, ind].transpose((1, 0, 2))
    delta_square = (Main - Excluded) ** 2
    sum = np.sum(delta_square, axis=2)
    Min = np.min(sum, axis=1)
    Min_ind = np.argmin(sum, axis=1)
    date_ind = np.where(np.min(Min_ind[list(np.where(Min == np.min(Min))[0])]) == Min_ind)[0]
    return (Excluded_province[np.min(Min_ind[list(np.where(Min == np.min(Min))[0])])],
            data['dates'][date_ind[list(Min[date_ind]).index(np.min(Min))]],
            data['dates'][date_ind[list(Min[date_ind]).index(np.min(Min))] + n_d - 1])

def main():
    exec(open('Prog-12-eval.py').read())

main()