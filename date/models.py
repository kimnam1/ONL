from django.db import models
from django.urls import reverse


class Onl(models.Model):
    month = models.PositiveSmallIntegerField("월", blank=True, )
    date = models.PositiveSmallIntegerField("일", blank=True, )
    slug = models.SlugField(max_length=20, allow_unicode=True, unique=True, blank=True, )
    events = models.TextField(max_length=500, verbose_name="사건", blank=True,)

    class Meta:
        ordering = ('month', 'date',)

    def title(self):
        return str(self.month) + "월 " + str(self.date) + "일"

    def __str__(self):
        return str(self.month) + "월 " + str(self.date) + "일"

    def date_with_dlf(self):
        return str(self.date) + "일"

    def yesterday_month(self):
        if self.date == 1:
            if self.month == 1:  # 1월이면
                return 12
            else:
                return self.month-1
        else:
            return self.month

    def yesterday_date(self):
        if self.date == 1:
            if self.month == 3:
                return 29
            if self.month == 1 or self.month == 2 or self.month == 4 or self.month == 6 or self.month == 8 or self.month == 9 or self.month == 11:
                return 31
            if self.month == 5 or self.month == 7 or self.month == 10 or self.month == 12:
                return 30
        else:
            return self.date - 1

    def tomorrow_month(self):
        if self.date == 31:
            if self.month == 12:
                return 1
            else:
                return self.month+1
        if self.date == 30 and (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11):
            return self.month+1
        if self.date == 29 and self.month == 2:
            return 3
        else:
            return self.month

    def tomorrow_date(self):
        if self.date == 31:
            return 1
        if self.date == 30 and (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11):
            return 1
        if self.date == 29 and self.month == 2:
            return 1
        else:
            return self.date + 1











class Event(models.Model):
    event = models.CharField(verbose_name="사건", max_length=200)

    date = models.ForeignKey(Onl, verbose_name="날짜", on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="연도")

    def __str__(self):
        return self.event

class Birth(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)

    date = models.ForeignKey(Onl, verbose_name="날짜", on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="연도")

    def __str__(self):
        return self.name

class Death(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)

    date = models.ForeignKey(Onl, verbose_name="날짜", on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="연도")

    def __str__(self):
        return self.name