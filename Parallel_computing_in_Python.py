""" Created in Mar 2019 by Paul A. Gureghian """

""" Parallel computing allows you to carry out many calculations at the same time. """ 

### Import packages 
import collections
import multiprocessing

### Define a dataset
Scientist = collections.namedtuple('Scientist',['name', 'born',])
                                   
scientists = (
             Scientist(name='Ada Lovelace', born=1815),
             Scientist(name='Emmy Noether', born=1882),
             Scientist(name='Marie Curie', born=1867),
             Scientist(name='Tu Youyou',born=1930),
             Scientist(name='Ada Yonath', born=1939),
             Scientist(name='Vera Rubin', born=1928),
             Scientist(name='Sally Ride', born=1951),
             )

### Define 'process_item' function
def process_item(item):
    
    return{'name': item.name, 'age': 2017 - item.born} 
            
### Setup a 'multiprocessing pool' 
pool = multiprocessing.Pool()
result = pool.map(process_item, scientists)   

### Print data transformation results
print(tuple(result)) 



 