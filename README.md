Houssam Eddine BAHHOUS houssam-eddine.bahhous@etu.univ-orleans.fr
Amal BAZHAR amal.bazhar@etu.univ-orleans.fr
Hasnaa ECHCHATBI hasnaa.echchatbi@etu.univ-orleans.fr
Nina METROUH nina.metrouh@etu.univ-orleans.fr

#Question 1

Création de projet cc :
    $django-admin startproject cc
Création de l'application collec_management
    $python manage.py startapp collec_management

    $python manage.py runserver


#Question 3

    $python manage.py makemigrations
    $python manage.py migrate


#Question 4

    $python manage.py shell
        $from collec_management.models import Collec
        $collec = Collec(title="",description="",date="")
        $collec.save()

        .
        .
        .
        $exit()
    $mkdir collec_management/fixtures
    $python manage.py dumpdata collec_management.Collec > collec_management/fixtures/examples.json
    $python manage.py loaddata examples



        





