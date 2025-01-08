# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기전 전까지 계속해서 노출되도록 만들어주세요
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요

balance = 3000  #현재 잔액을 보여주세요
receipts = [] #[]대괄호:list / {key:value}중괄호:dict / (): tuple

while True:
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break

    elif num == '1':
        deposit_amount = int(input("입금 금액을 입력하세요.: ")) #input()=내장함수 / int()=정수형 데이터로 형변환 해주는 내장함수
        balance += deposit_amount #할당연산자 balance = balance + deposit_amount
        receipts.append(("입금", deposit_amount, balance)) #.append : 리스트에 요소 집어넣기
        print(f"입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")

    elif num == '2':
        withdraw_amount = int(input("출금 금액을 입력하세요.: ")) #input()=내장함수 / int()=정수형 데이터로 형변환 해주는 내장함수
        if withdraw_amount > 0: #출금 금액이 0보다 많을때
                if withdraw_amount <= balance: #출금 금액이 잔액보다 같거나 적을경우
                    balance -= withdraw_amount #잔액-출금액
                    receipts.append(("출금", withdraw_amount, balance)) #.append : 리스트에 요소 집어넣기
                    print(f"출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")
                else: #출금액이 잔액보다 같지 않거나 적지 않을경우
                    print(f"출금 잔액이 부족합니다. 현재 잔액: {balance}")

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")