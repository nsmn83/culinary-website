function toggleMenu() {
  const nav = document.getElementById("myTopnav");
  const dropdowns = nav.querySelectorAll('.dropdown .dropdown-content');

  if (nav.className === "topnav") {
    nav.className += " responsive";
  } else {
    nav.className = "topnav";
  }

  // Ukryj wszystkie submenu przy każdym toggle hamburgera
  dropdowns.forEach(dd => {
    dd.style.display = "none";
  });
}

// Funkcja dla mobilnego rozwijania submenu
function toggleDropdown(event) {
  if (window.innerWidth <= 600) {
    event.preventDefault();
    const dropdownContent = event.currentTarget.nextElementSibling;

    // Toggle tylko tego dropdownu
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  }
}
