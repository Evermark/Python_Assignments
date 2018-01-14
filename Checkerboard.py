for row_count in range(1,9):
    new_row = ''
    if row_count % 2 ==0:
        for i in range(1,9):
            if i%2 ==0:
                new_row += '*'
            else:
                new_row += '_'
    else:
        for i in range(1,9):
            if i%2 ==0:
                new_row += '_'
            else:
                new_row += '*'
    print new_row
