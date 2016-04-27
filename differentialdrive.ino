
/* A=left B=right motor
   IN1,IN2(direction control) for left motor
   similarly for right motor.
   pin can be set as required
*/

const int ENA = 9;
const int ENB = 10;
const int IN1 = 3;
const int IN2 = 4;
const int IN3 = 5;
const int IN4 = 6;

const int Vmax=100;
const int L= 0.05  ;
const int R= 0.015 ;

void motioncommand(int v, int w)

void setup()
{
   pinMode(ENA, OUTPUT);
   pinMode(IN1, OUTPUT);
   pinMode(IN2, OUTPUT);
   pinMode(IN3, OUTPUT);
   pinMode(IN4, OUTPUT);
}


void loop()
{
  /*get the required velocity and rotational speed after comparing
  current trajectory to the desired one (v,w)*/
  motioncommand(v,w);

}

void motioncommand(int v, int w)
{
  /*v_right and v_left may be calculated before? less computation on arduino?
     */
  v_right = (2*v+w*L)/(2*R);
  v_left = (2*v-w*L)/(2*R);
  
  /*direction foward athawa reverse garna*/
  if(v_right<0)
  {
    digitalWrite (IN1, LOW);
    digitalWrite (IN2, HIGH);
  }
  else 
  {
    digitalWrite (IN2, LOW);
    digitalWrite (IN1, HIGH);
   }
   
  analogWrite(ENA,255/Vmax*v_right);
 
   
   if(v_left<0)
  {
    digitalWrite (IN3, LOW);
    digitalWrite (IN4, HIGH);
  }
  else 
  {
    digitalWrite (IN4, LOW);
    digitalWrite (IN3, HIGH);
   }
   
   analogWrite(ENB,255/Vmax*v_left); 
  
}


