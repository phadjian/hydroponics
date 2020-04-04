/*
 *   dht11.c:
 *   Simple test program to test the wiringPi functions
 *   DHT11 test
 * 	 https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
 */

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MAXTIMINGS 85

//#define DHTPIN 1
#define DHTPIN 7

int dht11_dat[5] = {0,0,0,0,0};

int read_dht11_dat()
{
	uint8_t laststate = HIGH;
	uint16_t counter = 0;
	uint8_t j = 0, i;
	float f; // fahrenheit

	dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;

	// pull pin down for 18 milliseconds
	pinMode(DHTPIN, OUTPUT);
	digitalWrite(DHTPIN, LOW);
	delay(18);
	// then pull it up for 40 microseconds
	digitalWrite(DHTPIN, HIGH);
	delayMicroseconds(40); 
	// prepare to read the pin
	pinMode(DHTPIN, INPUT);

	// detect change and read data
	for ( i=0; i< MAXTIMINGS; i++) {
		counter = 0;
		while (digitalRead(DHTPIN) == laststate) {
			counter++;
			//printf("%d\n", counter);
			delayMicroseconds(1);
			if (counter == 255) {
				break;
			}
		}
		laststate = digitalRead(DHTPIN);

		if (counter == 255) break;

		// ignore first 3 transitions
		if ((i >= 4) && (i%2 == 0)) {
			// shove each bit into the storage bytes
			dht11_dat[j/8] <<= 1;
			if (counter > 50)
				dht11_dat[j/8] |= 1;
			j++;
		}
	}
	
	//printf("dht11_dat0=%d\n", dht11_dat[0]);
	//printf("dht11_dat1=%d\n", dht11_dat[1]);
	//printf("dht11_dat2=%d\n", dht11_dat[2]);
	//printf("dht11_dat3=%d\n", dht11_dat[3]);
	//printf("j=%d\n", j);
	
	// check we read 40 bits (8bit x 5 ) + verify checksum in the last byte
	// print it out if data is good
	if ((j >= 40) && 
			(dht11_dat[4] == ((dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF)) ) {
		f = dht11_dat[2] * 9. / 5. + 32;
		printf("Humidity = %d.%d %% Temperature = %d.%d *C (%.1f *F)\n", 
				dht11_dat[0], dht11_dat[1], dht11_dat[2], dht11_dat[3], f);
		if (f < 60) {
			return 1;
		} else if (f > 70) {
			return 2;
		}
		return 0;
	}
	else
	{
		return 0;
	}
}

int main (void)
{

	printf ("Raspberry Pi wiringPi DHT11 Temperature test program\n") ;

	if (wiringPiSetup () == -1)
		exit (1) ;
	
	int value = 0;
	
	while (1) 
	{
		value = read_dht11_dat();
		printf("value = %d\n", value);
		delay(5000); // wait 5sec to refresh
	}

	return 0 ;
}
