window.addEventListener("resize", handleChange);

function handleChange() {
    let headerSpacerHeight = document.getElementsByTagName("header")[0].offsetHeight;
    document.getElementById("header-spacer").style.height = (headerSpacerHeight + "px");
}
handleChange()

