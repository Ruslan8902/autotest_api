from pydantic import BaseModel, EmailStr, Field, UUID4, StringConstraints, ValidationError
from typing import Annotated


class ShortUserSchema(BaseModel):
    """
    Описание базовой структуры пользователя.
    """
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class UserSchema(ShortUserSchema):
    """
    Описание структуры пользователя с полем id.
    """
    id: UUID4


# constr function is discouraged in favor of using Annotated with StringConstraints instead.
# constr function will be deprecated in Pydantic 3.0.
class CreateUserRequestSchema(ShortUserSchema):
    """
    Описание структуры запроса на создание пользователя.
    """
    password: Annotated[
        str,
        StringConstraints(pattern=r'^\w{8,25}$')
    ]


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
