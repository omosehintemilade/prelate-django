const url = window.location.href;

const EnumRedirectParams = {
  travelInfo: "travel-info",
  travelBudget: "travel-budget",
  requestChanges: "request-change"
};

// select tab panes based on redirect urls params
const redirectParam = url.split("?")?.[1]?.split("=");
console.log({ redirectParam });

// Tab panes
const tabs = document.querySelectorAll(".tab");
const tabPanes = document.querySelectorAll(".tab-pane");

tabs.forEach((tab, index) =>
  tab.addEventListener("click", () => {
    console.log("tab ", index);

    activateTab(index);
  })
);

const splittedUrl = url.split("#");
if (splittedUrl[1] == "submitted") {
  Swal.fire({
    html: "<h5>Your Enquiry has been submitted successfully!. <br /><b>We will reach out to you as soonest.</b></h5>"
  });
}

// Select dropdown html
const countriesDropdownText = document.querySelector("#countriesDropdown span");

const countriesDropdownOptions = document.querySelectorAll(
  "#countriesDropdownOption"
);
console.log({ countriesDropdownText });
countriesDropdownOptions.forEach((opt) => {
  opt.addEventListener("click", (e) => {
    countriesDropdownText.innerText = e.target.innerText;
  });
});
// Select dropdown html

// Prevent users from seeing the modal twice on reload
// console.log({ btn: document.querySelector(".swal2-confirm") });
// alert("foo bar");
// document.querySelector(".swal2-confirm").addEventListener("click", () => {
//   alert("hellow");
//   const url = window.location.href;
//   const splittedUrl = url.split("#");
//   console.log(splittedUrl[0]);
//   window.location.href = splittedUrl[0];
//   console.log("redirecting...");

//   window.history.pushState({}, document.title, );

// });

console.log({ btn: document.querySelector(".swal2-confirm") });
alert("foo bar");
document.querySelector(".swal2-confirm").addEventListener("click", () => {
  alert("hellow");
  const url = window.location.href;
  const splittedUrl = url.split("#");
  console.log(splittedUrl[0]);
  console.log("redirecting...");

  window.history.pushState({}, document.title, splittedUrl[0]);
});

// FUNCTIONS
function activateTab(currentTabIndex) {
  console.log({ currentTabIndex });
  tabs.forEach((tab) => {
    const activeTab = document.querySelector(".active");

    activeTab.classList.remove("active");

    // add active class to clicked tab
    tab.classList.add("active");

    // remove all tab panes and display clicked tab pane
    tabPanes.forEach((pane, paneIndex) => {
      if (paneIndex === currentTabIndex) pane.style.display = "block";
      else pane.style.display = "none";
    });
  });
}
