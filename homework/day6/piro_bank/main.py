from account import *

print("### SC 은행 고객 관리 시스템 ###")
print("")

customer_list = []

while True:
    print("=========================")
    print("원하시는 서비스를 선택해주세요.")
    print("1. 계좌 생성")
    print("2. 계좌 조회 및 입출금")
    print("3. VIP 조회")
    print("4. 총 계좌 수 조회")
    print("0. 프로그램 종료")
    print("")
    option = input("")
    
    if option == '0':
        break
    
    elif option == '1':
        print("---------- 계좌 생성 ----------")
        name = input("계좌명을 입력해 주세요: ")
        if name == '0':
            break
        money = int(input("첫 입금 금액을 입력해 주세요: "))
        customer = Account(name, money)
        customer_list.append(customer)
        print("계좌 생성 완료")
        print("")
        
    elif option == '2':
        print("---------- 계좌 조회 및 입출금 ----------")
        option_2_name = input("본인 계좌명을 입력해주세요: ")
        check = False
        for c in customer_list:
            if c.account_holder == option_2_name:
                check = True
                print("")
                print("서비스를 선택해주세요.")
                print("1. 조회\n2. 입금\n3. 출금\n0. 뒤로가기")
                option_2_option = input("")
                if option_2_option == '0':
                    break
                elif option_2_option == '1':
                    c.display_info()
                    print("------------- 입금 내역 ------------")
                    c.deposit_history()
                    print("------------- 출금 내역 ------------")
                    c.withdraw_history()
                    print("조회 완료")
                    print("")
                elif option_2_option == '2':
                    input_deposit = int(input("입금하시려는 금액을 입력해주세요 (단위: 원): "))
                    c.deposit(input_deposit)
                    print("")
                elif option_2_option == '3':
                    input_withdraw = int(input("출금하시려는 금액을 입력해주세요 (단위: 원): "))
                    c.withdraw(input_withdraw)
                    print("")
            else:
                continue

        if check == False:
            print("일치하는 계좌명이 없습니다.")
            print("")
                        
    elif option == '3':
        print("---------- VIP 조회 ----------")
        for c in customer_list:
            if c.balance >= 1000000:
                c.display_info()
                print("-------------------------")
        print("명단 끝")
        print("")

    elif option == '4':
        print("---------- 총 계좌 수 조회 ----------")
        Account.get_account_num()
        print("조회 끝")
        print("")
        
print("------------ 프로그램 종료 -------------")
print("이용해 주셔서 감사합니다.")
_ = input("엔터키를 눌러 종료")






