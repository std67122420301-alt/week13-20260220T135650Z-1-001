types = [
  'Grass','Ice','Fighting','Poison',
  'Normal','Fire', 'Water','Electric',
  'Ground','Flying','Psychic','Bug',
  'Rock', 'Ghost','Dragon','Dark',
  'Steel','Fairy'
]
from pokemon.models import Type
def create_pokemon_types():
  for type in types:
    pt = Type(name=type)
    db.session.add(pt)
    db.session.commit(pt)