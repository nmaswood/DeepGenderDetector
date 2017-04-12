# Gender Detector

I have 30,000 > data points of actors from imdb and their gender. I want to see if I can use this data to build a tool that identify the gender of an arbitary name.

##  Access the Data

In order to read the data as a list of tuples<name, gender>

```python
from data import People

name_gender_data = People.read()

```
