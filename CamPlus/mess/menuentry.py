import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CamPlus.settings')

import django
django.setup()

from mess.models import menu


def menuupd():
    menu.objects.all().delete()
    menu.objects.create(day="Sunday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Monday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Tuesday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Wednesday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Thursday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Friday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")
    menu.objects.create(day="Saturday",brk='Chole Khulche<br>Boiled Egg(L)<br>Bread Butter/Jam<br>Masala Sprouts<br>Tea/Coffee<br>Milk(L)<br>Cornflakes/Bournvita',lun="Rajma<br>Lauki<br>Plain Rice<br>Plain & Butter Roti<br>Veg Raita(L)<br>Salad<br>Papad(L)",snk="Namkeen Poha(L)<br>Meethi Chatney<br>Coffee<br>Rasna",din="Aloo capsicum<br>Black Masoor Dal<br>Veg Fried Rice<br>Plain & Butter Roti<br>Salad<br>Peda(L)")

if __name__ == '__main__':
    print("updating menu")
    menuupd()
    print("updated menu")
