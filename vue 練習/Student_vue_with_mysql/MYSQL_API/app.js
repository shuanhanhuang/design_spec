import express from 'express'
import {getStudents, getStudent, createStudent, EditStudent, deleteStudent} from './database.js'
import cors from 'cors';

const app = express()
app.use(cors({
    origin: 'http://localhost:5173', // 允许的域名
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE', // 允许的HTTP方法
    optionsSuccessStatus: 204, // 预检请求的成功状态码
  }))
// 先檢查是否包含 JSON 資料
// 如果request body 包含 JSON 資料，它會分析 JSON 資料並轉換為 JavaScript 物件。
// 將分析後的物件附加到 (req) 上，以便後續的路由處理可以使用它来處理請求
app.use(express.json())

app.get('/students',async (req, res)=>{
    const students = await getStudents()
    res.send(students)
})

app.get('/students/:id',async (req, res)=>{
    const id = req.params.id
    const student = await getStudent(id)
    res.send(student)
})

app.post('/students',async (req, res)=>{
    try{
        const {s_id, s_name, s_sex, s_birthday, s_score} = req.body
        const student = await createStudent(s_id, s_name, s_sex, s_birthday, s_score)
        res.status(201).send(student)
    }
    catch{
        res.status(422).send("所有資訊都要填寫")
    }
    
})

app.put('/students/:id',async (req, res)=>{
    const {id, s_id, s_name, s_sex, s_birthday, s_score} = req.body  
    const student = await EditStudent(id,s_id, s_name, s_sex, s_birthday, s_score)
    res.status(201).send(student)
})

app.delete('/students/:id',async (req, res)=>{
    const id = req.params.id
    console.log(req.params.id)
    const students = await deleteStudent(id)
    res.send(students)
})

app.use((err, req, res, next) => {
    console.error(err.stack)
    res.status(500).send('Something broke!')
})

app.listen(8080, ()=>{
    console.log('server is running in 8080')
})
