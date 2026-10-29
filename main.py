from fastapi import FastAPI 
app = FastAPI()
 
students ={
    1:{"name":"Ashish","course":"M.Tech","email":"ashi@xyz.com"},
    2:{"name":"Arush","course":"B.Tech","email":"arush@xyz.com"} ,
    3:{"name":"Aish","course":"B.Arch","email":"aish@xyz.com"},
    4:{"name":"Suman","course":"M.Sc","email":"suman@xyz.com"},
    5:{"name":"Subhashish","course":"M.Phill","email":"subhhi@xyz.com"}
}
@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/get-student/{student_id}")  
def get_student(student_id: int):
    student = students.get(student_id)
    #if student is None:
        #raise HTTPException(status_code=404, detail="Student Not Found")
    return student
 @app.post("/create-students")
def create_student(name:str,course:str,email:alnum):
   return{
        "name":name,
        "course": course,
        "email": email
   }
