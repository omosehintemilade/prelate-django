const url = window.location.href;
const desktopTabs = document.querySelectorAll(".travel-info .tab");
const mobileTabs = document.querySelectorAll(".travel-mobile-nav .tab");
const tabPanes = document.querySelectorAll(".tab-pane");

console.log({ desktopTabs, mobileTabs });

const EnumRedirectParams = {
  travelInfo: "travel-info",
  travelBudget: "travel-budget",
  requestChanges: "request-changes"
};

// select tab panes based on redirect urls params
const redirectParam = url.split("?")?.[1]?.split("=")[1];

if (redirectParam) {
  if (redirectParam === EnumRedirectParams.travelInfo) activateTab(0);
  else if (redirectParam === EnumRedirectParams.travelBudget) activateTab(1);
  else if (redirectParam === EnumRedirectParams.requestChanges) activateTab(2);
}

// console.log({ redirectParam });

// Tabs && Tab panes
desktopTabs?.forEach((tab, index) =>
  tab.addEventListener("click", () => activateTab(index))
);
mobileTabs?.forEach((tab, index) =>
  tab.addEventListener("click", () => activateTab(index))
);

// Sweet Alert
const splittedUrl = url.split("#");
if (splittedUrl[1]?.includes("submitted")) {
  Swal.fire({
    html: "<h5 class='text-sm'>Your Enquiry has been submitted successfully!. <br /><b>We will reach out to you as soonest.</b></h5>"
  });
}

// console.log({ btn: document.querySelector(".swal2-confirm") });
document.querySelector(".swal2-confirm")?.addEventListener("click", () => {
  const url = window.location.href;
  const splittedUrl = url.split("#");
  // console.log(splittedUrl[0]);
  // console.log("redirecting...");

  window.history.pushState({}, document.title, splittedUrl[0]);
});

// FUNCTIONS
function activateTab(currentTabIndex) {
  console.log({ currentTabIndex });

  const mobileActiveTab = document.querySelector(".travel-mobile-nav .active");
  const desktopActiveTab = document.querySelector(".travel-info .active");

  mobileActiveTab.classList.remove("active");
  desktopActiveTab.classList.remove("active");

  desktopTabs?.[currentTabIndex].classList.add("active");
  mobileTabs?.[currentTabIndex].classList.add("active");

  // remove all tab panes and display clicked tab pane
  tabPanes.forEach((pane, paneIndex) => {
    if (paneIndex === currentTabIndex) pane.style.display = "block";
    else pane.style.display = "none";
  });
}

// Select Dropdown
document.querySelector("#countries")?.addEventListener("change", (e) => {
  window.location = `${url.split("?")[0]}?country=${e.target.value}`;
});
