# Abstract Factory
## 概要
どのオブジェクトを生成するかといった権限をサブクラスにサブクラスに委譲することにより、オブジェクト生成という変更が生じる部分を切り出し、オブジェクト間の関係を疎結合にすることにより、保守性を高めることができる。

## メリット
1. 実行するメインプログラムを修正することなく、サブクラス群を環境変化に伴って交換することができること
2. 新しいファクトリが増えた場合もオープン・クローズドの原則が守られている

## デメリット
1. 関連オブジェクトが増えた場合、修正箇所がすべてのFactoryクラスに及んでしまう点