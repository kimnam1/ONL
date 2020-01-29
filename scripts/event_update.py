import wikipediaapi

from date.models import Onl

wiki = wikipediaapi.Wikipedia('ko') # 한국 위키피디아 사이트로 접속 세팅




month = list(range(1, 13))
date = list(range(1, 32))
for mon in month:
    print(str(mon) + "월 입니다.")
    if mon in [4, 6, 9, 11]:
        for d in date:
            if d == 30:
                print(str(mon) + "/" + str(d))
                page_wiki = wiki.page(f'위키백과:오늘의 역사/{mon}월 {d}일')
                if page_wiki.exists():
                    print(f'{mon}월 {d}일 wiki에 존재!')
                    print(page_wiki.text)
                    print()
                    print()
                    print()
                    print()
                    Onl(month=mon, date=d, slug=f'{mon}-{d}', events=page_wiki.text).save()
                if page_wiki.exists() == False:
                    print(f'{mon}월 {d}일 wiki에 존재 안함!!!!!!!!!!!!!!!!!!!!!')
                print('30일까지인 달입니다.')
                break
            else:
                print(str(mon) + "/" + str(d))
                page_wiki = wiki.page(f'위키백과:오늘의 역사/{mon}월 {d}일')
                if page_wiki.exists():
                    print(f'{mon}월 {d}일 wiki에 존재!')
                    print(page_wiki.text)
                    print()
                    print()
                    print()
                    print()
                    Onl(month=mon, date=d, slug=f'{mon}-{d}', events=page_wiki.text).save()
                if page_wiki.exists() == False:
                    print(f'{mon}월 {d}일 wiki에 존재 안함!!!!!!!!!!!!!!!!!!!!!')
    if mon == 2:
        for d in date:
            if d == 29:
                print(str(mon) + "/" + str(d))
                page_wiki = wiki.page(f'위키백과:오늘의 역사/{mon}월 {d}일')
                if page_wiki.exists():
                    print(f'{mon}월 {d}일 wiki에 존재!')
                    print(page_wiki.text)
                    print()
                    print()
                    print()
                    print()
                    Onl(month=mon, date=d, slug=f'{mon}-{d}', events=page_wiki.text).save()
                if page_wiki.exists() == False:
                    print(f'{mon}월 {d}일 wiki에 존재 안함!!!!!!!!!!!!!!!!!!!!!')
                break
            else:
                print(str(mon) + "/" + str(d))
                page_wiki = wiki.page(f'위키백과:오늘의 역사/{mon}월 {d}일')
                if page_wiki.exists():
                    print(f'{mon}월 {d}일 wiki에 존재!')
                    print(page_wiki.text)
                    print()
                    print()
                    print()
                    print()
                    Onl(month=mon, date=d, slug=f'{mon}-{d}', events=page_wiki.text).save()
                if page_wiki.exists() == False:
                    print(f'{mon}월 {d}일 wiki에 존재 안함!!!!!!!!!!!!!!!!!!!!!')
    elif mon in [1, 3, 5, 7, 8, 10, 12]:
        for d in date:
            print(str(mon) + "/" + str(d))
            page_wiki = wiki.page(f'위키백과:오늘의 역사/{mon}월 {d}일')
            if page_wiki.exists():
                print(f'{mon}월 {d}일 wiki에 존재!')
                print(page_wiki.text)
                print()
                print()
                print()
                print()
                Onl(month=mon, date=d, slug=f'{mon}-{d}', events=page_wiki.text).save()
            if page_wiki.exists() == False:
                print(f'{mon}월 {d}일 wiki에 존재 안함!!!!!!!!!!!!!!!!!!!!!')
            if d == 31:
                print("31일까지인 달입니다.")




