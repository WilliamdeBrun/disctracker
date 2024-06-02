/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"

  ],
  theme: {
    extend: {
      backgroundImage:{
        'my': "url('../assets/background-dg.png')", 
      },
    },
  },
  plugins: [],
}

