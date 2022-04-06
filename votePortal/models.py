from django.db import models

class Districts(models.Model):
  name = models.CharField(max_length=50,null=True )
  code = models.CharField(max_length=4,null=True )

  def __str__(self) -> str:
      return self.code