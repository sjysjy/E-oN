#main.py

import system

def main():
    print("도서 관리 프로그램")
    print("1. 도서 추가")
    print("2. 도서 검색")
    print("3. 도서 정보 수정")
    print("4. 도서 삭제")
    print("5. 도서 목록 출력")
    print("6. 종료")

    number=input("번호 입력: ")
    print("\n")
    return number

while True:
    num=main()

    if num == "1":
        system.add_Book()
    elif num == "2":
        system.search_Book()
    elif num == "3":
        system.edit_Book()
    elif num == "4":
        system.remove_Book()
    elif num == "5":
        system.print_Book()
    elif num == "6":
        print("도서 관리 프로그램을 종료합니다!")
        break
    

    
    

    
    
    
