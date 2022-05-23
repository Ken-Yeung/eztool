// <-- ###### class ###### -->
class class_worker{
    constructor(id, debug=false){
        let status = id.toString().charAt(0) == ".";
        if(!status){
            this.elem = document.getElementById(id.toString());
        } else {
            this.elem = document.querySelector(id,toString());
        }
        this.debug = debug;
    }

    add(class_name){
        if(this.elem.classList.contains(class_name) == false){
            this.elem.classList.add(class_name);
            if(this.debug){
                console.log(`Class: [${class_name}] added.`);
            }
        } else if(this.debug){
            console.log(`Class: [${class_name}] existed.`);
        }
        return false;
    }

    remove(class_name){
        if(this.elem.classList.contains(class_name)){
            this.elem.classList.remove(class_name);
            if(this.debug){
                console.log(`Class: [${class_name}] removed.`);
            }
        } else if(this.debug){
            console.log(`Class: [${class_name}] not found.`);
        }
        return false;
    }

    delay_add(class_name, ms){
        var element = this.elem;
        let debug = this.debug;
        setTimeout(()=>{
            if(element.classList.contains(class_name) == false){
                element.classList.add(class_name);
                if(debug){
                    console.log(`Class: [${class_name}] added by delay after ${ms.toString()}ms.`);
                }
            } else if(debug){
                console.log(`Class: [${class_name}] existed after ${ms.toString()}ms.`);
            }
        },ms);
    }

    delay_remove(class_name, ms){
        var element = this.elem;
        let debug = this.debug;
        setTimeout(()=>{
            if(element.classList.contains(class_name)){
                element.classList.remove(class_name);
                if(debug){
                    console.log(`Class: [${class_name}] removed by delay after ${ms.toString()}ms.`);
                }
            } else if(debug){
                console.log(`Class: [${class_name}] not found after ${ms.toString()}ms.`);
            }
        },ms);
    }
}

// INFO:     127.0.0.1:55302 - "POST /uploadfiles HTTP/1.1" 422 Unprocessable Entity
class upload_progress {
    constructor(n){
        this.rate = 1 / n;
        this.counter = 0;
        this.record = [];
    }

    recorder(i){
        let road = i * this.rate;
        this.record.push(road);
        let len = this.record.length;
        if(len < 2){
            this.counter = this.counter + road;
        }else{
            this.counter = this.counter + this.record[len-1] - this.record[len-2];
        }
        return Math.round(this.counter);
    }

    refresh(){
        this.record = [];
    }
}
async function upload_files(e, pos){
    e.preventDefault();
    const files = e.target[pos].files;
    const len_files = files.length;
    let progress_bar = new upload_progress(len_files);
    var config = {
        onUploadProgress: progress => { // While Uploading
            let completed = Math.floor((progress.loaded * 100) / progress.total);
            let progressing = progress_bar.recorder(completed);

            console.log(`Original: ${completed}`);
            console.log(`Completed: ${progressing}%`);
            
            document.getElementById("progress").innerText = progressing.toString() + "%"; //Dom %%
        },
        headers: {
            "Content-Type": "multipart/form-data"
        }
    }

    let BtnController = new class_worker("btn");
    BtnController.add("noshow");

    for(let i = 0; i < len_files; i++){
        let data = new FormData();

        data.append('files', files[i]);
        
        console.log(`Start file name: ${files[i].name}`);
        
        await axios.post("/uploadfiles", data, config)
        .then((response) => { //When Finished upload
            let re_obj = response.data;
        
            if (re_obj.result){
                let p = document.createElement("H4");
                p.innerText = "Finished: " + files[i].name + "\n==========================================";
                document.body.appendChild(p);
                console.log("=====================");
            }
        }).catch((error) => { //Catch Error
            
            console.log(error);
        
        });
        progress_bar.refresh();
    }
    let pp = document.createElement("H1");
    pp.innerText = "Finished All Uploading";
    document.body.appendChild(pp);
    document.getElementById("uploadForm").reset();
    BtnController.remove("noshow");
}

(function () {
    console.log("Document Ready.");
    document.getElementById("uploadForm").addEventListener("submit", e => {
        upload_files(e, 0);
    });
})();