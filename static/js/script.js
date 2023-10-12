// Modal event
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

var modal = document.getElementById("change-profile-picture-modal");
var button = document.getElementById("change-profile-picture-button");
var span = document.getElementsByClassName("close")[0];

button.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

document.getElementById("add_image_field").addEventListener("click", function () {
    var newInput = document.createElement("input");
    newInput.type = "file";
    newInput.name = "images";
    newInput.className = "form-control";
    newInput.multiple = true;
    document.getElementById("additional_image_fields").appendChild(newInput);
});