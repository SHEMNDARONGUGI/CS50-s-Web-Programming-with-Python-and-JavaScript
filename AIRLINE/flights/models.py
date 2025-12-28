from django.db import models

# PS C:\Users\user\Desktop\CS50\airline> python manage.py shell
# 7 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from flights.models import Flight
# >>> f = Flight(origin="New York", destination="London", duration=415)
# >>> f.save()
# > Flight.objects.all()
# <QuerySet [<Flight: Flight object (1)>]>
#  flights = Flight.objects.all()
# >>> flights
# <QuerySet [<Flight: 1 New York to London>]>

# Ctrl click to launch VS Code Native REPL
# Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> jfk = Airport(code="JFK", city="New York")
# >>> jfk.save()
# >>> lhr = Airport(code="LHR", city="London 
#   File "<console>", line 1
#     lhr = Airport(code="LHR", city="London
#                                    ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> lhr = Airport(code="LHR", city="London"
# ... lhr = Airport(code="LHR", city="London")
#   File "<console>", line 1
#     lhr = Airport(code="LHR", city="London"
#                  ^
# SyntaxError: '(' was never closed
# >>> lhr = Airport(code="LHR", city="London")
# >>> lhr.save()
# >>> cdg = Airport(code="CDG",city="Paris")  
# >>> cdg.save()
# >>> nrt =(code="NRT", city="Tokyo")
#   File "<console>", line 1
#     nrt =(code="NRT", city="Tokyo")
#           ^^^^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# >>> nrt =Airport(code="NRT", city="Tokyo") 
# >>> nrt.save
# <bound method Model.save of <Airport: Tokyo (NRT)>>
# >>> nrt.save()
# >>> 
# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"
    
