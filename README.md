# Gender Detector

I scraped the names and genders of 50,000 thousand people from IMDB. Using this Data I want to accurately guess a person's gender given their name.

##  Access the Data

In order to process/ read the data as a pandas pd

```python
from data import People

name_gender_data = People.read()
```
