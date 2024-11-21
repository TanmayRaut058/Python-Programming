months_to_days = {
    'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
    'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31
}
day_names = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def display_grid(d, row=5, col=7):
    c = ''
    c += ('.' + '-' * 5) * col + '.' + '\n'
    c += '| ' + '  | '.join(day_names).center(5 * col) + ' |\n'
    c += ('.' + '-' * 5) * col + '.' + '\n'
    for i in range(row):
        c += '|'
        for j in range(col):
            c += (f"{d[i][j]:^5}") + '|'
        c += '\n'
        c += ('.' + '-' * 5) * col + '.' + '\n'
    return c

def cal_printer(mm=1, yy=2020):
    c = ''
    month = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    # Calculate the day of the week for the first day of the month
    day = (yy - 1) % 400
    day = (day // 100) * 5 + ((day % 100) - (day % 100) // 4) + ((day % 100) // 4) * 2
    day = day % 7

    nly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Non-leap year
    ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Leap year

    # Add days of the previous months
    if yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0):
        s = sum(ly[:mm - 1])
    else:
        s = sum(nly[:mm - 1])

    day = (day + s) % 7

    # Generate the calendar header
    c += (month[mm] + ' ' + str(yy)).center(20, '-') + '\n'
    c += 'Su Mo Tu We Th Fr Sa\n'

    # Fill initial spaces
    c += '   ' * day

    # Number of days in the current month
    days_in_month = ly[mm - 1] if yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0) else nly[mm - 1]

    # Add days to the calendar
    for date in range(1, days_in_month + 1):
        c += f'{date:2} '
        day = (day + 1) % 7
        if day == 0:
            c += '\n'

    c += '\n'
    return c

def cal_printer_print(yy, row=4, col=3, fillchar='-'):
    months = [cal_printer(i, yy).splitlines() for i in range(1, 13)]
    formats = {
        '3X4': (3, 4),
        '4X3': (4, 3),
        '6X2': (6, 2),
        '12X1': (12, 1),
        '2X6': (2, 6)
    }

    x = input("Enter your Format (3X4, 4X3, 6X2, 12X1, 2X6): ")
    if x not in formats:
        print("Invalid format!")
        return

    rows, cols = formats[x]
    for r in range(rows):
        for i in range(7):  # Assuming each calendar month has at most 7 rows
            row_data = []
            for c in range(cols):
                idx = r * cols + c
                if idx < 12:
                    row_data.append(months[idx][i].ljust(22))
                else:
                    row_data.append(''.ljust(22))
            print('   '.join(row_data))
        print(fillchar * (22 * cols + 3 * (cols - 1)))

# Main program
y = int(input("Enter your year: "))
z = input("Enter filler character: ")
cal_printer_print(y, fillchar=z)
