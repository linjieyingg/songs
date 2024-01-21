function createTextCursor(event){
    let el = document.getElementById("hovering");
      el.style.top = event.clientY + "px";
      el.style.left = event.clientX + "px";
  }
  
function play(){
  let audio = document.getElementById('preview')
  audio.play()
}