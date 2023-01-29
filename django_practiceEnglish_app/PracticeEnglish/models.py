from django.db import models

class example(models.Model):
    name = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    example = models.CharField(max_length=500)

    def __str__ (self):
        return self.name
    
class phrase_say(models.Model):
    phrase = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.phrase
class phrase_off(models.Model):
    phrase = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.phrase
class phrase_afraid(models.Model):
    phrase = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.phrase

class verb_court(models.Model):
    verb = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.verb   
class verb_restaurant(models.Model):
    verb = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.verb
class verb_airport(models.Model):
    verb = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.verb
class verb_hotel(models.Model):
    verb = models.CharField(max_length=30)
    meaning = models.CharField(max_length=60)
    #example = models.CharField(max_length=500)

    def __str__ (self):
        return self.verb
    

class new_thing_me_too(models.Model):
    new = models.CharField(max_length=30)
    example = models.CharField(max_length=60)
  #  instead = models.CharField(max_length=1000)

    def __str__ (self):
        return self.new
class new_thing_ithink(models.Model):
    new = models.CharField(max_length=30)
   # example = models.CharField(max_length=60)
  #  instead = models.CharField(max_length=1000)

    def __str__ (self):
        return self.new
class new_thing_very(models.Model):
    new = models.CharField(max_length=30)
    example = models.CharField(max_length=60)
  #  instead = models.CharField(max_length=1000)

    def __str__ (self):
        return self.new