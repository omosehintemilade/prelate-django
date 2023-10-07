console.log("helllo world from xx.js");

const form = document.querySelector("form");
const checkbox = document.querySelector("#checkbox");

form.addEventListener("submit", async (e) => {
  const button = form.querySelector(".submit-btn");
  try {
    e.preventDefault();

    // change submit button text
    button.innerText = "Submitting...";
    button.disabled = true;
    if (!checkbox.checked) {
      button.innerText = "Submit Form";
      button.disabled = false;

      let html = `Oops! <br /><b>We need your consent to be able to process your application on your behalf</b>`;

      Swal.fire({
        icon: "error",
        html: `<h5 class='text-base mobile:text-sm'>${html}</h5>`
      });
      return;
    }

    // CONSTRUCT APPLICANT DATA
    const applicantInfoSection = document.querySelector("#applicant-info-body");
    const applicant_info = {
      travel_history: []
    };

    // Grab all input elements
    const inputEls = applicantInfoSection.querySelectorAll("input");
    console.log({ inputEls });
    // Grab all select elements
    const selectEls = applicantInfoSection.querySelectorAll("select");
    console.log({ selectEls });

    inputEls.forEach((el) => {
      // finetune applicants data to match the format the model is expecting
      const pattern = /^travel_history_info_\[\d+\]$/;

      if (pattern.test(e.name)) {
        // push into travel history array
        applicant_info.travel_history.push(el.value);
      } else {
        applicant_info[el.name] = el.value;
      }
    });
    selectEls.forEach((el) => {
      applicant_info[el.name] = el.value;
    });

    console.log({ applicant_info });

    const applicant_info_hardcoded = {
      travel_history: [],
      firstname: "Omosehin",
      middlename: "Ifeoluwa",
      surname: "O",
      nationality: "Nigeria",
      dob: "2023-10-04",
      tribe: "Yoruba",
      email: "olayinka.omosehin@charisol.io",
      phone_number: "+2341234567890",
      permanent_address: "Lagos Mainland",
      postal_address: "Lagos Mainland",
      alt_phone_number: "+2348137650935",
      passport_number: "12345678900",
      date_of_issue: "2023-10-24",
      date_of_expiry: "2023-10-04",
      // "travel_info_[0]": "Hello world One",
      // "travel_info_[1]": "Hello world Two",
      // "travel_info_[2]": "Hello world Three",
      travel_history: [
        "Hello world One",
        "Hello world Two",
        "Hello world Three"
      ],
      title: "Mrs",
      gender: "MALE",
      marital_status: "ENGAGED"
    };

    // CONSTRUCT APPLICANT EDUCATION DATA
    const educationHistorySection = document.querySelector(
      "#educational-history-body"
    );
    const education_history = [];

    // Grab the li's
    const educationHistoryList = educationHistorySection.querySelectorAll("li");

    console.log({ educationHistoryList });

    educationHistoryList.forEach((li) => {
      const education = {};
      // Grab all input elements
      const inputEls = li.querySelectorAll("input");
      console.log({ inputEls });
      // Grab all select elements
      inputEls.forEach((el) => (education[el.name] = el.value));
      education.educational_level = li.querySelector("select").value;
      console.log({ education });
      education_history.push(education);
    });
    console.log({ education_history });

    const education_history_hardcoded = [
      {
        name_of_institution: "Institution One",
        date_attended: "2023-10-01",
        date_graduated: "2023-10-07",
        institution_address: "Lagos Mainland",
        educational_level: "PRIMARY"
      },
      {
        name_of_institution: "Institution Two",
        date_attended: "2023-08-27",
        date_graduated: "2023-11-02",
        institution_address: "Lagos Mainland",
        educational_level: "SECONDARY"
      },
      {
        name_of_institution: "Institution Three",
        date_attended: "2023-10-24",
        date_graduated: "2023-10-07",
        institution_address: "No 58 Mbano street, Aladinma IMO state",
        educational_level: "TERTIARY"
      }
    ];
    // return;
    const req = await fetch("", {
      method: "POST",
      body: JSON.stringify({
        applicant_info: applicant_info_hardcoded,
        education_history: education_history_hardcoded
      }),

      headers: {
        "content-type": "application/x-www-form-urlencoded",
        "X-CSRFToken": getCookie("csrftoken")
      }
    });

    const data = await req.json();

    console.log({ data });
    button.innerText = "Submit Form";
    button.disabled = false;

    Swal.fire({
      html: `<h5 class='text-base mobile:text-sm'>🎉🎉🎉 <br /> Thank you for trusting us with your visa application process<br /><b>We will reach out to you as soonest.</b></h5>`
    });
    // Trigger
  } catch (error) {
    button.innerText = "Submit Form";
    button.disabled = false;
  }
});

$(document).ready(function () {
  $(".country_of_choice").select2();
});
