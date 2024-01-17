function createTextCursor(event){
    let el = document.getElementById("hoveringText");
      el.style.top = event.clientY + "px";
      el.style.left = event.clientX + "px";
  }
  
document.querySelector(".hovering").addEventListener('onmouseover', createTextCursor);