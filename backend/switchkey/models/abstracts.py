"""abstract model for created, updated timestamps"""

from django.db import models


class TimeStamp(models.Model):
    """Database model for created and updated timestamps"""

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"""created at : {self.created} ,
            modified at : {self.modified}"""
