# Prog-11: Weather report (EP.2)

import json
import math

def top_K_max_temp_by_region(data, K):
    a = {}
    for i in data.values():
        for j in i['list']:
            if i['city']['region'] in a:
                a[i['city']['region']] += tuple([(-j['main']['temp'],\
                    i['city']['name'],j['dt_txt'])])
            else:
                a[i['city']['region']] = tuple([(-j['main']['temp'],\
                    i['city']['name'],j['dt_txt'])])
    x = {i:sorted(a[i])[:K] for i in a}; y = {}
    for i in sorted(x):
        for j in range(K):
            if i in y: 
                y[i].append((-x[i][j][0],)+(x[i][j][1:3]))
            else: 
                y[i] = [(-x[i][j][0],)+(x[i][j][1:3])]
    return y

def average_temp_by_date(data, region):
    a = {}
    for i in data.values():
        if region == 'ALL' or i['city']['region'] == region:
            for j in i['list']:
                if j['dt_txt'].split()[0] in a:
                    a[j['dt_txt'].split()[0]] += [j['main']['temp']]
                else:
                    a[j['dt_txt'].split()[0]] = [j['main']['temp']]
    return [(i,sum(a[i])/len(a[i])) for i in a]

def max_rain_in_3h_periods(data, region, date):
    x = {}
    for i in data.values():
        if region == 'ALL' or i['city']['region'] == region:
            for j in i['list']:
                if 'rain' in j:
                    if j['dt_txt'] in x:
                        x[j['dt_txt']] += [j['rain']['3h']]
                    else:
                        x[j['dt_txt']] = [j['rain']['3h']]
    o = {int(i.split()[1].split(':')[0]):max(x[i]) for i in x if date == i.split()[0]}; out = []
    for k in range(0,24,3):
        if k in o:
            out.append((k,o[k]))
        else:
            out.append((k,float(0)))
    return sorted(out)

def AM_PM_weather_description_by_region(data, date):
    x_AM = {}; x_PM = {}; AM = {}; PM = {}
    for i in data.values():
        for j in i['list']:
            for k in j['weather']:
                if date == j['dt_txt'].split()[0] and  0 <= int(j['dt_txt'].split()[1].split(':')[0]) < 12:
                    if i['city']['region'] in x_AM:
                        x_AM[i['city']['region']] += (k['description'],)
                    else:
                        x_AM[i['city']['region']] = (k['description'],)
                elif date == j['dt_txt'].split()[0] and 12 <= int(j['dt_txt'].split()[1].split(':')[0]) < 24:
                    if i['city']['region'] in x_PM:
                        x_PM[i['city']['region']] += (k['description'],)
                    else:
                        x_PM[i['city']['region']] = (k['description'],)
    for i in x_AM:
        y = {}
        for j in x_AM[i]:
            if j in y: 
                y[j] += 1
            else: 
                y[j] = 1
            t = {}
            for key,v in y.items():
                if v in t: 
                    t[v] += [key]
                else: 
                    t[v] = [key]
        AM[i] = {'AM':sorted(t[max(t.keys())])[0]}
    for i in x_PM:
        y = {}
        for j in x_PM[i]:
            if j in y: 
                y[j] += 1
            else: 
                y[j] = 1
            t = {}
            for key,v in y.items():
                if v in t: 
                    t[v] += [key]
                else: 
                    t[v] = [key]
        PM[i] = {'PM':sorted(t[max(t.keys())])[0]}
    out = {}
    for i in ['N','E','W','S','C','NE']: 
        p = {}
        if i in AM:
            for k,v in AM[i].items():
                p[k] = v 
                if i in PM:
                    for key,value in PM[i].items():
                        p[key] = value
        elif i in PM:
            for k,v in PM[i].items():
                p[k] = v 
                if i in AM:
                    for key,value in AM[i].items():
                        p[key] = value
        out[i] = p
    return out

def most_varied_weather_provinces(data):
    x = {}; y = {}
    for i in data.values():
        for j in i['list']: 
            for k in j['weather']:
                if i['city']['name'] in x:
                    x[i['city']['name']].add(k['description'])
                else:
                    x[i['city']['name']] = {k['description']}
    for i in x:
        if len(x[i]) in y: 
            y[len(x[i])].add(i)
        else: 
            y[len(x[i])] = {i}
    return y[max(y.keys())]

def main():
    print(most_varied_weather_provinces(json.load(open('weather_5_40_2.json'))))

main()