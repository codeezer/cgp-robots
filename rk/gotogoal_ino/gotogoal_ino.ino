
float R = 3.3;
float L = 13.5;

float x = 0;
float y = 50;
float phi = 0;

float goal_x=100;
float goal_y=50;

float vel_robot=0;
float omega_robot=0;

float omega_left,omega_right,left_wheel_distance,right_wheel_distance,distance_centre,error;
float prev_encoder_left=0,prev_encoder_right=0;

void gotogoal();

void setup() {

}

void loop() {
 gotogoal();
}

void gotogoal(){
 float encoder_right,encoder_left,del_encoder_left,del_encoder_right,error,error_dash;
 
 /*get encoder readings*/
 del_encoder_left = 20;
 del_encoder_right = 30;
  
 prev_encoder_left=
 prev_encoder_right=

 left_wheel_distance = 2*PI*R*del_encoder_left/60;
 right_wheel_distance = 2*PI*R*del_encoder_right/60;
 distance_centre = (left_wheel_distance + right_wheel_distance)/2;

 x += distance_centre*cos(phi);
 y += distance_centre*sin(phi);

 phi += (right_wheel_distance-left_wheel_distance)/L;

 error = atan((goal_y - y)/(goal_x - x)) - phi;  
 error_dash = atan2(sin(error),cos(error));

 omega_robot = 10*error_dash;
 vel_robot = 1; 
 /*motioncommand(vel_robot,omega_robot);*/

}
