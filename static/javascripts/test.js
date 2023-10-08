$(document).ready(function () {
  console.log("helllo world from xx.js");

  // REGISTER SELECT ELEMENT
  $(".countries").select2();

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
      const applicant_info = getApplicantInfo();
      // CONSTRUCT APPLICANT EDUCATION DATA
      const education_history = getEducationHistory();
      // CONSTRUCT APPLICANT APPLICATION INFO
      const application_info = getApplicationInfo();
      // CONSTRUCT EMERGENCY CONTACT INFO
      const emergency_contact = getEmergencyContactInfo();
      // CONSTRUCT PARENT/GUARDIAN INFO
      const guardians_info = getGuardiansInfo();
      // return;
      const req = await fetch("", {
        method: "POST",
        body: JSON.stringify({
          applicant_info,
          education_history,
          application_info,
          relationships: [emergency_contact, ...guardians_info]
        }),

        headers: {
          "content-type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCookie("csrftoken")
        }
      });

      const data = await req.json();

      console.log({ data });
      // Update Button
      button.innerText = "Submit Form";
      button.disabled = false;

      Swal.fire({
        html: `<h5 class='text-base mobile:text-sm'>🎉🎉🎉 <br /> Thank you for trusting us with your visa application process<br /><b>We will reach out to you as soonest.</b></h5>`
      });
      form.reset();
      // Trigger
    } catch (error) {
      button.innerText = "Submit Form";
      button.disabled = false;
    }
  });

  // APPLICANT INFO
  const getApplicantInfo = () => {
    const applicantInfoSection = form.querySelector("#applicant-info-body");
    const data = {
      travel_history: []
    };

    // Grab all input elements
    const inputEls = applicantInfoSection.querySelectorAll("input");
    console.log({ inputEls });
    // Grab all select elements
    const selectEls = applicantInfoSection.querySelectorAll("select");
    console.log({ selectEls });

    inputEls.forEach((el) => {
      // finetune applicants travel history format to match the format the model is expecting
      const pattern = /^travel_history_info_\[\d+\]$/;

      if (pattern.test(el.name)) {
        // push into travel history array
        data.travel_history.push(el.value);
      } else {
        data[el.name] = el.value;
      }
    });

    selectEls.forEach((el) => {
      data[el.name] = el.value;
    });

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
    console.log({ applicant_info: data });
    // return data;
    return applicant_info_hardcoded;
  };

  // EDUCATION HISTORY
  const getEducationHistory = () => {
    const educationHistorySection = form.querySelector(
      "#educational-history-body"
    );
    const data = [];

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
      data.push(education);
    });
    console.log({ education_history: data });

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

    // return data
    return education_history_hardcoded;
  };

  // APPLICATION INFO
  const getApplicationInfo = () => {
    const applicationInfoSection = form.querySelector("#application-info-body");
    const data = {};
    // Grab all input elements
    const inputEls = applicationInfoSection.querySelectorAll("input");
    console.log({ inputEls });
    // Grab select elements
    const selectEl = applicationInfoSection.querySelector("select");
    console.log({ selectEl });

    [...inputEls, selectEl].forEach((el) => {
      data[el.name] = el.value;
    });

    const hardcoded_data = {
      country_not_listed: "Nicaragua",
      course: "Main Course",
      alternative_course: "Alternative Course",
      province: "Province Of Choice",
      country: "Nigeria"
    };
    console.log({ application_info: data });
    // return data;

    return hardcoded_data;
  };

  // EMERGENCY CONTACT INFO
  const getEmergencyContactInfo = () => {
    const section = form.querySelector("#emergency-contact-body");
    const data = {};
    // Grab all input elements
    const inputEls = section.querySelectorAll("input");
    // Grab select elements
    const selectEl = section.querySelector("select");

    [...inputEls, selectEl].forEach((el) => {
      data[el.name] = el.value;
    });

    const hardcoded_data = {
      fullname: "Omosehin Ifeoluwa O",
      relationship: "Brother",
      date_of_birth: "2023-10-31",
      email_address: "olayinka.omosehin@charisol.io",
      phone_number: "+2341234567890",
      permanent_address: "Lagos Mainland",
      gender: "MALE"
    };
    console.log({ getEmergencyContactInfo: data });
    // return data;

    return hardcoded_data;
  };

  // EDUCATION HISTORY
  const getGuardiansInfo = () => {
    const section = form.querySelector("#guardian-info-body");
    const data = [];

    // Grab the li's
    const li = section.querySelectorAll("li");

    console.log({ li });

    li.forEach((li, index) => {
      const guardian = {};
      // Grab all input elements
      const inputEls = li.querySelectorAll("input");
      const selectEls = li.querySelectorAll("select");
      const relationships = ["FATHER", "MOTHER"];
      console.log({ index });
      [...inputEls, ...selectEls].forEach(
        (el) => (guardian[el.name] = el.value)
      );
      guardian.relationship = relationships[index];
      data.push(guardian);
    });
    console.log({ getGuardiansInfo: data });

    const hardcoded_data = [
      {
        fullname: "Omosehin Ifeoluwa O",
        date_of_birth: "2023-10-22",
        current_employment: "Doctor",
        permanent_address: "Lagos Mainland",
        gender: "MALE",
        marital_status: "ENGAGED",
        relationship: "FATHER"
      },
      {
        fullname: "Oluchi Osuagwu",
        date_of_birth: "2023-10-04",
        current_employment: "Trader",
        permanent_address: "No 58 Mbano street, Aladinma IMO state",
        gender: "FEMALE",
        marital_status: "DIVORCED",
        relationship: "MOTHER"
      }
    ];

    // return data
    return hardcoded_data;
  };
});
