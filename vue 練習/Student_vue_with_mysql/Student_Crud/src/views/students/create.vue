<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                <h4>Add student</h4>
            </div>
            <div class="card-body">
                <div class="alert alert-warning" v-if=" model.student.s_id == '' || model.student.s_name == ''
                || model.student.s_sex == '' || model.student.s_birthday == '' || model.student.s_score == '' ">
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
                    <label for="">學號</label>
                    <input type="text" v-model="model.student.s_id" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">姓名</label>
                    <input type="text" v-model="model.student.s_name" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">性別</label>
                    <input type="text" v-model="model.student.s_sex" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">生日</label>
                    <input type="text" v-model="model.student.s_birthday" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">成績</label>
                    <input type="text" v-model="model.student.s_score" class="form-control" />
                </div>
                <div class="mb-3">
                    <button class="btn btn-primary" @click="saveStudent">儲存</button>
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
            }
        }
    },
    methods:{
        saveStudent(){
            axios.post('http://localhost:8080/students',this.model.student)
            .then(res=>{
                console.log(res)
                this.model.student={
                    s_id:"",
                    s_name:"",
                    s_sex:"",
                    s_birthday:"",
                    s_score:""
                }
                // alert(res.data.message)
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