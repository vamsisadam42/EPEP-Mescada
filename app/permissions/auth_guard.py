from fastapi import Depends, HTTPException
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM

def require_role(role: str):
    def wrapper(token: str = Depends()):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_role = payload.get("role")
            if user_role != role:
                raise HTTPException(status_code=403, detail="Forbidden")
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")
    return wrapper
