import csv
def get_last_char(link, num):
    return link[-num:]

with open('Website_URLs.csv', mode='r', encoding='utf-8') as csv_file, open('output.txt', mode='w', encoding='utf-8') as txt_file:
    reader = csv.reader(csv_file)
    csv_list = []
    next(reader)
    for row in reader:
        link=row[2]
        last_char=get_last_char(link,6)
        csv_list.append(last_char)
    print(csv_list)

