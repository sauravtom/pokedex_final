import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemonGo.settings')

import django
django.setup()

from search.models import Pokedex
from search.views import search_pokemon

def showDB():
    for c in Pokedex.objects.all():
        print str(c)

def populate2():
    for pokemon in search_pokemon('*',result_type='dict')[:10]:
        print pokemon
        add_pokemon(name=pokemon['name'],image_url=pokemon['image_url'])

    # Print out what we have added to the DB
    showDB()

def populate():
    add_pokemon(name='foodchamber',image_url='food.png')

    # Print out what we have added to the DB
    for c in Pokedex.objects.all():
        print str(c)

def add_pokemon(name, image_url, pokemon_type='N/A'):
    p = Pokedex.objects.get_or_create(pokemon_name=name, pokemon_image=image_url, pokemon_type=pokemon_type)[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    #print search_pokemon('*',result_type='dict')
    showDB()
    #populate2()