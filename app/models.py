from django.db import models

TRANSACTION_TYPE = (
    ('income', 'income'),
    ('expense', 'expense')
)

TRANSACTION_REASON = (
    ('uber','uber'),
    ('grocery stores', 'grocery stores'),
    ('food','food'),
    ('water can', 'water can'),
    ('other', 'other')
)

class User(models.Model):
    id=models.UUIDField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.id


class Transaction(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=10,choices=TRANSACTION_TYPE)
    date=models.DateField()
    reason=models.CharField(max_length=20, choices=TRANSACTION_REASON)
    other_reason=models.CharField(max_length=50)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return self.id