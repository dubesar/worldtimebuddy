# worldtimebuddy
Get current time for all possible timezone using CLI (exclusively for developers)

Version - 0.1.2

[![Publish worldtimebuddy](https://github.com/dubesar/worldtimebuddy/actions/workflows/publish-package.yml/badge.svg)](https://github.com/dubesar/worldtimebuddy/actions/workflows/publish-package.yml)

```
Usage: worldtimebuddy [OPTIONS]

  Display current time for all timezones, major timezones, or a specific
  timezone.

Options:
  --format TEXT         DateTime format string
  --major               Show only major timezones
  -tz, --timezone TEXT  Show time for a specific timezone
  --list                List all available timezones
  --delta TEXT          Add or subtract time from a particular timezone
  --help                Show this message and exit.
```
### Installation:
1. Clone the repository locally
``` bash
git clone https://github.com/dubesar/worldtimebuddy.git
cd worldtimebuddy
```
2. Run the following code to install dependencies and worldtimebuddy
``` bash
pip install -r requirements.txt
python3 setup.py build
python3 setup.py install
```


### Usage:


1. Get all the timezones
```
> worldtimebuddy

Africa/Abidjan                 2024-10-06 13:49:11
Africa/Accra                   2024-10-06 13:49:11
....
```

2. Get all timezone in particular format
```
> worldtimebuddy --format '%A, %B %d, %Y %I:%M %p %Z'

Africa/Abidjan                 Sunday, October 06, 2024 01:49 PM GMT
Africa/Accra                   Sunday, October 06, 2024 01:49 PM GMT
Africa/Addis_Ababa             Sunday, October 06, 2024 04:49 PM EAT
...
```

3. Get major timezones

Currenlty only IST/PST/PDT/UTC by default. But user can set major timezones in their environment with name `MAJOR_TIMEZONES`, this tool will pick up those as the major
versions.
eg.
```
> MAJOR_TIMEZONES=["UTC", "Asia/Kolkata"]
> worldtimebuddy --major

UTC                            2024-10-06 13:50:26
PDT                            2024-10-06 06:50:26
Asia/Kolkata                   2024-10-06 19:20:26
```

4. Listing all timezones
```
> worldtimebuddy --list

Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
...
```

5. Getting a particular timezone
```
> worldtimebuddy --timezone UTC
UTC                            2024-10-06 19:33:35

> worldtimebuddy --timezone JST
Asia/Tokyo                     2024-10-07 04:33:35
...
```

6. Getting a difference of time from a particular timezone <br> (supported time formats: +/- min, hr, day) 
```
> worldtimebuddy --timezone UTC --delta +2hr
UTC                            2024-10-06 20:43:35
...
```