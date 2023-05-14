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

const signInButton = document.getElementById("sign-in-button");

if (signInButton) {
    signInButton.addEventListener("click", () => {
        const modal = document.getElementById("sign-in-popup");
        modal.showModal();
    });
}

const closeModalButton = document.getElementById("close-modal");

closeModalButton.addEventListener("click", () => {
    const modal = document.getElementById("sign-in-popup");
    modal.close();
});

const details = document.querySelector("details");

if (details) {
    const list = details.querySelector("ul");

    console.log(details);

    list.onmouseleave = () => {
        console.log("mouseleave called");
        details.removeAttribute("open");
    };
}
