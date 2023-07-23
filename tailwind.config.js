/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: "#1C2E6A",
        textPrimary: "#6A6A6A"
      },
      listStyleType: {
        disclosureClosed: "disclosure-closed"
      }
    }
  },
  plugins: [require("flowbite/plugin")]
};
