/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                orange: "#F5C518",
                black: {
                    18: "rgb(18, 18, 18)",
                    26: "rgb(26, 26, 26)"
                },
                blue: { 87: "rgb(87, 153, 239)" }
            }
        }
    },
    plugins: []
};
