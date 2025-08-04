requests = ['get', 'post', 'put']

# 조건에 따라 다르게 처리
for request in requests:
    if request == 'get':
        print("you can't get this")
    else:
        print(f"this is your request: {request}")

# 빈 리스트 확인 - if 에 리스트 이름 사용 시 True, False 로 빈 리스트 여부 확인
error_requests = []
if error_requests:
    for request in error_requests:
        print(request)
else:
    print('empty list')

# 여러 개 리스트 다루기
clients = ['get', 'post', 'put']
servers = ['get', 'delete']

for client in clients:
    if client in servers:
        print(client)
    else:
        print(f"You can't do {client}")