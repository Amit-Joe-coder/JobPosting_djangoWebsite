import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myjobs.settings')
import django
django.setup()
from mainapp.models import hydrabad,goa,meerut,noida
from faker import Faker
from random import *
#title,qualification,address,date,contact
fake=Faker()
def ph_no(n):
    for i in range(n):
        num=randint(6,9)
        for i in range(9):
            num=str(num)+str(randint(1,9))
        return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        ftitle=fake.random_element(elements=('Project Manager','Team Leader','Software Engineer','Bar Tender','Master chef','C.A','Associate Engineer'))
        fqualification=fake.random_element(elements=('B.Tech','MCA','M.Sc','M.Tech','Phd','M.Com','M.Cheff'))
        faddress=fake.address()
        fcontact=ph_no(n)
        hydrabad.objects.get_or_create(title=ftitle,
                               qualification=fqualification,
                               date=fdate,
                               contact=fcontact,
                               address=faddress,
                               )
        goa.objects.get_or_create(title=ftitle,
                               qualification=fqualification,
                               date=fdate,
                               contact=fcontact,
                               address=faddress,
                               )
        meerut.objects.get_or_create(title=ftitle,
                               qualification=fqualification,
                               date=fdate,
                               contact=fcontact,
                               address=faddress,
                               )
        noida.objects.get_or_create(title=ftitle,
                               qualification=fqualification,
                               date=fdate,
                               contact=fcontact,
                               address=faddress,
                               )



n=int(input("Enter number of records: "))
populate(n)
print(f'{n} Records inserted successfully.....')