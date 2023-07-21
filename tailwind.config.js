/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: "#1C2E6A"
      }
    }
  },
  plugins: [require("flowbite/plugin")]
};
