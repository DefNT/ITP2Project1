class Course:
    def __init__(self, course_id, name, credits, description="",
                 prerequisites=None, max_capacity=30):
        self._course_id = course_id
        self._name = name
        self._description = description
        self._credits = credits
        self._prerequisites = prerequisites or []
        self._max_capacity = max_capacity
        self._enrolled_students = []

    @property
    def course_id(self):
        return self._course_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Course cannot be empty")
        self._name = value.strip()

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        if not isinstance(value, (int, float)) or (value <= 0):
            raise ValueError("Course credits must be positive number")
        self._credits = value

    @property
    def description(self):
        return self._description

    @property
    def prerequisites(self):
        return self._prerequisites.copy()

    @property
    def max_capacity(self):
        return self._max_capacity

    @property
    def enrolled_cnt(self):
        return len(self._enrolled_students)

    @property
    def is_full(self):
        return self.enrolled_cnt >= self._max_capacity

    def add_prerequisite(self, course_id):
        if course_id not in self._prerequisites:
            self._prerequisites.append(course_id)

    def remove_prerequisite(self, course_id):
        if course_id in self._prerequisites:
            self._prerequisites.remove(course_id)

    def enroll_student(self, student_id):
        if self.is_full:
            raise ValueError(f"Course {self._name} is full ({self._max_capacity} max)")
        if student_id not in self._enrolled_students:
            self._enrolled_students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self._enrolled_students:
            self._enrolled_students.remove(student_id)

    def display_info(self):
        prereq_str = ", ".join(self._prerequisites) if self._prerequisites else "None"
        return (
            f"[Course] {self._course_id}: {self._name} | "
            f"Credits: {self._credits} | Prereqs: {prereq_str} | "
            f"Enrolled: {self.enrolled_cnt}/{self._max_capacity}"
        )

    def to_dict(self):
        return {
            "course_id": self._course_id,
            "name": self._name,
            "credits": self._credits,
            "prerequisites": ";".join(self._prerequisites) if self._prerequisites else "",
            "max_capacity": self._max_capacity,
            "description": self._description,
        }

    @classmethod
    def from_dict(cls, data):
        prereqs = data.get("prerequisites", "")
        prereq_list = [p.strip() for p in prereqs.split(";") if p.strip()]
        return cls(
            course_id=data["course_id"],
            name=data["name"],
            credits=int(data.get("credits", 3)),
            description=data.get("description", ""),
            prerequisites=prereq_list,
            max_capacity=int(data.get("max_capacity", 30)),
        )
    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return f"Course(id='{self._course_id}', name='{self._name}', credits={self._credits})"