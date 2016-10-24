
# Quake-o'-Lantern

__Hack-o'-Lantern '16__

![quakeolantern](./static/quakeolantern-320.gif)

Vibrate a miniture pumpkin whenever there's an earthquake somewhere in the world.

Movement lasts two seconds for each order of magnitude of the earthquake 
by default, e.g. M2 lasts four seconds and M4 lasts eight seconds. 

## Requirements

* Raspberry Pi with Internet connectivity
* Micro servo, e.g. [Continuous Rotation Micro Servo - FS90R](https://www.adafruit.com/products/2442)
* 6 volt power source, e.g. [4 x AA Battery Holder](https://www.adafruit.com/products/830)
* 1 x 1k ohm resistor
* 1 x Breadboard
* Various wires

## Setup

#### Wiring

See http://razzpisampler.oreilly.com/ch05.html#FIG7.15

#### Software

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Pumpkin

* Cut a hole in the bottom of the pumpkin that fits the body of the servo
* Scoop out all the meat
* Place some folder tissue inside the pumpkin to serve as padding for the servo
* Slide the servo into the pumpkin so that the horn is on the outside
  * _Note: A [wheel horn](https://www.servocity.com/146sh-standard-wheel-arm) seems to work best, but any one should do_

## Run

Using defaults:

```
python ./quakeolantern.py
```

Overriding with environment variables:

```
QOL_USGS_ATOM_URL="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.atom" \
QOL_USGS_CHECK_INTERVAL=240 \
QOL_SERVO_PIN=17 \
python ./quakeolantern.py
```

#### Environment Variables

<dl>
<dt>QOL_SECONDS_PER_MAGNITUDE</dt>
<dd>number of seconds to shake per magnitude, default: 2</dd>

<dt>QOL_SERVO_PIN</dt>
<dd>gpio pin for controlling the servo, default: 18</dd>

<dt>QOL_USGS_ATOM_URL</dt>
<dd>default: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.atom</dd>

<dt>QOL_USGS_CHECK_INTERVAL</dt>
<dd>interval in seconds to check for new eartquakes, default: 60</dd>
</dl>


## References

* USGS ATOM Syndication https://earthquake.usgs.gov/earthquakes/feed/v1.0/atom.php
* Servo wiring based on http://razzpisampler.oreilly.com/ch05.html
