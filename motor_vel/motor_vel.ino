/* 
 * rosserial::std_msgs::Int16 Test
 * Receives a Int16 input
 */

#include <ros.h>
#include <std_msgs/Int16.h>


ros::NodeHandle nh;

//variable for storing motor velocities
int m11,m12,m21,m22;

//pins to which motor is to be connected
int m1p1=3,m1p2=5,m2p1=9,m2p2=10;

/*messageCb1 is callback function for motor1
* messageCb2 is callback function for motor2*/
void messageCb1( const std_msgs::Int16& msg){
  int x;
  x = msg.data;
  unpack1(x);
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}
void messageCb2( const std_msgs::Int16& msg){
  int y;
  y = msg.data;
  unpack2(y);
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}

std_msgs::Int16 test;
ros::Subscriber<std_msgs::Int16> m1("motor_vel1", &messageCb1);
ros::Subscriber<std_msgs::Int16> m2("motor_vel2", &messageCb2);
ros::Publisher p("my_topic", &test);

/*since the velocities of motor are 8-bit data
* the values of signal on pin1 and pin2 are packed
* into 16-bit data, so there is individual unpacking 
* for both the motor_vel*/

void unpack1(int x){
  if(x<0){
    m11=0;
    m12=x;
  }
  else{
    m11=x;
    m12=0;
  }
}
void unpack2(int y){
  if(y<0){
    m21=0;
    m22=255-y;
  }
  else{
    m21=y;
    m22=0;
  }
}
void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.advertise(p);
  nh.subscribe(m1);
  nh.subscribe(m2);
  digitalWrite(4,LOW);
  pinMode(m1p1,OUTPUT);
  pinMode(m1p2,OUTPUT);
  pinMode(m2p1,OUTPUT);
  pinMode(m2p2,OUTPUT);

}

void loop(){
  analogWrite(m1p1,m11);
  analogWrite(m1p2,m12);
  analogWrite(m2p1,m21);
  analogWrite(m2p2,m22);
  test.data=m11+m12+m21+m22; 
  p.publish( &test );
  nh.spinOnce();
  delay(10);
}

