
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
int speaker = 4;

void setup()
{
    

  Serial.begin(9600);
  lcd.init(); 
    pinMode(speaker, OUTPUT);
    
    

  
  //lcd.cursor(0,0);
                         // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
   // iterate over the notes of the melody.
  
  
  //lcd.print("Hello, world!");
  
}


void loop()

{
  lcd.backlight();
  
  while (Serial.available()>0){
      
      
      lcd.write(Serial.read());
      
      
      
      
      //lcd.clear();
        for (int i=0; i<30; i++) {
    digitalWrite(speaker, HIGH);
    delayMicroseconds(1000);
    digitalWrite(speaker, LOW);
    delayMicroseconds(1000);
    int speaker = 4;
  }
  
  
  
}

  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
    lcd.print("Center your face");

   //digitalWrite(4, LOW);
//lcd.print("SF06");
    
  }






