function createTextCursor(event){
    let el = document.getElementById("hovering");
      el.style.top = event.clientY + "px";
      el.style.left = event.clientX + "px";
  }
  
document.getElementById("hovering").addEventListener('mouseover', createTextCursor);

