from django.db import models

class Login(models.Model):
    email = models.EmailField(max_length=50, default="null")
    password = models.CharField(max_length=16, default="null")
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
