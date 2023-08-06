// Sweet Alert Notification
const url = window.location.href;

const splittedUrl = url.split("#");

if (splittedUrl[1]?.includes("submitted")) {
  let html = `Your Enquiry has been submitted successfully! <br /><b>We will reach out to you as soonest.</b>`;

  // if notification is for newsletter sub
  const redirectParam = url.split("?")?.[1]?.split("=")[1];

  console.log({ redirectParam });

  if (redirectParam === "subscribe")
    html = `🎉🎉🎉 <br /> Thank you for joining our newsletters list! <br /><b>Be on the lookout for amazing contents from us</b>`;

  Swal.fire({
    html: `<h5 class='text-base mobile:text-sm'>${html}</h5>`
  });
}

// console.log({ btn: document.querySelector(".swal2-confirm") });
document.querySelector(".swal2-confirm")?.addEventListener("click", () => {
  const url = window.location.href;
  const splittedUrl = url.split("#");
  // console.log(splittedUrl[0]);
  // console.log("redirecting...");

  //   change url without reloading the page
  window.history.pushState({}, document.title, splittedUrl[0]);
});
