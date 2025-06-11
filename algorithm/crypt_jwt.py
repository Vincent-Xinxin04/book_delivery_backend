import os
import time
import secrets
import bcrypt
import jwt
from datetime import datetime, timedelta
from typing import Tuple

# 密码加密函数 (使用 bcrypt)
def encrypt_password(password: str) -> Tuple[str, str]:
    """
    将明文密码加密为安全哈希值
    返回: (加密后的密码, 存储用的 salt)
    """
    # 生成随机的 salt (bcrypt 会自动处理 salt 存储)
    salt = bcrypt.gensalt(rounds=12)  # 适当增加计算成本
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8'), salt.decode('utf-8')

# 密码验证函数
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码是否匹配存储的哈希值
    """
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

# 生成 JWT 令牌函数
def generate_login_token(user_id: str, username: str, secret_key: str, expires_hours: int = 24) -> str:
    """
    生成安全的 JWT 登录令牌
    返回: 签名的 JWT 字符串
    """
    # 生成随机 JWT ID 防止重放攻击
    jti = secrets.token_hex(16)
    
    payload = {
        # 标准声明
        'sub': user_id,           # 主题 (用户ID)
        'iat': datetime.utcnow(), # 签发时间
        'exp': datetime.utcnow() + timedelta(hours=expires_hours),  # 过期时间
        'jti': jti,               # 唯一令牌ID
        
        # 自定义声明
        'user': username,
        'scope': 'access',        # 权限范围
        'iss': 'your-app-name'    # 签发者
    }
    
    # 使用 HS256 算法签名
    return jwt.encode(payload, secret_key, algorithm='HS256')

# 验证 JWT 令牌函数
def verify_login_token(token: str, secret_key: str) -> dict:
    """
    验证并解码 JWT 令牌
    返回: 解码后的 payload 字典
    抛出异常: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=['HS256'],
            options={'require': ['exp', 'iat', 'sub']}  # 要求必须包含的字段
        )
        return payload
    except jwt.PyJWTError as e:
        # 在实际应用中应记录日志
        raise ValueError(f"无效的令牌: {str(e)}")