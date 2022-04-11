from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from config import SECRET_KEY, ALGORITHM
from middlewares import generate_session
from schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_router = APIRouter()


# def get_current_user(session: Session = Depends(generate_session),
#                      token: str = Depends(oauth2_scheme)):
#     credetials_exception = HTTPException(
#         status_code=HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         uid: int = payload.get('id')
#         if uid is None:
#             raise credetials_exception
#         token_data = TokenData(id=uid)
#     except JWTError:
#         raise credetials_exception
#
#     user = get_user_by_id(uid=token_data.id, session=session)
#     if user is None:
#         raise credetials_exception
#     return user
#
#
# @auth_router.post('/token', response_model=Token)
# def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(),
#                     session: Session = Depends(get_session)):
#     user = authenticate_user(session=session, username=form_data.username,
#                              password=form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(user.id)
#     return Token(access_token=access_token, token_type='bearer')
#
#
# @auth_router.get('/user/me', response_model=UserGetModel)
# def read_user_me(current_user: User = Depends(get_current_user)):
#     return current_user