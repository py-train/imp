from django.db import models

# Create your models here.
class Tips(models.Model):

    class Meta:
        db_table = 'TIPS'

    total_bill = models.FloatField(primary_key=True)
    tip = models.FloatField()
    sex = models.CharField(max_length=100)
    smoker = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    size = models.IntegerField()

    def __repr__(self):
        return f'{self.total_bill} {self.tip} {self.sex}'
    
    def as_list(self):
        return [self.total_bill, self.tip, self.sex, self.smoker,
                self.day, self.time, self.size]