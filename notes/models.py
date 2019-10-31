from django.db import models
from django.shortcuts import redirect, reverse

LABEL_CHOICES = (
    ('WARNING', 'warning'),
    ('PRIMARY', 'primary'),
    ('SECONDARY', 'secondary')
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=9)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finish_item_url(self):
        return reverse("finish-note-item", kwargs={
            'id': self.id
        })

    def get_recover_item_url(self):
        return reverse("recover-note-item", kwargs={
            'id': self.id
        })

    def get_delete_item_url(self):
        return reverse("delete-note-item", kwargs={
            'id': self.id
        })
