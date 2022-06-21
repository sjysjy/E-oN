# system.py
# 도서 추가, 검색, 수정, 삭제 함수



#도서 추가 함수
def add_Book():
    book=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "a", encoding='UTF8')
    add=input("추가할 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 띄어쓰기로 구분하여 입력하세요: ")
    book.write("\n")
    book.write(add)
    book.close()

    check=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
    print(check.read())
    check.close()
    


#도서 검색 함수
def search_Book():
     book=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
     search=input("검색할 단어를 입력하세요: ")
     lines=book.readlines()
     for l in lines:
         if l.find(search) > -1:
             print(l.strip("\n"))
         else:
             pass
     print("\n")
     book.close()
     


#도서 정보 수정 함수
def edit_Book():
     book=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
     lines=book.readlines()
     book_w=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "w", encoding='UTF8')
     title=input("수정할 도서의 제목을 입력하세요: ")
     edit=input(" 도서명, 저자, 출판연도, 출판사명, 장르를 띄어쓰기로 구분하여 수정사항을 입력하세요: ")
     
     for l in lines:
         if l.find(title) > -1:
             book_w.write(edit)
         else:
             book_w.write(l)
     book.close()
     book_w.close()

     check=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
     print(check.read())
     check.close()
    


#도서 삭제 함수
def remove_Book():
     book_r=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
     lines=book_r.readlines()
     print(lines)
     book_w=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "w", encoding='UTF8')
     title=input("삭제할 도서의 제목을 입력하세요: ")
     
     for l in lines:
         if l.find(title) == -1:
             book_w.write(l)

     book_r.close()
     book_w.close()
         

     check=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
     print(check.read())
     check.close()



#현재 도서 목록 출력 함수
def print_Book():
    book=open("C:/Users/송주연/AppData/Local/Programs/Python/Python38-32/Python source/E-oN 7th assignment/input.txt", "r", encoding='UTF8')
    print(book.read())
    book.close()



    
     

             

