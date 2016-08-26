#include <Wire.h> 
#include <HMC5883L.h> 

HMC5883L compass; 

void setup() 
{ 
  Serial.begin(9600);
  Wire.begin();
  compass = HMC5883L();
  compass.SetScale(1.3);
  compass.SetMeasurementMode(Measurement_Continuous);
} 
void loop() 
{
  int xDegree = get_angle();
  Serial.println(xDegree);
  delay(1000); 
}


int get_angle(){
  MagnetometerRaw raw = compass.ReadRawAxis(); 
  MagnetometerScaled scaled = compass.ReadScaledAxis(); 
  float xHeading = atan2(scaled.YAxis, scaled.XAxis); 
  //float yHeading = atan2(scaled.ZAxis, scaled.XAxis); 
  //float zHeading = atan2(scaled.ZAxis, scaled.YAxis); 
  
  if(xHeading < 0) xHeading += 2*PI; 
  if(xHeading > 2*PI) xHeading -= 2*PI; 
  //if(yHeading < 0) yHeading += 2*PI; 
  //if(yHeading > 2*PI) yHeading -= 2*PI; 
  //if(zHeading < 0) zHeading += 2*PI; 
  //if(zHeading > 2*PI) zHeading -= 2*PI;
  float xDegrees = xHeading * 180/M_PI; 
  //float yDegrees = yHeading * 180/M_PI; 
  //float zDegrees = zHeading * 180/M_PI; 
  return xDegrees;
}
