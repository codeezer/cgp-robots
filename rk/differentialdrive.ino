
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
const float L= 0.05  ;
const float R= 0.015 ;

void motioncommand(int v, int w);

float integral1,integral2;
float previous_error1,previous_error2;
float kp_1=1,
      kd_1=0,
      ki_1=0,
      kp_2=1,
      kd_2=0,
      ki_2=0;

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
  float v,w;
  motioncommand(v,w);
}

void motioncommand(int v, int w)
{
  /*v_right and v_left may be calculated before? less computation on arduino?
     */

  float v_right,v_left,error,drive,derivative;   
  v_right = (2*v+w*L)/(2*R);
  v_left = (2*v-w*L)/(2*R);
 
  /*get current left and right wheel velocities*/
  float measuredright,measuredleft;
 
  error = v_right - measuredright ;                /*PID*/
  integral1 = integral1 + error;                  
  derivative = error - previous_error1;
  drive = kp_1*error + kd_1*derivative + ki_1*integral1;
  previous_error1 = error;
  v_right = drive;

  error = v_left - measuredleft;
  integral2 = integral2 + error;
  derivative = error - previous_error2;
  drive = kp_2*error + kd_2*derivative + ki_2*integral2;
  previous_error2 = error;
  v_left=drive;
  
  if(v_right<0)                   /*direction foward athawa reverse garna*/
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

