str_of_time = '1h 45m,360s,25m,30m 120s,2h 60s'
times_no_gap = str_of_time.replace(' ',',')
times_no_comma = times_no_gap.split(',')
summ = 0
for t in times_no_comma:
    if 'h' in t:
        summ = summ+int(t[:-1])*60
    if 'm' in t:
        summ = summ+int(t[:-1])
    if 's' in t:
        summ = summ+int(t[:-1])//60
print(summ)