# familiar-crop-monitor

Using this sample GPS data do create harverts map


Py requirements | but not in this case, i'll use the sample file in geo/gps_...

```csv
$GNGGA,064656.00,3402.91778,S,15101.42545,E,1,12,0.62,140.8,M,18.6,M,,*5E
```
$GNGGA
Time, position, and fix related data of the receiver
064656.00
record timestamp in UTC timezone 06:46:56
3402.91778,S
latitude multiplied by 100. S for Southern Hemisphere
15101.42545,E
longitude multiplied by 100. E for Eastern Hemisphere

> At this point, i'm following this guy: https://python.plainenglish.io/receiving-and-processing-gps-data-using-external-receiver-with-python-24d3592ad2e0