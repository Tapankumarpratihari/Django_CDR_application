from django.shortcuts import render
from .models import CDR


# Create your views here.
def parse_cdr_file(request):
    if request.method=='POST' and request.FILES['cdr_file']:
        cdr_file=request.FILES['cdr_file']
        reader = csv.reader(cdr_file)
        for row in reader:
            MSISDN=row[0],
            IMSI=row[1],
            IMEI=row[2],
            PLAN=row[3],
            CALL_TYPE=row[4],
            CORRESP_TYPE=row[5],
            CORRESP_ISDN=row[6],
            DURATION=row[7],
            TIME=row[8],
            DATE=row[9]
            cdr=CDR.objects.create(
               MSISDN=MSISDN,
                IMSI=IMSI,
                IMEI=IMEI,
                PLAN=PLAN,
                CALL_TYPE=CALL_TYPE,
                CORRESP_TYPE=CORRESP_TYPE,
                CORRESP_ISDN=CORRESP_ISDN,
                DURATION=DURATION,
                TIME=TIME,
                DATE=DATE 
            )
    return render(request,'parse.html')
            