from fastapi import HTTPException, status

class BaseException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserExistException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "пользователь уже зарегистрирован"
    
class IncorrectEmailPassword(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "некоректный email или пароль"
    
class TokenMissing(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "токен отстутсвует"
    
class TokenIncorrect(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "неверный формат токена"
    
class UserNotPresent(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "пользователь не найден"
    
class CourseNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "курс не найден"