from django.db import models
from django.db import models
# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.name

class   Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('RPG', 'RPG'),
        ('Shooter', 'Shooter'),
        ('Strategy', 'Strategy'),

    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_multiplayer = models.BooleanField(default=False)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    cover_image = models.ImageField(upload_to='game_covers/')
# one-to-many
    developer1 = models.ForeignKey(Developer, on_delete=models.CASCADE,related_name='games')
# many-to-many
    platform = models.ManyToManyField(Platform)
    def __str__(self):
        return self.title
# one-to-one
class GameDetail(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    engine = models.CharField(max_length=100)
    hours_to_complete = models.IntegerField()
    steam_score = models.IntegerField()
    def __str__(self):
        return f"Details of {self.game.title}"
