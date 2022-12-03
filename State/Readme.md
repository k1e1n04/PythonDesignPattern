# State
Stateパターンは振る舞いに関するデザインパターンの一種。オブジェクトの状態を表現するために用いられる。

## クラス図
PlantUMLを使用して記載しています。
``` plantuml
@startuml
class State {
    + handle()
}
class Context {
    + handle()
}
class DockerStateA {
    + handle()
}
class DockerStateB {
    + handle()
}

State <|-- DockerStateA
State <|-- DockerStateB
Context o-- State
@enduml
```

## クラス説明
### State
Stateは、状態を表すためのものです。状態ごとに異なる振る舞いをするインタフェースを定めます。

### DockerState
DockerState役は、具体的な個々の状態を表現するものです。
State役で定められたインタフェースを具体的に実装します。

### Context
Context役は、現在の状態を表すConcreteState役のオブジェクトを保持します。状態、前後関係、文脈の役を行います。
Contextである管理センターに振る舞いを記述し，「起動中」だったらこうで，「停止中」だったらこうで...と条件を分岐させて複雑なコードを書かなくても，DockerStateに動作を記述してContextで保持しておけば，管理も保守も簡単になります。

## サンプルプログラム
サンプルではDockerを動かした時の動作を確認してみる。
- Dockerを起動すると、動作状態は、"running"になる
- Dockerを停止すると、動作状態が、"exited"になる
- Dockerを再起動すると、動作状態が、"running"になる