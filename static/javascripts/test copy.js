console.log("helllo world from xx.js");

const form = document.querySelector("form");
const checkbox = document.querySelector("#checkbox");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!checkbox.checked) {
    let html = `Oops! <br /><b>We need your consent to be able to process your application on your behalf</b>`;

    Swal.fire({
      icon: "error",
      html: `<h5 class='text-base mobile:text-sm'>${html}</h5>`
    });
    return;
  }

  // CONSTRUCT APPLICANT DATA
  const applicantInfoSection = document.querySelector("#applicant-info-body");
  const applicant_info = {};

  // Grab all input elements
  const inputEls = applicantInfoSection.querySelectorAll("input");
  console.log({ inputEls });
  // Grab all input elements
  const selectEls = applicantInfoSection.querySelectorAll("select");
  console.log({ selectEls });
  //  // Grab all input elements
  //  const inputEls = applicantInfoSection.querySelectorAll("");
  // console.log({ inputEls });
  inputEls.forEach((el) => {
    applicant_info[el.name] = el.value;
  });
  selectEls.forEach((el) => {
    applicant_info[el.name] = el.value;
  });

  console.log({ applicant_info });

  return;
  const payload1 = {
    siblings: [
      {
        name: "FOO",
        email: "bar"
      },
      {
        name: "FOO1",
        email: "bar1"
      }
    ],
    name: "Olayinka"
  };

  const req = await fetch("", {
    method: "POST",
    body: JSON.stringify(payload1),

    headers: {
      "content-type": "application/x-www-form-urlencoded",
      "X-CSRFToken": getCookie("csrftoken")
    }
  });

  const data = await req.json();

  console.log({ data });
  //   form.submit()
});
