#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>

//*** Motor Driver ******
#define aPwm 6
#define aIn1 7
#define aIn2 8

#define bPwm 10
#define bIn1 12
#define bIn2 13
//***********************

//dilip
const int ENA = 6;
const int ENB = 10;
const int IN1 = 7;
const int IN2 = 8;
const int IN3 = 12;
const int IN4 = 13;

const int Vmax=100;


void motioncommand(int v, int w);

float integral1,integral2;
float previous_error1,previous_error2;
float kp_1=1,
      kd_1=0,
      ki_1=0,
      kp_2=0.8,
      kd_2=0,
      ki_2=0;
////////////////////////////////

//*** Encoder *********
#define encAClk 2     //Interrupt Pin
#define encADT 4
#define encBClk 3     //Interrupt Pin
#define encBDT 5
//*********************
Encoder knobRight(encAClk, encADT);
Encoder knobLeft(encBClk, encBDT);

float R = 0.033;
float L = 0.135;

float x = 0;
float y = 0;
float phi = PI;

float previous_error=0;
int time=0;
int prev_time=0;
float goal_x=1;
float goal_y=0;

float vel_robot=0;
float omega_robot=0;

float left_wheel_distance=0,right_wheel_distance=0,distance_centre=0,error=0;
int prev_encoder_left=0,prev_encoder_right=0;

void gotogoal();

void setup() {
    
   pinMode(ENA, OUTPUT);
   pinMode(IN1, OUTPUT);
   pinMode(IN2, OUTPUT);
   pinMode(IN3, OUTPUT);
   pinMode(IN4, OUTPUT);
   pinMode(ENB, OUTPUT);
  /*
    //*** Motor Driver **
    pinMode(aPwm, OUTPUT);
    pinMode(aIn1, OUTPUT);
    pinMode(aIn2, OUTPUT);
    pinMode(bPwm, OUTPUT);
    pinMode(bIn1, OUTPUT);
    pinMode(bIn2, OUTPUT);
    //*****************
    */
    Serial.begin(9600);

}

int previous_encoder_left=0;
int current_encoder_left=0;

void loop() {
  
  
  
  current_encoder_left = knobRight.read();
 // int current_encoder_right = knobLeft.read();
  motioncommand(6,0);
  Serial.println(current_encoder_left - previous_encoder_left);
  Serial.print(" ");
  previous_encoder_left = current_encoder_left;
  //Serial.print(current_encoder_left);
  time = millis();
  delay(50 - (time-prev_time)); 
  prev_time = millis();
  
  //gotogoal();
}

void motioncommand(int v, int w)
{
  /*v_right and v_left may be calculated before? less computation on arduino?
     */
  float cmd_vel=0;
  float v_right,v_left,error,drive,derivative;   
  v_right = (2*v+w*L)/(2*R);
  //v_left = (2*v-w*L)/(2*R);
  v_left =6;
  /*get current left and right wheel velocities*/
  float measuredright,measuredleft;
  measuredleft=current_encoder_left-previous_encoder_left;
  
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
  cmd_vel=drive;
  
 /* if(v_right<0)                   //direction foward athawa reverse garna
  {
    digitalWrite (IN1, LOW);
    digitalWrite (IN2, HIGH);
  }
  else 
  {
    digitalWrite (IN2, LOW);
    digitalWrite (IN1, HIGH);
   }
   
  analogWrite(ENA,255/Vmax*v_fright);
  */
   
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
  analogWrite(ENA,255/12*cmd_vel);
 
  
  // analogWrite(ENB,255/Vmax*v_right); 
  
}


