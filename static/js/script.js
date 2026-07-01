const video = document.getElementById("video");

let stream = null;

// Start Camera
document.getElementById("startCamera").onclick = async ()=>{

    stream = await navigator.mediaDevices.getUserMedia({

        video:{
            facingMode:"environment"
        }

    });

    video.srcObject = stream;

    setInterval(detectFrame,500);

}

// Stop Camera
document.getElementById("stopCamera").onclick = ()=>{

    if(stream){

        stream.getTracks().forEach(track=>track.stop());

    }

}
async function detectFrame(){

    if(stream == null) return;

    const canvas = document.getElementById("canvas");

    canvas.width = video.videoWidth;

    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(video,0,0);

    const image = canvas.toDataURL("image/jpeg");

    const response = await fetch("/detect/frame",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            image:image

        })

    });

    const data = await response.json();

    updateTable(data);

}
function updateTable(data){

    let table =

    `<tr>

    <th>Object</th>

    <th>Jumlah</th>

    </tr>`;

    for(let key in data.count){

        table +=

        `<tr>

        <td>${key}</td>

        <td>${data.count[key]}</td>

        </tr>`;

    }

    document.getElementById("resultTable").innerHTML = table;

}