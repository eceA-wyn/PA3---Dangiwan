import pandas as pd

cars = pd.read_csv('cars.csv')

cars[1:6:2]

#----End Of Cell----

cars.loc[cars['Model']=='Mazda RX4']

#----End Of Cell----

cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]

#----End Of Cell----

cars.loc[ (cars['Model'] == 'Mazda RX4 Wag') | 
(cars['Model'] == 'Ford Pantera L') |
(cars['Model'] == 'Honda Civic'), 
['cyl', 'gear']]

#----End Of Cell----


#----End Of Cell----


#----End Of Cell----

