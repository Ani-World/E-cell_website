function initNavigation() {

    const navbar = document.querySelector("nav");
    const navLinks = document.querySelectorAll("nav a");

    /* Navbar background on scroll */

    window.addEventListener("scroll", function () {

        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

    });

    /* Smooth scroll */

    navLinks.forEach(function(link){

        link.addEventListener("click", function(e){

            const targetId = this.getAttribute("href");

            if(targetId.startsWith("#")){

                e.preventDefault();

                const target = document.querySelector(targetId);

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

}