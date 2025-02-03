from pydantic import BaseModel, field_validator


class StripStrBaseModel(BaseModel):
    @field_validator("*", mode="before")
    def strip_strings(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

