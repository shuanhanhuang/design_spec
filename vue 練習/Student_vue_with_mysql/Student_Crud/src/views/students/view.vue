
import { RouterLink } from 'vue-router';
<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-header">
        <h4>
          Students
          <RouterLink to="/students/create" class="btn btn-primary float-end">
            Add student
          </RouterLink>
        </h4>
      </div>
      <div class="card-body">
        <table class="table table-bordered">
          <thead>
            <tr>
              <td>學號</td>
              <td>姓名</td>
              <td>性別</td>
              <td>生日</td>
              <td>成績</td>
            </tr>
          </thead>
          <tbody v-if="students.length > 0">
            <tr v-for="(student,index) in students" :key="index">
              <td>{{ student.s_id }}</td>
              <td>{{ student.s_name }}</td>
              <td>{{ student.s_sex }}</td>
              <td>{{ formatDate(student.s_birthday)}}</td>
              <td>{{ student.s_score }}</td>
              <td>
                <RouterLink :to="{path: '/students/'+student.id+'/edit'}" class="btn btn-success mx-2">Edit</RouterLink>
                <button type="button" class="btn btn-danger mx-2" @click="deleteStudent(student.id)">Delete</button>
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td colspan="6">loading...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    name:"student",
    data(){
      return{
        students:[]
      }
    },
    mounted(){
      // console.log("i am here")
      this.getStudents()
    },
    methods:{
      getStudents(){
        axios.get('http://localhost:8080/students').then(res => {
          this.students = res.data
          console.log(res.data)
        })
      },
      formatDate(date) {
        // padStart(2, '0') 的作用是保證日期中的日（Day）部分具有兩個數字的長度。
        // 如果日期的日部分是單個數字（例如，5），padStart 將在數字前面添加一個零，變成了那些數（05）。
        if (date) {
          const formattedDate = new Date(date);
          const year = formattedDate.getFullYear();
          const month = (formattedDate.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始
          const day = formattedDate.getDate().toString().padStart(2, '0');
          return `${year}年${month}月${day}日`;
        }
        return '';
      },
      deleteStudent(studentId){
        if(confirm("確定要刪除這筆資料嗎?")){
          // console.log(studentId)
          axios.delete(`http://localhost:8080/students/${studentId}`)
          .then(res => {
            alert("成功刪除資料")
            this.getStudents()
          })
        }
        
      }
    }
  }

</script>