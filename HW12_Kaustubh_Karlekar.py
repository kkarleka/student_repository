from flask import Flask, render_template
import sqlite3

app: Flask = Flask(__name__)
path = (r"C:\sqlite\StudentRepo.db")

@app.route('/')
def instructor_table_db():

    db = sqlite3.connect(path)
    query = """select a.Name, a.CWID, b.Course, b.Grade, c.Name  from students as a 
				                join grades as b on a.CWID = b.StudentCWID 
								join instructors as c on c.CWID = b.InstructorCWID 
								group by a.Name, a.CWID, b.Course, b.Grade
								order by a.Name"""
    res = db.execute(query)
    inst_list = []
    for row in res:
        inst_list.append({'name': row[0],'cwid': row[1],'course': row[2],'grade': row[3],'instructor': row[4]})
    db.close()
    return render_template('instructor.html', header = 'Instructor Repository', table_title = 'Instructor Details', data = inst_list)

    
app.run(debug=True)
    

    
    