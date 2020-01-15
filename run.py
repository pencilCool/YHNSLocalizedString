from openpyxl import load_workbook

import os


def export_localized_string(path):
    wb = load_workbook('test/resouce.xlsx')
    sheet = wb.active
    for row in sheet.rows:
        key = row[0].value
        value = row[1].value
        print '"{}" = "{}";'.format(key, value)
        print 'NSLocalizedString(@"{}","{}");'.format(key, value)


if __name__ == "__main__":
    export_localized_string("")
