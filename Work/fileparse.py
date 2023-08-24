# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        if select:
            indices = [idx for idx, s in enumerate(headers) if s in select]   
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue

            if select:
                row = [row[index] for index in indices]

            if types and (len(types) == len(row)):
                try:
                    row = [func(val) for func,val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
