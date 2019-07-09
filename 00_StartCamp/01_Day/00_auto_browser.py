import webbrowser

menus = ['개성왕만둣국','알리오올리오','해물순두부찌개']

for menu in menus :
    print
    webbrowser.open(f'https://search.naver.com/search.naver?query={menu}')