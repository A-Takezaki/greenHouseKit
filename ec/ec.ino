/*
 このプログラミングコードはGNU General Public Licenseに則り、Michael Ratcliffe氏が作製したもの（参考文献１）を基に改変・加筆しました。 
*/
//必要なライブラリをincludeする
#include <OneWire.h>
#include <DallasTemperature.h>

//変数の定義
int R1= 1000;//電極に使用するプルダウン抵抗の値。手元に1000Ωの抵抗がない場合は適宜変更。ただし、300Ω以上にしないといけない。
int Ra=25; //Arduino側にある抵抗の値。これを変える必要はない。
int ECPin= A0;
int ECGround=A1;
int ECPower =A4;

float PPMconversion=0.7;//PPM値を算出するのに必要定数
float TemperatureCoef = 0.019; //今回のコードでは温度較正を線形の関数を用いて行う。その際に使用する1次関数の傾きの値。液肥を測る分には変更する必要はないと思われる。
float K=2.8;//電極の大きさに依存する値。もし、日本の家庭用コンセント以外の電極（例えば自分で切り出したアルミ板等）を使用する場合は、計算しなおして下さい。詳しい算出方法は他の記事参照。


//温度センサの通信設定
const int TempProbePossitive =8;  //温度計の電源線の指定
const int TempProbeNegative=9;    //温度計のGND線の指定

#define ONE_WIRE_BUS 10 //DS18B20の黄色の線が刺さるピン


//各種ライブラリの設定 
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


//初期化
float Temperature=10;
float EC=0;
float EC25 =0;
int ppm =0;
float raw= 0;
float Vin= 5;
float Vdrop= 0;
float Rc= 0;
float buffer=0;

//起動時に一回行うセットアップ過程
void setup()
{
  Serial.begin(9600);
  pinMode(TempProbeNegative , OUTPUT ); 
  digitalWrite(TempProbeNegative , LOW );
  pinMode(TempProbePossitive , OUTPUT );
  digitalWrite(TempProbePossitive , HIGH );
  pinMode(ECPin,INPUT);
  pinMode(ECPower,OUTPUT);
  pinMode(ECGround,OUTPUT);
  digitalWrite(ECGround,LOW);

  delay(100);// センサの設定のための待機時間
  sensors.begin();
  delay(100);
}

//くり返し処理の過程
void loop()
{
    if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'r') {
      int ecValue =  GetEC();
      Serial.println(ecValue);
    }
    
    if (command == 't') {
      // digitalWrite(ledPin, HIGH);
      // delay(5000);
      // digitalWrite(ledPin, LOW);
      Serial.println(1000);
    }
  }
// GetEC();
// PrintReadings();  
// delay(5000); 
}


// テスト開発時のコード
//メインループからの呼び出し
int GetEC(){
sensors.requestTemperatures();// Send the command to get temperatures
Temperature=sensors.getTempCByIndex(0); //Stores Value in Variable
//液体の抵抗の推定
digitalWrite(ECPower,HIGH);
raw= analogRead(ECPin);
raw= analogRead(ECPin);// This is not a mistake, First reading will be low beause if charged a capacitor
digitalWrite(ECPower,LOW);
//ECに変換
Vdrop= (Vin*raw)/1024.0;
Rc=(Vdrop*R1)/(Vin-Vdrop);
Rc=Rc-Ra; 
EC = 1000/(Rc*K);
//温度較正
EC25  =  EC/ (1+ TemperatureCoef*(Temperature-25.0));
ppm=(EC25)*(PPMconversion*1000);
return EC25
;}

//外部への書き出し
void PrintReadings(){
Serial.print(EC25);
Serial.print(",");
Serial.print(ppm);
Serial.print(",");
Serial.println(Temperature);
};
