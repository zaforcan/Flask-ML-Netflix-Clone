const sections = document.querySelectorAll("section");

window.addEventListener("scroll", function () {
	sections.forEach((section) => {
		const distFromTop =
			document.body.scrollTop + section.getBoundingClientRect().top;
		if (distFromTop < 10) {
			document.body.style.background = section.dataset.color;
		}
	});
});
