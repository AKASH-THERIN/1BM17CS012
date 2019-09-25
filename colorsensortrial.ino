const int s0=8;
const int s1=9;
const int s2=12;
const int s3=11;
const int out =10;

int red=2;
int  green=3;
int blue=4;
void setup() {
 Serial.begin(9600);
 pinMode(s0,OUTPUT);
 pinMode(s1,OUTPUT);
 pinMode(s2,OUTPUT);
 pinMode(s3,OUTPUT);
 pinMode(out,INPUT);
 pinMode(red,OUTPUT);
 pinMode(green,OUTPUT);
 pinMode(blue,OUTPUT);
 digitalWrite(s1,HIGH);
 
}

void loop() {
  // put your main code here, to run repeatedly:
 color();
 Serial.print("R Intensity");
 Serial.print(red,DEC);
 Serial.print("G Intensity");
 Serial.print(green,DEC);
 Serial.print("b Intensity");
 Serial.print(blue,DEC);

 if(red<blue && red < green)
 {
  Serial.println(" (red color)");
  digitalWrite(red,HIGH);
  digitalWrite(green,LOW);
  digitalWrite(blue,LOW);
  
 }
 else if(blue < red && blue < green)
 {
  Serial.println(" (blue color)");
  digitalWrite(red,LOW);
  digitalWrite(green,LOW);
  digitalWrite(blue,HIGH);
 }
 else if(green < red &&  green< blue)
 {
  Serial.println(" (green color)");
  digitalWrite(red,LOW);
  digitalWrite(green,HIGH);
  digitalWrite(blue,LOW);
 }
 else {
  Serial.println();
  
 }
 delay(300);
 digitalWrite(red,LOW);
  digitalWrite(green,LOW);
  digitalWrite(blue,LOW);
 
}
void color()
{
  digitalWrite(s2,LOW);
  digitalWrite(s3,LOW);
  red=pulseIn(out,digitalRead(out)==HIGH?LOW :HIGH);
   digitalWrite(s3,HIGH);
   blue=pulseIn(out,digitalRead(out)==HIGH?LOW :HIGH);
   digitalWrite(s2,HIGH);
   green=pulseIn(out,digitalRead(out)==HIGH?LOW :HIGH);
}
