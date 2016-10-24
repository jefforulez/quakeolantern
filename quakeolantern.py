#!/usr/bin/python

__author__  = "@jefforulez"

import os, re, sys, time
import subprocess

import RPi.GPIO as GPIO
import feedparser

#
# environment variables
#

print "+ initializing globals"

USGS_ATOM_URL = os.getenv( 'QOL_USGS_ATOM_URL', \
	"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.atom" )
print "- USGS_ATOM_URL: {}".format( USGS_ATOM_URL )

USGS_CHECK_INTERVAL = int( os.getenv( 'QOL_USGS_CHECK_INTERVAL', 60 ) )
print "- USGS_CHECK_INTERVAL: {}".format( USGS_CHECK_INTERVAL )

SERVO_PIN = int( os.getenv( 'QOL_SERVO_PIN', 18 ) )
print "- SERVO_PIN: {}".format( SERVO_PIN )

SECONDS_PER_MAGNITUDE = int( os.getenv( 'QOL_SECONDS_PER_MAGNITUDE', 2 ) )
print "- SECONDS_PER_MAGNITUDE: {}".format( SECONDS_PER_MAGNITUDE )

#
#
#

def trigger_servo ( magnitude ):

	print "+ trigger_servo(), magnitude: {}".format( magnitude )

	print "- initializing gpio"
	GPIO.setwarnings( False )
	GPIO.setmode( GPIO.BCM )
	GPIO.setup( SERVO_PIN, GPIO.OUT )
	trigger_servo.pwm = GPIO.PWM( SERVO_PIN, 100 )

	trigger_servo.pwm.start( 5 )

	loops = int( int( magnitude ) * SECONDS_PER_MAGNITUDE ) 
	print "- begin movement, loops: {}".format( loops )

	for second in range( 0, loops ):

		trigger_servo.pwm.ChangeDutyCycle( 10 )
		time.sleep(.2)

		trigger_servo.pwm.ChangeDutyCycle( 20 )
		time.sleep(.2)

		trigger_servo.pwm.ChangeDutyCycle( 15 )
		time.sleep(.2)

		trigger_servo.pwm.ChangeDutyCycle( 25 )
		time.sleep(.2)

		trigger_servo.pwm.ChangeDutyCycle( 15 )
		time.sleep(.2)

	trigger_servo.pwm.stop()

	print "- finish movement"

	return

#
#
#

def check_atom ():

	print "+ check_atom()"

	if not hasattr( check_atom, "quakes" ):
		check_atom.quakes = dict()

	if not hasattr( check_atom, "modified" ):
		 check_atom.modified = 0

	feed = feedparser.parse( USGS_ATOM_URL, modified=check_atom.modified )

	if hasattr( feed, "modified" ):
		print "- feed.modified: {}".format( feed.modified )
		check_atom.modified = feed.modified

	if ( len( feed.entries ) == 0 ):
		print "- no current earthquakes, feed.status: {}".format( feed.status )
		return

	id = feed.entries[0]["id"]
	title = feed.entries[0]["title"]

	if ( id in check_atom.quakes ):
		print "- skipping known quake, id: {}".format( id )
		return

	print "- id: {}".format( id )
	print "- title: {}".format( title )

	m = re.search( "^M\s(\d+)", title )

	if not m:
		print "! unable to determine magnitude"
		return

	check_atom.quakes[ id ] = title

	return m.group(1)

#
#
#

if __name__ == "__main__":

	while ( 42 ):
		magnitude = check_atom()
		if magnitude:
			trigger_servo( magnitude )
		time.sleep( USGS_CHECK_INTERVAL )




