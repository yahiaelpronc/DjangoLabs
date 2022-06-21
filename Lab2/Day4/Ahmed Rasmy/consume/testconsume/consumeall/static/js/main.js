////////// Stats Numbers ////////////
function incrementStats() {
    let nums = document.querySelectorAll(".box .num");
    let statsSection = document.querySelector(".stats");
    let started = false;
  
    function startCount(ele) {
      let goal = ele.dataset.goal;
      let count = setInterval(function () {
        ele.textContent++;
        if (ele.textContent == goal) {
          clearInterval(count);
        }
      }, 1000 / goal);
    }
    window.addEventListener("scroll", function () {
      if (window.scrollY >= statsSection.offsetTop - 100) {
        if (!started) {
          nums.forEach((num) => startCount(num));
        }
        started = true;
      }
    });
  }
  incrementStats();
  
  ////////////////// skills progress //////
  let skills = document.querySelector(".skills");
  let spans = document.querySelectorAll(".prog span");
  
  window.addEventListener("scroll", function () {
    //////////// sskills Onscroll/////////
    if (window.scrollY >= skills.offsetTop) {
      spans.forEach((span) => {
        span.style.width = span.dataset.progress;
      });
    }
  });
  