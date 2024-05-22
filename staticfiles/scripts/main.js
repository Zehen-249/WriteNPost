const navTogle = document.querySelector("#navTgl");
const sidebar = document.querySelector("#leftSideBar");


navTogle.onclick = () => {
    console.log(sidebar);
    navTogle.classList.toggle("bi-x-lg");
};
