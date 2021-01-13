from django.db import models

# Create your models here.
class Silnik(models.Model):
    kod = models.CharField(max_length=30)
    pojemnosc = models.IntegerField()
    moc = models.IntegerField()
    odciecieObrotow = models.IntegerField()
    kompresja = models.CharField(max_length=10)

    def __str__(self):
        return self.kod

class Modele(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=30)
    lataProdukcji = models.CharField(max_length=30)
    silnik = models.ForeignKey(Silnik, on_delete=models.DO_NOTHING)
    nadwozie = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa