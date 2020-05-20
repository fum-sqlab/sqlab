from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class StepStatuses:
    INITIATED = 1
    ACTIVE = 2
    SKIPPED = 3
    DONE = 4


class CycleStatuses:
    INITIATED = 1
    STARTED = 2
    STOPPED = 3
    FINISHED = 4


CYCLE_STATUS_CHOCIES = (
    (CycleStatuses.INITIATED, 'ایجاد شده'),
    (CycleStatuses.STARTED, 'شروع شده'),
    (CycleStatuses.STOPPED, 'متوقف شده'),
    (CycleStatuses.FINISHED, 'به پایان رسیده'),
)


class WorkCycle(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    status = models.PositiveSmallIntegerField(
        choices=CYCLE_STATUS_CHOCIES,
        default=CycleStatuses.INITIATED,
        verbose_name='وضعیت')
    create_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    close_date = models.DateTimeField(verbose_name='تاریخ پایان')

    creator = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='cycles',
        verbose_name='ایجاد کننده'
    )
