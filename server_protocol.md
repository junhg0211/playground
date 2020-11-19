# Server Protocol

* W* 클라이언트가 메시지를 보내면 같은 월드에 있는 모든 플레이어의 클라이언트가 이 메시지를 받습니다.

* 버퍼사이즈 형태 : 정보의 크기가 아주 큰 경우, 정보의 길이를 먼저 보내고
  클라이언트에서 받은 정보의 양이 정보의 길이와 같아질때까지 정보를 받는 정보의 형태입니다.
  playground의 프로토콜에서는 정보의 길이와 정보를 `\n`으로 구분하여 전송합니다.

## Permission

* `OP <NICKNAME>`

`<NICKNAME>`에게 관리자 권한을 부여합니다.

* `DEOP <NICKNAME>`

`<NICKNAME>`에게서 관리자 권한을 제거합니다.

## General

* `CHAT <NICKNAME> <CONTENT>`

W*
`<NICKNAME>`이 `<CONTENT>`라고 말합니다.

* `ANNOUNCE <WORLD|ALL> <CONTENT>`

`<WORLD|ALL>`에 `<CONTENT>`를 공지합니다.

## World

* `WORLD <NICKNAME> <DESTINATION> [PASSWORD]`

`<NICKNAME>`을 `<DESTINATION>` 월드로 이동시킵니다.
만약 비밀번호가 있다면 `[PASSWORD]`를 비밀번호로 사용합니다.

* `WORLDLIST [NUMBER]`

가장 최근에 생성된 최대 `[NUMBER]`개의 서버 이름을 확인합니다.
만약 `[NUMBER]`가 없다면 모든 이름을 전송합니다.
전송의 형태는 버퍼사이즈입니다.

* `WORLDINFO <WORLD>`

`<WORLD>`의 정보를 확인합니다.
`<WORLD>`의 이름, 주인, 접속중인 사람의 수가 `\t`로 구분되어 전달됩니다.

## Moving and Animation

* `MOVE <NICKNAME> <POSITION_X> <POSITION_Y>`

W*
`<NICKNAME>`을 `<POSITION_X>`, `<POSITION_Y>`로 이동시킵니다.
움직임을 보인 플레이어도 이 메시지를 통해 움직임을 적용합니다.

* `EMOTION <NICKNAME> <EMOTION>`

W*
`<NICKNAME>`이 `<EMOTION>` 의사표현을 보입니다.