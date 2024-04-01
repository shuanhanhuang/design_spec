<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                <h4>Edit student</h4>
            </div>
            <div class="card-body">
                <div class="alert alert-warning" v-if=" model2.student.s_id == '' || model2.student.s_name == ''
                || model2.student.s_sex == '' || model2.student.s_birthday == '' || model2.student.s_score == '' ">
                    <p v-if=" model.student.s_id == '' ">
                        ※ {{ warning_id }}
                    </p>
                    <p v-if=" model.student.s_name == '' ">
                        ※ {{ warning_name }}
                    </p>
                    <p v-if=" model.student.s_sex == '' ">
                        ※ {{ warning_sex }}
                    </p>
                    <p v-if=" model.student.s_birthday == '' ">
                        ※ {{ warning_birthday }}
                    </p>
                    <span v-if=" model.student.s_score == '' ">
                        ※ {{ warning_score }}
                    </span>
                </div>
                <div class="mb-3">
                    <input type="hidden" v-model="model2.student.id" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">學號</label>
                    <input type="text" v-model="model2.student.s_id" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">姓名</label>
                    <input type="text" v-model="model2.student.s_name" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">性別</label>
                    <input type="text" v-model="model2.student.s_sex" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">生日</label>
                    <input type="text" v-model="model2.student.s_birthday" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">成績</label>
                    <input type="text" v-model="model2.student.s_score" class="form-control" />
                </div>
                <div class="mb-3">
                    <button class="btn btn-primary" @click="updateStudent">儲存</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default{
    name:'studentCreate',
    
    data(){
        return {
            studentId : "",
            warning_score:"成績欄位必填",
            warning_id:"學號欄位必填",
            warning_name:"姓名欄位必填",
            warning_birthday:"生日欄位必填",
            warning_sex:"性別欄位必填",
            model:{
                student:{
                    s_id:"",
                    s_name:"",
                    s_sex:"",
                    s_birthday:"",
                    s_score:""
                }
            },
            model2:{
                student:{
                    id:"",
                    s_id:"",
                    s_name:"",
                    s_sex:"",
                    s_birthday:"",
                    s_score:""
                }
            }
        }
    },
    mounted(){
        console.log(this.$route.params.id)
        this.studentId = this.$route.params.id
        this.getStudentData(this.$route.params.id)
    },
    methods:{
        getStudentData(studentId){
            axios.get(`http://localhost:8080/students/${studentId}`)
            .then(res => {
                console.log(res.data)
                this.model2.student.id = res.data.id
                this.model2.student.s_id = res.data.s_id
                this.model2.student.s_name = res.data.s_name
                this.model2.student.s_sex = res.data.s_sex
                this.model2.student.s_birthday = this.formatDate(res.data.s_birthday)
                this.model2.student.s_score = res.data.s_score
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
                return `${year}/${month}/${day}`;
            }
            return '';
        },
        updateStudent(){
            console.log(this.studentId)
            axios.put(`http://localhost:8080/students/${this.studentId}`,this.model2.student)
            .then(res => {
                console.log(res)
                alert("成功更新資料")
            })
            .catch((error) =>{
                    if (error.response.status==422) {
                        console.log("所有表格都要填寫")
                    } 
                    else if (error.request) {
                        console.log(error.request);
                    } 
                    else {
                        console.log('Error', error.message);
                    }
                })
        }
    }
    
}
</script>