from django.db import models


class Tribunal(models.Model):
    codigo = models.CharField(max_length=10)
    sigla = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    site_principal = models.URLField()
    site_busca_1_f = models.URLField()
    site_busca_2_f = models.URLField()
    site_busca_1_e = models.URLField()
    site_busca_2_e = models.URLField()

    def __str__(self):
        return self.sigla

    def get_site(self, instancia, tipo):
        sites = {
            "primeirafisico": self.site_busca_1_f,
            "segundafisico": self.site_busca_2_f,
            "primeiraeletronico": self.site_busca_1_e,
            "segundaeletronico": self.site_busca_2_e
        }
        return sites[f"{instancia}{tipo}"]
