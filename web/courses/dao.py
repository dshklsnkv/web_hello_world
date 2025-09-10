from web.dao.base import BaseDAO
from web.courses.models import CourseModel

class CoursesDAO(BaseDAO):
    model = CourseModel