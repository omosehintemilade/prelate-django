// Sweet Alert Notification
const url = window.location.href;

const splittedUrl = url.split("#");
if (splittedUrl[1]?.includes("submitted")) {
  Swal.fire({
    html: "<h5 class='text-base mobile:text-sm'>Your Enquiry has been submitted successfully!. <br /><b>We will reach out to you as soonest.</b></h5>"
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
