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
