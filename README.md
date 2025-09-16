# PA3---Dangiwan

# PROBLEM 1
``` python
import pandas as pd
#accessing the functions within the pandas library and calling it as pd

cars = pd.read_csv('cars.csv')
#reading the cars.csv file, loading it and saving it to the variable cars

pd.concat([cars.head(), cars.tail()])
#the .head function displays the first 5 rows of the data frame
#the .tail function displays the last 5 rows of the data frame
#the function .concat concatenates the first 5 rows and last 5 rows of the data frame
```

# PROBLEM 2
``` python
import pandas as pd
#accessing the library pandas to use its functions and call it pd

cars = pd.read_csv('cars.csv')
#reading the cars.csv file, loading it and saving it to the variable cars

cars[1:6:2]
#splicing displays the first five rows with odd-numebered columns of the cars
```
``` python
cars.loc[cars['Model']=='Mazda RX4']
#the function .loc locates the element in the data frame under model which
#contains 'Mazda RX4'
```
``` python
cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]
# the function .loc locates the element in the data fram under model which
#contains 'Camaro Z28' and search for the value of its cyl
```
``` python
cars.loc[ (cars['Model'] == 'Mazda RX4 Wag') | 
(cars['Model'] == 'Ford Pantera L') |
(cars['Model'] == 'Honda Civic'), 
#the function .loc was used to find the models wanted under the column model
#the or condition was used so that only the specified models will be selected 
['cyl', 'gear']]
#after the models were selected, only the values under 'cyl' and 'gear' was displayed
```

