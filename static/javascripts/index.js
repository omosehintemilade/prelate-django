// JavaScript code to handle side drawer toggle
const drawer = document.getElementById("side-drawer");
const hamburgers = document.querySelectorAll(".fa-bars");

hamburgers.forEach((hamburger) => {
  // console.log({ hamburger });
  hamburger.addEventListener("click", () => {
    drawer.classList.toggle("drawer-open");
  });
});
// JavaScript code to handle side drawer toggle end

// Format Figure
document
  .querySelectorAll(".figure")
  .forEach(
    (figureEl) =>
      (figureEl.textContent = Number(figureEl.textContent).toLocaleString(
        "en-US"
      ))
  );
