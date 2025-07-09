from web3 import Web3
from eth_account.messages import encode_defunct
import eth_account
import os

def sign_message(challenge, filename="secret_key.txt"):
    """
    用私钥对挑战签名，返回签名结果和账户地址
    """
    # 读取私钥（自动处理空白/空行）
    with open(filename, "r") as f:
        private_key = f.read().strip()  # 直接读取并去除所有空白
    assert private_key, "私钥文件为空或仅含空白字符"  # 确保有有效私钥

    # 初始化 Web3（如需连测试网节点可在此指定）
    w3 = Web3()
    message = encode_defunct(challenge)  # 编码挑战消息

    # 用私钥创建账户并签名
    account = w3.eth.account.from_key(private_key)
    signed_message = account.sign_message(message)

    # 验证签名（可选，确保逻辑正确）
    recovered_addr = eth_account.Account.recover_message(
        message, 
        signature=signed_message.signature.hex()
    )
    assert recovered_addr == account.address, "签名与地址不匹配！"

    return signed_message, account.address


if __name__ == "__main__":
    for _ in range(4):
        challenge = os.urandom(64)
        sig, addr = sign_message(challenge)
        print(f"账户地址: {addr}")
        # 可选：打印签名（调试用）
<<<<<<< HEAD
        # print(f"签名: {sig.signature.hex()}")
=======
        # print(f"签名: {sig.signature.hex()}")
>>>>>>> e12bbb7dbcc713f248e7003d47d86fc66d297306
