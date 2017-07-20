document.getElementById("datetime1").defaultValue = "2017-07-20T11:42";
document.getElementById("datetime2").defaultValue = "2017-07-20T11:42";

openModal = function() {
    document.getElementById('new_task_popup').style.display = "block";
}
closeModal = function() {
    document.getElementById('new_task_popup').style.display = "none";
}

document.getElementById("close").onclick = closeModal();

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
