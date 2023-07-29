// Tab panes
const tabs = document.querySelectorAll(".tab");
const tabPanes = document.querySelectorAll(".tab-pane");

tabs.forEach((tab, index) =>
  tab.addEventListener("click", () => {
    console.log("tab ", index);

    // remove active class from other tabs
    tabs.forEach((tab) => tab.classList.remove("active"));

    // add active class to clicked tab
    tab.classList.add("active");

    // remove all tab panes and display clicked tab pane
    tabPanes.forEach((pane, paneIndex) => {
      if (paneIndex === index) pane.style.display = "block";
      else pane.style.display = "none";
    });
  })
);

const url = window.location.href;
const splittedUrl = url.split("#");

if (splittedUrl[1] == "submitted") {
  //Swal.fire({
  //  html: "<h5>Your Enquriry has been submitted successfully!. <br /><b>We will reach out to you as soonest.</b></h5>",
  //  });

  const modal = document.querySelector("#defaultModal");
  const modalbackdrop = document.querySelector("#modal-backdrop");

  console.log(modal);

  setTimeout(() => {
    // modal.classList.add("flex");
    console.log("I m setting it");
    modal.style.display = "flex";
  }, 500); // modalbackdrop.classList.add("block!");
  // modal.style.display = "flex";
  modalbackdrop.style.display = "block";
}

// const modal = document.querySelector(".modal");
// console.log(modal)

// modal.classList.add("hidden");
// modal.classList.add("flex");
