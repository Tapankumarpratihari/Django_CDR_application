import csv
from django.db import models

class CDR(models.Model):
    MSISDN=models.CharField()
    IMSI=models.BigIntegerField()
    IMEI=models.BigIntegerField()
    PLAN=models.CharField()
    CALL_TYPE=models.CharField()
    CORRESP_TYPE=models.CharField()
    CORRESP_ISDN=models.CharField()
    DURATION=models.PositiveIntegerField()
    TIME=models.DateTimeField()
    DATE=models.CharField()


def parse_cdr_file(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cdr = CDR(
                MSISDN=row[0],
                IMSI=row[1],
                IMEI=row[2],
                PLAN=row[3],
                CALL_TYPE=row[4],
                CORRESP_TYPE=row[5],
                CORRESP_ISDN=row[6],
                DURATION=row[7],
                TIME=row[8],
                DATE=row[9],
            )
            cdr.save()

if __name__ == '__main__':
    parse_cdr_file('CDR.csv')