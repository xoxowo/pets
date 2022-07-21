import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pets.settings")
django.setup()

from member.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

CSV_PATH_PRODUCTS='./member.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        for row in data_reader:
            Owner.objects.create(
                name = row[1],
                age = int(row[2]),
                email = row[3],
                )
            print(row)
