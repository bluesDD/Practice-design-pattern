デザインパターンの練習帳。

## Iterator pattern

Iteratorは反復、繰り返すという意味。
集約したオブジェクトを列挙する手段を提供するデザインパターン。

下記の場合に使う。
- アプリケーション固有なデータ、構造を持ったオブジェクトにアクセスをする場合
- 配列やコレクションなどの集合する要素にアクセスする場合(配列はforループで回せるが、リストなどのコレクションは難しかったりする)
- 集合の要素に順次にアクセスする必要がある場合

[UML図](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Iterator_UML_class_diagram.svg)

### 構成要素

#### Aggregate 集合体クラス

数え上げるものの「集合体」を扱う。


## 参考

- デザインパターン「Iterator」 - Qiita
https://qiita.com/shoheiyokoyama/items/3f42d0057d9d5a861039

