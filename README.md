# dash.poltly-in-python
*this file is written in markdown*


# data analsis in Python course final project, Developer Guide
-------


This is the project conducted by group10, based on dash.plotly, using real-world dataset to create a local interactive Web interface, at a total of 366 observations.
More specifically, we focus on the analyze of "The Demand of Rental Bikes During year 2012 in Capital Bikeshare System" by visualizing 
as a preliminary research.


**research object**:
with three qualitative variables:

    *season*: season (1:winter, 2:spring, 3:summer, 4:fall)

    *holiday*: weather day is holiday or not
    
    *weathersit*:
        1: Clear, Few clouds, Partly cloudy, Partly cloudy
        2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
        3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
        4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

and quantitative variables selecting from:

    *temp*: Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)

    *atemp*: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)

    *hum*: Normalized humidity. The values are divided to 100 (max)

    *windspeed*: Normalized wind speed. The values are divided to 67 (max)

    *cnt* (more in a dependent variable sense for mldm): count of total rental bikes including both casual and registered


## Start $project by running:

    .../app.py

## Application structure
-------

### requirements

      dash>=2.6.1
      dash-bootstrap-components>=1.1.0
      dash-mantine-components>=0.10.1
      dash-iconify>=0.1.2
      numpy
      pandas
      dash-bootstrap-templates

### our environment

      Python 3.8.2,
      dash==2.7.1, dash-bootstrap-components==1.2.1, dash-bootstrap-templates==1.0.7, dash-core-components==2.0.0, dash-html-components==2.0.0, dash-table==5.0.0，plotly==5.11.0, numpy==1.18.2， pandas==1.0.3


This app has structure as in the following:
```
- app.py 
- pages
    - #for visualization
       |-- bar_charts.py
       |-- box_whisker.py
       |-- cluster_bar_charts.py
       |-- histograms.py
       |-- scatter_charts.py
    - #for table
       |-- dashboard.py
    - #for setting
       |-- __init__.py
       |-- not_found_404.py
       |-- default_fig.py
    - home.py
- views
    - #original dataset
       |-- bike.xlsx
       |-- data_content.txt
    - #processed dataframes
    - data.py
```


For more pages eg. more visualization, add in `-pages` folder and modify `-app.py` line 41. For updating data, check `-views-bike.xisx`. 
For modifying dataframe, check `-views-data.py`. Overall the filename is very story-telling.

## Features
-------

- with a light and dark theme switch component from the dash-bootstrap-templates library
- defalt_fig style
- selecting columns/ rows of the table with some reasonable restrictions (one qualitative and at most two quantitative, and can choose range of cnt)
- good robustness


## Contribute
-------

- Source Code: github.com/Lecter314/dash.poltly-in-python (a private one, please contact author before browsing)

## Support
-------

If you are having using/developing related issues, please let us know.
We have a mailing list located at: tyuy@edu.hse.ru

## License
-------

The project is licensed under the BSD license.
