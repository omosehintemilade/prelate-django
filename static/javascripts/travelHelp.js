const desktopTabs = document.querySelectorAll(".travel-info .tab");
const mobileTabs = document.querySelectorAll(".travel-mobile-nav .tab");
const tabPanes = document.querySelectorAll(".tab-pane");
const pageHeroSection = document.querySelector(".travel-info-hero-section");

const EnumRedirectParams = {
  travelInfo: "travel-info",
  travelBudget: "travel-budget",
  requestChanges: "request-changes"
};

const heroSections = [
  {
    className: "travel-info-hero",
    documentTitle: "Travel Info | Prelate Travels & Tours"
  },
  {
    className: "travel-budget-hero",
    documentTitle: "Travel Budget | Prelate Travels & Tours"
  },
  {
    className: "change-request-hero",
    documentTitle: "Request Changes | Prelate Travels & Tours"
  }
]; //Arranged in order which the tabs are arranged

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

// FUNCTIONS
function activateTab(index) {
  console.log({ index });

  const mobileActiveTab = document.querySelector(".travel-mobile-nav .active");
  const desktopActiveTab = document.querySelector(".travel-info .active");

  mobileActiveTab.classList.remove("active");
  desktopActiveTab.classList.remove("active");

  desktopTabs?.[index].classList.add("active");
  mobileTabs?.[index].classList.add("active");

  // Update page to use tab specific configuration
  const section = heroSections[index];
  if (section) {
    // update document title
    document.title = section.documentTitle;
    // remove all existing heroSection classes on pageHeroSection
    heroSections.forEach((i) => pageHeroSection.classList.remove(i.className));
    // add class to pageHeroSection
    pageHeroSection.classList.add(section.className);
  }

  // remove all tab panes and display clicked tab pane
  tabPanes.forEach((pane, paneIndex) => {
    if (paneIndex === index) pane.style.display = "block";
    else pane.style.display = "none";
  });
}

// Select Dropdown
document.querySelector("#countries")?.addEventListener("change", (e) => {
  window.location = `${url.split("?")[0]}?country=${e.target.value}`;
});
