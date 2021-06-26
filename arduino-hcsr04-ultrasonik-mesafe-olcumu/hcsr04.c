/*
https://ferhatcicek.com/2017/03/19/hc-sr04-ultrasonik-modul-kullanarak-arduino-uno-platformunda-mesafe-olcumu-ornegi-1/
*/

/*
HC-SR04 ornegi

 *  Arduino | HC-SR04 
 *  -------------------
 *    5V    |   VCC 
 *    10    |   Trig
 *    9     |   Echo 
 *    GND   |   GND
*/
 
//hc-sr04 sensorune ait kullanicak trigger ve echo portlari
const int trig_pin = 10;
int echo_pin = 9;
 
//uygulamada kullanilacak guvenli mesafe
int guvenlik_mesafesi = 10;
 
//uygulamada gunveli mesafe bilgisini ledle takip edebilmek icin
//kullanilacak pinler
int led_mesafe_guvenli = 3, 
led_mesafe_guvensiz = 2;
 
void setup() {
  //uygulada kullanilacak pinlerin durumunu ayarlayalim
  Serial.begin(9600);
  
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  
  pinMode(led_mesafe_guvenli, OUTPUT);
  pinMode(led_mesafe_guvensiz, OUTPUT);  
}
 
void loop()
{
  //sesin_suresi milisaniye cinsinden bir veridir.
  //bu veri santimetreye cevrilmektedir.
  long sesin_suresi, mesafe_cm;
 
 
  //olcum oncesi trigger low yapilarak sinyal gonderilmesi engellenir
  //10 ms sinyal gonderildikten sonra  
  //bunun amaci olasi hata olcumlerini minimize etmektedir
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);
 
  //
  pinMode(echo_pin, INPUT);
  sesin_suresi = pulseIn(echo_pin, HIGH);
 
  // olculen sureyi cm olarka mesafeye cevirme
  mesafe_cm = sesin_suresi / 29 / 2 ;
 
  //modulun olcum sinirlari disinda ise seri porttan menzil disi mesajinin
  //olcum sinilari icinde ise mesafe bilgisinin seria porttan gonderilmesi
  if (mesafe_cm > 200 || mesafe_cm < 2){
   Serial.println("Menzil Disi");
   }
   else {
      Serial.print(mesafe_cm);
      Serial.print("  cm");
      Serial.println();
   }
 
  //olculen mesafenin guvenli mesafe icinde olup olmaginin testi
  //olculen mesafeye ledlerinin durumunun degistirilmesi
  if (mesafe_cm > guvenlik_mesafesi)
  {
    digitalWrite(led_mesafe_guvenli, HIGH);
    digitalWrite(led_mesafe_guvensiz, LOW);
  }
  else
  {
    digitalWrite(led_mesafe_guvensiz, HIGH);
    digitalWrite(led_mesafe_guvenli, LOW);
  }
 
  delay(100);
}
