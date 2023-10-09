$(document).ready(function () {
  console.log("helllo world from xx.js");

  // REGISTER SELECT ELEMENT
  $(".countries").select2();

  const form = document.querySelector("form");
  const checkbox = document.querySelector("#checkbox");

  form.addEventListener("submit", async (e) => {
    const button = form.querySelector(".submit-btn");

    e.preventDefault();

    // change submit button text
    button.innerText = "Submitting...";
    button.disabled = true;
    if (!checkbox.checked) {
      button.innerText = "Submit Form";
      button.disabled = false;

      Swal.fire({
        icon: "error",
        html: `<h5 class='text-base mobile:text-sm'><b>Oops!</b> <br />We need your consent to be able to process your application on your behalf</h5>`
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
    // CONSTRUCT PARENT/GUARDIAN INFO
    const relationships_info = getRelationshipsInfo();
    // CONSTRUCT OTHER INFO DATA
    const other_info = getOtherInfo();

    try {
      const req = await fetch("", {
        method: "POST",
        body: JSON.stringify({
          applicant_info,
          education_history,
          application_info,
          relationships: [
            emergency_contact,
            ...guardians_info,
            ...relationships_info
          ],
          other_info
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
      console.log({ error });
      Swal.fire({
        icon: "error",
        html: `<h5 class='text-base mobile:text-sm'><b>Oops!</b> <br />Sorry an error occured while processing your request</h5>`
      });

      // Swal.fire({
      //   icon: "error",
      //   html: `<h5 class='text-base mobile:text-sm'><b>Oops!</b> <br />${
      //     error || "Sorry an error occured while processing your request"
      //   }</h5>`
      // });
    }
  });

  // APPLICANT INFO
  const getApplicantInfo = () => {
    const section = form.querySelector("#applicant-info-body");
    const data = {
      travel_history: []
    };

    // Grab all input elements
    const inputEls = section.querySelectorAll("input");
    console.log({ inputEls });
    // Grab all select elements
    const selectEls = section.querySelectorAll("select");
    console.log({ selectEls });

    [...inputEls, ...selectEls].forEach((el) => {
      // check if el is required - we're using this format because using the collapsible component removes the input from the dom hence the "required" attribute is useless
      const isRequired = Boolean(el.getAttribute("isrequired"));
      // console.log(el.name, isRequired, el.getAttribute("isRequired"));

      console.log("required field", isRequired, el.value, !el.value);
      if (isRequired && !el.value) {
        console.log(section.parentElement.querySelector("h2 button"));
        section.parentElement
          .querySelector("h2 button")
          .setAttribute("aria-expanded", "true");
        section.classList.remove("hidden");
        el.focus();
        Swal.fire({
          icon: "error",
          html: `<h5 class='text-base mobile:text-sm'><b>Error!</b> <br />Please fill in all required fields</h5>`
        });
        throw Error("field is required");
      }
      // finetune applicants travel history format to match the format the model is expecting
      const pattern = /^travel_info_\[\d+\]$/;
      if (pattern.test(el.name)) {
        // push into travel history array
        data.travel_history.push(el.value);
        // remove it from the data object
        delete data[el.name];
      } else {
        data[el.name] = el.value;
      }
    });

    console.log({ applicant_info: data });
    return data;
  };

  function validateInput(params) {}
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

    return data;
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

    console.log({ application_info: data });
    return data;
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

    console.log({ getEmergencyContactInfo: data });
    return data;
  };

  // GUARDIAN HISTORY
  const getGuardiansInfo = () => {
    const section = form.querySelector("#guardian-info-body");
    const data = [];

    // Grab the li's
    const li = section.querySelectorAll("li");

    console.log({ li });

    li.forEach((li) => {
      const guardian = {};
      // Grab all input elements
      const inputEls = li.querySelectorAll("input");
      const selectEls = li.querySelectorAll("select");
      [...inputEls, ...selectEls].forEach(
        (el) => (guardian[el.name] = el.value)
      );
      guardian.relationship = li.getAttribute("relationship");
      data.push(guardian);
    });
    console.log({ getGuardiansInfo: data });

    return data;
  };

  // GUARDIAN HISTORY
  const getRelationshipsInfo = () => {
    const section = form.querySelector("#relationship-info-body");
    const data = [];

    // Grab the li's
    const li = section.querySelectorAll("li");
    console.log({ li });
    li.forEach((li) => {
      // Get the type of the relationship
      const relation = {};
      console.log({ relation });
      // Grab all input elements
      const inputEls = li.querySelectorAll("input");
      const selectEls = li.querySelectorAll("select");
      [...inputEls, ...selectEls].forEach(
        (el) => (relation[el.name] = el.value)
      );
      // If Relationship wasn't filled
      if (!areAllObjectValuesEmpty(relation)) {
        data.push({
          ...relation,
          relationship: li.getAttribute("relationship").toUpperCase()
        });
      }
    });
    console.log({ getRelationshipsInfo: data });

    return data;
  };

  // APPLICANT INFO
  const getOtherInfo = () => {
    const section = form.querySelector("#other-info-body");
    const data = {
      extra_curicular_activities: []
    };

    // Grab all input elements
    const inputEls = section.querySelectorAll("input");

    const textAreas = section.querySelectorAll("textarea");

    [...inputEls, ...textAreas].forEach((el) => {
      // finetune applicants travel history format to match the format the model is expecting
      const pattern = /^extra_curicular_activity_\[\d+\]$/;

      if (pattern.test(el.name)) {
        // push into extra_curicular_activities array
        data.extra_curicular_activities.push(el.value);
      } else {
        data[el.name] = el.value;
      }
    });

    console.log({ getOtherInfo: data });

    return data;
  };

  function areAllObjectValuesEmpty(obj) {
    console.log({ obj });
    for (const value of Object.values(obj)) if (value !== "") return false;
    return true;
  }
});
