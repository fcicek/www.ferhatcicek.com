
int led_sayisi = 6;
int led_pin[6] = {3, 5, 6, 9, 10, 11};
  
void setup() {
  Serial.begin(9600);
  //belirledigimiz tum pinleri cikis yapalim
  for (int i = 0; i < led_sayisi; i++) {
    pinMode(led_pin[i], OUTPUT);
  }
}
  
void loop() {
  animasyon_1();
}
  
void animasyon_1() {
//tüm ledleri sonuk olarak belirleyelim
  int led_durum[6] = {0, 0, 0, 0, 0, 0 };
  for (int j = 0; j < 2; j++) {
//tum ledlerin konumunu sırasyla degistirelim
//ilk dongude led sonuk durumdaysa yanacak
//dongu tekrar edersen yanik durumdaysa sonecek
    for (int i = 0; i < led_sayisi; i++) {
      led_durum[i] = ~led_durum[i];
      digitalWrite(led_pin[i], led_durum[i]);
      delay(150);
    }
  }
}
