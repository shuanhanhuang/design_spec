import mysql from 'mysql2'
import dotenv from 'dotenv'

dotenv.config()

const pool = mysql.createPool({
    host: process.env.MYSQL_HOST ,
    user: process.env.MYSQL_USER,
    password: process.env.MYSQL_PASSWORD,
    database: process.env.MYSQL_DATABASE

}).promise()

export async function getStudents(){
    // 取得 result 陣列第一個值
    const [result] = await pool.query('select * from student') 
    // 上述寫法等同下兩行程式碼 
    // const result = await pool.query('select * from student') 
    // const rows = result[0]
    return result
}

export async function getStudent(id){
    const [result] = await pool.query(` select * from student where id = ? `,[id]) 
    return result[0]
}

export async function createStudent(s_id, s_name, s_sex, s_birthday, s_score){
    console.log(s_id, s_name, s_sex, s_birthday, s_score)
    try{
        const [result] = await pool.query(`INSERT INTO Student (s_id, s_name, s_sex, s_birthday, s_score) values(?, ?, ?, ?, ?)`,[s_id, s_name, s_sex, s_birthday, s_score])
        console.log("hello:"+result)
        //可以 return result 看看 --> insertId 是 result 結構裡面的一個 key ，代表現在插入的資料的 id 是多少
        const id = result.insertId
        return getStudent(id)
    }
    catch(error){
        console.error("Error:", error);
        return error;
    }
 
}

export async function EditStudent(id, s_id, s_name, s_sex, s_birthday, s_score){
    const [result] = await pool.query(`UPDATE Student 
    SET s_id = ?, s_name = ?, s_sex = ?, s_birthday = ?, s_score = ? 
    WHERE id = ?
    `,[s_id, s_name, s_sex, s_birthday, s_score, id])
    return getStudent(id)
    
}

export async function deleteStudent(id){
    const [result] = await pool.query(`DELETE FROM Student WHERE id = ?`,[id])
    return getStudents()
}

// const students = await getStudents()
// console.log(students)
// const student = await getStudent(1)
// console.log(student)
// const student = await createStudent(111018031, '江城風', '男', '1999-11-04', 79.3)
// console.log(student)