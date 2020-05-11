#include <Stepper.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27,20,4); 
Stepper myStepper(2050, 8,10,9,11);

void moveMotor(float direcao){
myStepper.step(direcao);   
}

void setVelMotor(int vel){
  myStepper.setSpeed(vel);
}

float convertGraus(float graus){
  return (graus*2050)/360;
}



String leStringSerial(){
  String conteudo = "";
  char caractere;
  
  // Enquanto receber algo pela serial
  while(Serial.available() > 0) {
    // Lê byte da serial
    caractere = Serial.read();
    // Ignora caractere de quebra de linha
    if (caractere != '\n'){
      // Concatena valores
      conteudo.concat(caractere);
    }
    // Aguarda buffer serial ler próximo caractere
    delay(10);
  }
  return conteudo;
}
void setup()
{
  lcd.init();
  lcd.backlight();
  myStepper.setSpeed(5);  //Determina a velocidade inicial do motor
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0){
  lcd.clear();
  String leitura = leStringSerial();
  
  if(leitura.indexOf("move:") != -1){
    lcd.clear();
    lcd.print(leitura);
    leitura.replace("move:","");
    if (! (convertGraus(leitura.toInt()) == 0)){
    lcd.print(leitura);
    moveMotor(convertGraus(leitura.toInt()));
    delay(1);
    }
  }
  if(leitura.indexOf("velMotor:") != -1){
    leitura.replace("velMotor:","");
    setVelMotor(leitura.toInt());
  }
  }
  delay(20);
}
