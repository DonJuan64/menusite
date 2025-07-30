from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://imgs.search.brave.com/k0aUkD_2r1uX9P78hJIIiSsZJsfr4B0qQpxkaphHfAM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS12ZWN0/b3IvbWVudS1yZXN0/YXVyYW50XzI0OTA4/LTI0MTExLmpwZz9z/ZW10PWFpc19oeWJy/aWQmdz03NDA")
    def __str__(self):
        return self.item_name






