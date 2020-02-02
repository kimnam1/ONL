from datetime import timedelta
import datetime

from django.db import models



class Onl(models.Model):
    month = models.PositiveSmallIntegerField("월", blank=True, )
    day = models.PositiveSmallIntegerField("일", blank=True, )
    date = models.DateField('날짜', blank=True, null=True, )
    slug = models.SlugField(max_length=20, allow_unicode=True, unique=True, blank=True, )
    events = models.TextField(max_length=500, verbose_name="사건", blank=True,)

    class Meta:
        ordering = ('month', 'day',)

    def title(self):
        return str(self.month) + "월 " + str(self.day) + "일"

    def __str__(self):
        return str(self.month) + "월 " + str(self.day) + "일"

    def day_with_dlf(self):
        return str(self.day) + "일"

    def month_in_string(self):
        return str(self.month)

    def month_from_date(self):
        return self.date.strftime("%m")

    def day_from_date(self):
        return self.date.strftime("%d")

    def yesterday(self):
        return self.date - timedelta(days=1)

    def tomorrow(self):
        return self.date + timedelta(days=1)

    # def yesterday_month(self):
    #     if self.day == 1:
    #         if self.month == 1:  # 1월이면
    #             return 12
    #         else:
    #             return self.month-1
    #     else:
    #         return self.month
    #
    # def yesterday_day(self):
    #     if self.day == 1:
    #         if self.month == 3:
    #             return 29
    #         if self.month == 1 or self.month == 2 or self.month == 4 or self.month == 6 or self.month == 8 or self.month == 9 or self.month == 11:
    #             return 31
    #         if self.month == 5 or self.month == 7 or self.month == 10 or self.month == 12:
    #             return 30
    #     else:
    #         return self.day - 1
    #
    # def tomorrow_month(self):
    #     if self.day == 31:
    #         if self.month == 12:
    #             return 1
    #         else:
    #             return self.month+1
    #     if self.day == 30 and (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11):
    #         return self.month+1
    #     if self.day == 29 and self.month == 2:
    #         return 3
    #     else:
    #         return self.month
    #
    # def tomorrow_day(self):
    #     if self.day == 31:
    #         return 1
    #     if self.day == 30 and (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11):
    #         return 1
    #     if self.day == 29 and self.month == 2:
    #         return 1
    #     else:
    #         return self.day + 1

    def yesterday_slug(self):
        ystrdy = self.yesterday()
        return str(ystrdy.month)+"-"+str(ystrdy.day)

    def tomorrow_slug(self):
        tmrrw = self.tomorrow()
        return str(tmrrw.month)+"-"+str(tmrrw.day)

    def save(self, *args, **kwargs):
        self.date = datetime.date(year=2020, month=self.month, day=self.day)
        super().save(*args, **kwargs)












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