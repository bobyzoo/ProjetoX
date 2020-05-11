#include <Stepper.h>
#include <Wire.h> //INCLUSÃO DE BIBLIOTECA
#include <LiquidCrystal_I2C.h> //INCLUSÃO DE BIBLIOTECA
//Inicializa a biblioteca utilizando as portas de 8 a 11 para
//ligacao ao motor
Stepper myStepper(2050, 8,10,9,11);

void moveMotor(float direcao){
myStepper.step(direcao);   
}
void setVelMotor(int vel){
  myStepper.setSpeed(vel);
  }
float convertGraus(float graus){
  Serial.println(graus*2050);
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

LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3, POSITIVE); 
void setup()
{

   lcd.begin (16,2); //SETA A QUANTIDADE DE COLUNAS(16) E O NÚMERO DE LINHAS(2) DO DISPLAY
 lcd.setBacklight(HIGH); //LIGA O BACKLIGHT (LUZ DE FUNDO)
 //Determina a velocidade inicial do motor
 myStepper.setSpeed(5);

 Serial.begin(9600);
}

void loop()
{
 
  if (Serial.available() > 0){
     String leitura = leStringSerial();
     if(leitura.indexOf("move:") != -1){
      Serial.println("-------");
      leitura.replace("move:","");
      Serial.println(leitura);
      moveMotor(convertGraus(leitura.toInt()));
      }
      
       if(leitura.indexOf("velMotor:") != -1){
      Serial.println("-------");
      leitura.replace("velMotor:","");
      Serial.println(leitura);
      setVelMotor(leitura.toInt());
      }
  }
 
}
