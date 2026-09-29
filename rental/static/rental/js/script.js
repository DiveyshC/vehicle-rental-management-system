document.addEventListener("DOMContentLoaded", function () {

    /*
     * ==========================================
     * MOBILE MENU
     * ==========================================
     */

    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav-menu");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();

            navMenu.classList.toggle("active");
        });
    }


    /*
     * ==========================================
     * VEHICLES NAVIGATION
     * ==========================================
     *
     * This prevents any other click handler from
     * changing the Vehicles navigation.
     */

    document.addEventListener(
        "click",
        function (event) {

            const vehiclesLink = event.target.closest(
                'a[href="/vehicles/"]'
            );

            if (!vehiclesLink) {
                return;
            }

            event.preventDefault();
            event.stopPropagation();

            window.location.assign("/vehicles/");
        },
        true
    );


    /*
     * ==========================================
     * OTHER NAVIGATION LINKS
     * ==========================================
     */

    const navLinks = document.querySelectorAll(".nav-menu a");

    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            const href = this.getAttribute("href");

            if (href === "/vehicles/") {
                return;
            }

            if (navMenu) {
                navMenu.classList.remove("active");
            }
        });

    });


    /*
     * ==========================================
     * AUTO HIDE MESSAGES
     * ==========================================
     */

    const messages = document.querySelectorAll(
        ".alert, .message, .messages li"
    );

    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 4000);

    });

});