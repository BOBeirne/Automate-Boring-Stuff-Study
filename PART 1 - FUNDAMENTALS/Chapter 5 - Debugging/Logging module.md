
# Logging

```python
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

## Logging levels 

in config: 

``` python
level=logging_logtype()
```

* **DEBUG** - lowest lvl, small details, diagnosing problems
* **INFO** - information along the program run
* **WARNING** - indicate potential problem that does not prevent prog from working but it might do in future
* **ERROR** - record error that caused program to fail to do something
* **CRITICAL** - highest lvl, fatal error that causer (or is about) to cause program to stop running entirely

## Disabling logging

* it's good practice to keep this near import logging line for easily disabling it

```python 
logging.disable(logging.CRITICAL) 
``` # will suppress all log messages at that level or lower

