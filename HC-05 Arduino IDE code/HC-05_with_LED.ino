// This code is a slightly modified version of the code found in this tutorial by Dejan Nedelkovski:
// https://howtomechatronics.com/tutorials/arduino/arduino-and-hc-05-bluetooth-module-tutorial/

#define ledPin 7
int state = 0;

void setup() {
	pinMode(ledPin, OUTPUT);
	digitalWrite(ledPin, LOW);
	Serial2.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
	if (Serial2.available() > 0) { // Checks whether data is coming from the serial port
		state = Serial2.read(); // Reads the data from the serial port
	}
	if (state == '0') {
		digitalWrite(ledPin, LOW); // Turn LED OFF
		Serial2.println("LED: OFF"); // Send back, to the phone, the String "LED: ON"
		state = 0;
	}
	else if (state == '1') {
		digitalWrite(ledPin, HIGH);
		Serial2.println("LED: ON");;
		state = 0;
	}
}
