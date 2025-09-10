from pydantic import BaseModel
from typing import Optional
    
class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    duration: int
    teacher_id: int
    
class CourseBase(CourseCreate):
    id: int