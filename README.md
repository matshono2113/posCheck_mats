# posCheck_mats
## 概要
学校などの施設における災害発生時の点呼・救助判断補助システム
BluetoothをONにした携帯を持っている登録者が、災害発生直前どこにいたか把握できるシステム

## 仕様機材
・Raspberry Pi 3 Model B+
・ES920LR, ES920EB

## scan.py
BDアドレススキャン

## lora.py
LoRaWNモジュール ES920LRを利用するための関数を宣言

## main.py
起動時ES920LRの設定
現在(19.8.21)scan.pyで取得したBDアドレスを標準出力

## 参考
ble通信 https://github.com/karulis/pybluez/tree/master/examples/ble
LoRa通信 https://github.com/AmbientDataInc/LoRa-rssi-measure
