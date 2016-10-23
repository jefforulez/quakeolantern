
# Quake-o'-Lantern

__Hack-o'-Lantern '16__

![quakeolantern](./static/quakeolantern-320.gif)

Vibrate a miniture pumpkin whenever there's an earthquake somewhere in the world.

Movement lasts one second for each order of magnitude of the earthquake,
e.g. M2 lasts two seconds and M4 lasts four seconds.

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

#### Optional Environment Variables

<dl>
<dt>QOL_USGS_ATOM_URL</dt>
<dd>default: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.atom</dd>
</dl>

<dl>
<dt>QOL_USGS_CHECK_INTERVAL</dt>
<dd>interval in seconds to check for new eartquakes, default: 60</dd>
</dl>

<dl>
<dt>QOL_SERVO_PIN</dt>
<dd>gpio pin for controlling the servo, default: 18</dd>
</dl>

## References

* Servo wiring based on http://razzpisampler.oreilly.com/ch05.html
