const qrFormEl = document.getElementById("qr-form")
qrFormEl.addEventListener("submit",( event)=>{
 event.preventDefault();
})

const formeData = new FormData(qrFormEl)
const text =  formeData.get("qrtext")
console.log("text");
