int Vin;  // Arduino A0 pinin kullanilacak degisken
float Sicaklik; // Sicakik degeri float olarak belirlenir

// include the library code:
#include <LiquidCrystal.h>

// LiquidCrystal kutuphanesi ile  lcd icin kullanacagimiz pinleri set edelim.
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // lcd nin satir ve sutun bilgisi
  lcd.begin(16, 2);
  // lcd nin 1. satirina ait bilgi mesaji
  lcd.print("Sicaklik: ");
}

void loop() {
  Vin = analogRead(0);    // A0 pin değerinin okunması
  Sicaklik = (500.0 * Vin)/1023; // A0 pininden okunan degerin sicaklik degerine cevrilmesi
  // set the cursor to column 3, line 1
  lcd.setCursor(3, 1);
   // Sicaklik degerini yazirma
   lcd.print("derece "); 
  lcd.print(Sicaklik); 
       
}
