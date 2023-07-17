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
