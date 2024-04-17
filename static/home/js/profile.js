document.addEventListener("DOMContentLoaded", () => {
 var profile = document.getElementById("profile-dropdown");
 window.addEventListener("click",() => {
   profile.style.display = "none";
 })
  var profile_btn = document.getElementById("profile-btn")
  profile_btn.addEventListener("click", (event)=> {
    event.stopPropagation();
    if (profile.style.display != "none") {
     profile.style.display = "none";
    } else {
     profile.style.display = "revert";
    }
  }
)

 });
