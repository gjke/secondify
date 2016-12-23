## Usage

1. Clone this repository ```git clone https://github.com/gjke/secondify.git```
2. Make sure that the folder containing secondify is on your classpath

```
import secondify
secondify.parse('1d').minutes() # returns 1440
secondify.parse('120m').hours() # returns 2.0
```

### The following time specifiers are supported:
* s for seconds
* m for minutes
* h for hours
* d for days
* w for weeks
* y for years