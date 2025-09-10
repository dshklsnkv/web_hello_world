from sqlalchemy import Column, Integer, String, ForeignKey
from web.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(Integer, nullable=False)  # в часах
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # teacher_id: Mapped[int] = mapped_column(foreign_key="users.id")
    
    teacher = relationship("UserModel", backref="courses")