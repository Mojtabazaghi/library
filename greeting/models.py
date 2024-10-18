from django.db import models

class Computer(models.Model):
    computer_name = models.CharField(max_length=20)
    computer_price = models.IntegerField()
    cpu = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    graphic = models.CharField(max_length=20)

    def __str__(self):
        return f'computer name: {self.computer_name} price: {self.computer_price} Rials'

class Monitor(models.Model):
    monitor_name = models.CharField(max_length=20)
    monitor_price = models.IntegerField()
    fullhd = models.CharField(max_length=20)
    oled = models.CharField(max_length=20)

    def __str__(self):
        return f'monitor name {self.monitor_name} monitor price {self.monitor_price} fullhd {self.fullhd} oled {self.oled}'

class Comment(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, null=True, blank=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=20)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} {self.text} time {self.created_at}'
