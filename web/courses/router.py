from fastapi import APIRouter, status
from typing import Sequence
from web.courses.schema import CourseBase, CourseCreate
from web.courses.dao import CoursesDAO
from web.exceptions import CourseNotFoundException

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("", status_code=201)
async def create_course(course_data: CourseCreate):
    await CoursesDAO.add(name = course_data.name,
                       description = course_data.description, 
                       duration = course_data.duration, 
                       teacher_id = course_data.teacher_id
                       )
    print(f"пользователь сохранен в бд:{course_data}")

@router.get("")
async def get_all_courses() -> Sequence[CourseBase]:
    return await CoursesDAO.find_all()

@router.get("/{id}")
async def get_course(id: int) -> CourseBase:
    course = await CoursesDAO.find_by_id(id)
    if not course:
        raise CourseNotFoundException
    return course

@router.delete("/{id}")
async def delete_course(id: int) -> dict:
    await CoursesDAO.delete(id)
    return {"status": "ok"}
