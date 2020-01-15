#!/usr/bin/env python

from openpyxl import load_workbook


def export_localized_string(path):
    wb = load_workbook('test/resouce.xlsx')
    sheet = wb.active
    with open('./result/LocalizedString.txt', 'a') as f:
        for row in sheet.rows:
            key = row[0].value
            value = row[1].value
            line = '"{}" = "{}";'.format(key, value)
            f.write(line)
            f.write("\n")

    with open('./result/copy_to_code.txt', 'a') as f:
        for row in sheet.rows:
            key = row[0].value
            value = row[1].value
            line = 'NSLocalizedString(@"{}","{}");'.format(key, value)
            f.write(line)
            f.write("\n")
            f.write("\n")


if __name__ == "__main__":
    export_localized_string("")
