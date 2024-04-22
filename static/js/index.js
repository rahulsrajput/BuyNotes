
function toggleList() {
    var list = document.getElementById("myList");
    var icon = document.getElementById("dropdownIcon");

    // Toggle the visibility of the list
    if (list.classList.contains("hidden")) {
        list.classList.remove("hidden");
        icon.classList.remove("fa-chevron-down");
        icon.classList.add("fa-chevron-up");
    } else {
        list.classList.add("hidden");
        icon.classList.remove("fa-chevron-up");
        icon.classList.add("fa-chevron-down");
    }
}


function toggleList1() {
    var list = document.getElementById("myList1");
    var icon = document.getElementById("dropdownIcon1");

    // Toggle the visibility of the list
    if (list.classList.contains("hidden")) {
        list.classList.remove("hidden");
        icon.classList.remove("fa-chevron-down");
        icon.classList.add("fa-chevron-up");
    } else {
        list.classList.add("hidden");
        icon.classList.remove("fa-chevron-up");
        icon.classList.add("fa-chevron-down");
    }
}

