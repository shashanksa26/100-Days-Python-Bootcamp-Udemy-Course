#nest
capitals={
    "france":"paris",
    "Germany":"Berlin"
}

#Nesting a List in a Dictionary
travel_log1 ={
    "france":["paris","Lille","Dijon"],
    "Germany":["berlin","Hamburg","Stuttgart"]
}

#Nesting Dictioanry in a Dictionary
travel_log2 ={
    "france":{"cities_visited":["paris","Lille","Dijon"],"total_visit":12},
    "Germany":{"cities_visited":["berlin","Hamburg","Stuttgart"],"total_visit":5}
}
#Nesting Dictionary in a List:

travel_log3 =[
{
    "Country":"france",
    "cities_visited":["paris","Lille","Dijon"],
    "total_visit":12,
},
{
    "Country":"Germany",
    "cities_visited":["berlin","Hamburg","Stuttgart"],
    "total_visit":5
    }
]
