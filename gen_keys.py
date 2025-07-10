from web3 import Web3
from eth_account.messages import encode_defunct
import eth_account
import os

def sign_message(challenge, filename="secret_key.txt"):
    """
    challenge - byte string
    filename - filename of the file that contains your account secret key
    To pass the tests, your signature must verify, and the account you use
    must have testnet funds on both the bsc and avalanche test networks.
    """
    # 读取私钥文件内容
    with open(filename, "r") as f:
        key = f.read().strip()  # 读取并去除首尾空白（比如换行符等）

    assert key, "Your account secret_key.txt is empty"  # 确保私钥内容非空

    w3 = Web3()
    message = encode_defunct(challenge)

    # 使用私钥创建账户对象并签名消息
    account = eth_account.Account.from_key(key)
    signed_message = account.sign_message(message)
    eth_addr = account.address

    # 验证签名是否正确（可选，这里主要是按作业逻辑做验证）
    recovered_addr = eth_account.Account.recover_message(message, signature=signed_message.signature.hex())
    assert recovered_addr == eth_addr, f"Failed to sign message properly"

    return signed_message, eth_addr


if __name__ == "__main__":
    for i in range(4):
        challenge = os.urandom(64)
        sig, addr = sign_message(challenge=challenge)
        print(addr)
