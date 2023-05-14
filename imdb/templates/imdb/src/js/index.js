"use strict";

const openBurgerMenuButton = document.getElementById("burger-menu-button");
const closeBurgerMenuButton = document.getElementById("burger-close-button");
const burgerMenu = document.getElementById("burger-menu");

openBurgerMenuButton.addEventListener("click", () => {
    burgerMenu.style.transform = "translateX(0)";
});
closeBurgerMenuButton.addEventListener("click", () => {
    burgerMenu.style.transform = "translateX(-100%)";
});
