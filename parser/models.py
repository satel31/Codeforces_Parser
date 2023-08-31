from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Problem(models.Model):
    topics = models.TextField(verbose_name='Topics')
    solutions_amount = models.IntegerField(**NULLABLE, verbose_name='Solutions amount')
    problem_name = models.CharField(max_length=255, verbose_name='Problem name')
    index = models.CharField(max_length=100, verbose_name='Index')
    rating = models.IntegerField(**NULLABLE, verbose_name='rating')
    is_used = models.BooleanField(default=False, verbose_name='Is_used')

    def __str__(self):
        return f'Problem: {self.problem_name}'

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problems'
