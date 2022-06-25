// increase numbers
function incrementStats() {
  let nums = document.querySelectorAll(".section .section-details .num");
  let statsSection = document.querySelector("#expereince");
  let started = false;

  function startCount(ele) {
    let goal = ele.dataset.goal;
    let count = setInterval(function () {
      ele.textContent++;
      if (ele.textContent == goal) {
        clearInterval(count);
      }
    }, 2000 / goal);
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

// show button scroll

let span = document.querySelector(".up");

window.onscroll = function () {
  if (this.scrollY >= 500) {
    span.classList.add("show");
  } else {
    span.classList.remove("show");
  }
};

function scrollTopPage() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
