# Commands

* P* 관리자 권한이 필요합니다.

## FORMS

* `<NICKNAME>` : 사람의 이름입니다. `,`를 통해 두 명 이상의 사람을 한 번에 표현할 수 있습니다.
  * 만약 완벽한 이름이 아니더라도 한 명의 사람을 특정할 수 있는 경우 사용이 가능합니다.
    예를 들어, 월드에 `Sch_0q0`와 `zer0ken`, `Allen_Chii`가 들어와있을 때, `z`는 `zer0ken`을 뜻합니다.
    또한 `s,a`는 `Sch_0q0`과 `Allen_Chii`를 동시에 가리킵니다.
* `<DESTINATION>` : `<X> <Y>`형태를 가지는 월드의 특정한 점의 좌표값입니다.
* `< ___ >` : 불특정한 개수의 띄어쓰기를 포함할 수 있는 값입니다. 이 값 뒤에는 다른 값이 오지 않습니다.

## Interaction

* `W <NICKNAME> < CONTENT >` : `<NICKNAME>`에게 `< CONTENT >`를 귓속말합니다.

## Moving

* P* `TP`
  * `<NICKNAME>` : `<NICKNAME>`에게 순간이동합니다.
  * `<NICKNAME1> <NICKNAME2>` : `<NICKNAME1>`을 `<NICKNAME2>`에게 순간이동 시킵니다.
  * `<DESTINATION>` : `<DESTINATION>`로 순간이동합니다.
  * `<NICKNAME> <DESTINATION>` : `<NICKNAME>`을 `<DESTINATION>`으로 순간이동 시킵니다.
* P* `WORLD <WORLD> [PASSWORD]` : `[PASSWORD]`로 `<WORLD>`에 접속합니다.