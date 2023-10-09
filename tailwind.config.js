/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    screens: {
      mobile: { max: "500px" },
      tablet: { max: "768px" },
      laptop: { max: "1024px" },
      desktop: { max: "1280px" },
      xtraLarge: { min: "1281px" }
    },
    extend: {
      colors: {
        primary: "#1C2E6A",
        textPrimary: "#6A6A6A",
        buttonPrimary: "#FFC702"
      },
      listStyleType: {
        disclosureClosed: "disclosure-closed",
        "lower-alpha": "lower-alpha",
        "upper-alpha": "upper-alpha"
      },
      fontSize: {
        xxs: "10px"
      }
    }
  },
  plugins: [require("flowbite/plugin")]
};
