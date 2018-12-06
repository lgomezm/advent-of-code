import re
import datetime

class Event:
    def __init__(self, date, message):
        self.date = date
        self.message = message

def quicksort(a):
    def quicksort_helper(a, lo, hi):
        if lo < hi:
            p = partition(a, lo, hi)
            quicksort_helper(a, lo, p-1)
            quicksort_helper(a, p+1, hi)
    def partition(a, lo, hi):
        pivot = a[lo]
        i = lo+1
        j = hi
        done = False
        while True:
            while i <= j and a[i].date <= pivot.date:
                i = i + 1
            while a[j].date >= pivot.date and j >= i:
                j = j -1
            if j < i:
                break
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        temp = a[lo]
        a[lo] = a[j]
        a[j] = temp
        return j
    quicksort_helper(a, 0, len(a)-1)

def compute_sleep_times(events):
    guard_id = -1
    sleep_times = {}
    for e in events:
        if e.message == 'falls asleep':
            startsleep = e.date
        elif e.message == 'wakes up':
            date_key = str(e.date.month)+'-'+str(e.date.day)
            if guard_id in sleep_times:
                if date_key in sleep_times[guard_id]:
                    sleep_times[guard_id][date_key].append((startsleep.minute, e.date.minute-1))
                else:
                    sleep_times[guard_id][date_key] = [(startsleep.minute, e.date.minute-1)]
            else:
                sleep_times[guard_id] = {date_key: [(startsleep.minute, e.date.minute-1)]}
        else:
            m = re.search(r'(?<=#)\d+', e.message)
            if m is not None:
                guard_id = int(m.group(0))
    return sleep_times

def calculate_most_asleep(sleep_times):
    most_asleep = ('0', 0)
    for guard_id, times in sleep_times.items():
        count = 0
        for _, sleep_intervals in times.items():
            for interval in sleep_intervals:
                count += interval[1] - interval[0] + 1
        if most_asleep[1] < count:
            most_asleep = [guard_id, count]
    return most_asleep[0]

def compute_sleep_by_minute(sleep_times, most_asleep):
    times = sleep_times[most_asleep]
    sleep_by_min = {}
    for _, sleep_intervals in times.items():
        for interval in sleep_intervals:
            for x in range(interval[0], interval[1]+1):
                if x in sleep_by_min:
                    sleep_by_min[x] += 1
                else:
                    sleep_by_min[x] = 1
    return sleep_by_min

def calculate_max_minute_sleep(sleep_by_min):
    max_count = (0,0)
    for minute, count in sleep_by_min.items():
        if count > max_count[1]:
            max_count = (minute, count)
    return max_count[0]

def processLog(lines):
    events = []
    for line in lines:
        date = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        message = line[19:].strip()
        events.append(Event(date, message))
    quicksort(events)
    sleep_times = compute_sleep_times(events)
    most_asleep = calculate_most_asleep(sleep_times)
    sleep_by_min = compute_sleep_by_minute(sleep_times, most_asleep)
    minute = calculate_max_minute_sleep(sleep_by_min)
    print(int(most_asleep)*minute)

with open('../input/day4.txt') as f:
    lines = f.readlines()
    processLog(lines)