from django.db import models


# Create your models here.


class report(models.Model):
    # Model for each reports
    id = models.BigAutoField(unique=True)
    title = models.CharField(max_length=50, null=True)
    fields = models.OneToManyField('reportField',through='report_reportField')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    FormID = models.ForeignKey('Form', on_delete=models.SET_NULL, null=True, blank=True)


class reportField(models.Model):
    id = models.BigAutoField(unique=True)
    reportF = models.ForeignKey(Field, on_delete=models.SET_NULL)


class report_reportField(models.Model):
    reportF = models.ForeignKey(reportField, on_delete=models.CASCADE)
    report = models.ForeignKey(report, on_delete=models.CASCADE)


