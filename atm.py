# 입력 검증 및 에러 처리 추가
# 잘못된 입력 값(-금액, 문자 입력 등)을 처리하도록 기능을 추가해주세요.
# 유효하지 않은 메뉴 선택시 경고 메세지 또는 사용 방법을 재안내 해주세요.
# gitmoji = fix a bug (벌레)

balance = 3000  #현재 잔액을 보여주세요
receipts = [] #[]대괄호:list / {key:value}중괄호:dict / (): tuple

while True:
    while True:
        num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료): ")
        
        # 메뉴 숫자 입력 안내
        if not num.isdigit() or int(num) not in [1, 2, 3, 4]:
            print("숫자만 입력해주세요. (예: 1)")
            continue  # 잘못된 입력 -> 다시 메뉴 선택으로 돌아감
        
        break  # 올바른 입력 -> 메뉴 선택 종료

    if num == '4':  # 종료
        break

    elif num == '1':  # 입금
        while True:
            deposit_input = input("입금 금액을 입력하세요: ")
            
            # 입금 입력값 체크
            if not deposit_input.isdigit() or "-" in deposit_input:
                print("숫자만 입력해주세요. (예: 1000)")
                continue  # 잘못된 입력 -> 다시 입금 금액 입력으로 돌아감

            deposit_amount = int(deposit_input)
            break  # 올바른 입력 -> 입금 처리 진행

        balance += deposit_amount  # 잔액에 입금 금액 추가
        receipts.append(("입금", deposit_amount, balance))  # 영수증에 추가
        print(f"입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")

    elif num == '2':  # 출금
        while True:
            withdraw_input = input("출금 금액을 입력하세요: ")
            
            # 출금 입력값 체크
            if not withdraw_input.isdigit() or "-" in withdraw_input:
                print("숫자만 입력해주세요. (예: 1000)")
                continue  # 잘못된 입력 -> 다시 출금 금액 입력으로 돌아감

            withdraw_amount = int(withdraw_input)
            break  # 올바른 입력 -> 출금 처리 진행

        if withdraw_amount > 0:  # 출금 금액이 0보다 큰 경우
            if withdraw_amount <= balance:  # 출금 금액이 잔액보다 같거나 적을 경우
                balance -= withdraw_amount  # 잔액에서 출금 금액 차감
                receipts.append(("출금", withdraw_amount, balance))  # 영수증에 추가
                print(f"출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")
            else:  # 출금 금액이 잔액보다 클 경우
                print(f"출금 잔액이 부족합니다. 현재 잔액: {balance}")
        else:
            print("출금 금액을 올바르게 작성해주세요.")

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")