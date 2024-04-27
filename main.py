from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("Udayan Higher Secondary School", "Dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
kashem = Student("Kashem", nine)
raisa = Student("Raisa", ten)
sumona = Student("Sumona", ten)

school.student_admission(rahim)
school.student_admission(kashem)
school.student_admission(raisa)
school.student_admission(sumona)

rahman = Teacher("Rahman Khan")
kuddus = Teacher("Kuddus Khan")
abul = Teacher("Abul Khan")
toriqul = Teacher("Toriqul Khan")

bangla = Subject("Bangla", rahman)
physics = Subject("Physics", kuddus)
chemistry = Subject("Chemistry", abul)
biology = Subject("Biology", toriqul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)