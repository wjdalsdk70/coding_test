def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, '-', '_', '.' 제외한 모든 문자 제거
    import re
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 4단계: 마침표(.)가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열이면 "a"를 대입
    if not new_id:
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 첫 15자만 남기고 나머지 문자 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')  # 마침표(.)가 끝에 위치하면 제거

    # 7단계: 길이가 2자 이하라면 마지막 문자를 반복해서 길이 3이 될 때까지 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
