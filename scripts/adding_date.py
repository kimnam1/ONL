from date.models import Onl

for dd in Onl.objects.all():
    dd.save()
    print(str(dd.date) +" saved")