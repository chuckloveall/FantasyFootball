players = [
{
"name": "Michael Thomas",
"catches": 149,
"targets": 185
},
{
"name": "Julio Jones",
"catches": 99,
"targets": 157
},
{
"name": "Davante Adams",
"catches": 83,
"targets": 127
}
]
for player in players:
    name = player['name']
    catches = player['catches']
    targets = player['targets']
    catch_rate = catches/targets
    print(name + ' had a catch rate of ' + str(catch_rate))
