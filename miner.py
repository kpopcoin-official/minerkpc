import requests
import json
import struct

# 1. 노드 RPC 접속 정보
RPC_URL = "http://127.0.0.1:8717"
RPC_USER = "admin"
RPC_PASS = "1234"

def rpc_call(method, params=[]):
    headers = {'content-type': 'application/json'}
    payload = json.dumps({"method": method, "params": params, "id": 1})
    response = requests.post(RPC_URL, auth=(RPC_USER, RPC_PASS), headers=headers, data=payload)
    return response.json()['result']

print("=== 파이썬 채굴기 가동 준비 ===")

# 2. 노드와 통신 테스트
info = rpc_call("getblockchaininfo")
print(f"현재 노드의 블록 높이: {info['blocks']}")
print(f"현재 해시 난이도: {info['difficulty']}")

# 3. 8바이트 논스 적용 예시 (파이썬의 마법)
nonce = 1234567890
# '<Q' 는 숫자를 8바이트(64비트) 리틀 엔디안으로 바꿔주는 마법의 포맷입니다.
nonce_bytes = struct.pack("<Q", nonce) 
print(f"8바이트 논스 변환 결과: {nonce_bytes.hex()}")

# (이후 이곳에 getblocktemplate를 받아와서 해시를 찾는 로직이 추가됩니다.)
