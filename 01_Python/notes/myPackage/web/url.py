def my_url(itemPerPage=10, **args):
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    a = args.get('key')
    b = args.get('targetDt')
    if bool(a) != True or bool(b) != True:
        return '필수 요청변수가 누락되었습니다.'
    if itemPerPage < 1 or itemPerPage > 10:
        return '1~10까지의 값을 넣어주세요.'
    return (f'{url}itemPerPage={itemPerPage}&key={a}&targetDt={b}')
