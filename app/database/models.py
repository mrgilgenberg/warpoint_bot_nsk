from pydantic import BaseModel
from uuid import UUID
from datetime import date


class UserRow(BaseModel):
    uu_user_id: UUID
    n_telegram_id: int
    vc_full_name: str | None = None
    d_birthday: date | None = None
    vc_phone: str | None = None
    b_blocked: bool
    uu_presenter_id: UUID


class PresenterRow(BaseModel):
    uu_presenter_id: UUID
    n_presenter_id: int