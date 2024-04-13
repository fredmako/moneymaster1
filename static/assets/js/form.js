document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#signup-form");
    const steps = Array.from(document.querySelectorAll(".form-step"));
    let currentStep = 0;

    const showStep = (stepIndex) => {
        steps[currentStep].classList.remove("active");
        steps[stepIndex].classList.add("active");
        currentStep = stepIndex;
    };

    const updateFormSummary = () => {
        const formSummary = document.querySelector("#form-summary");
        formSummary.innerHTML = ""; // Clear previous summary

        const formData = new FormData(form);
        formData.forEach((value, key) => {
            const summaryItem = document.createElement("p");
            summaryItem.textContent = `${key}: ${value}`;
            formSummary.appendChild(summaryItem);
        });
    };

    const handleNextButton = () => {
        const nextButtons = Array.from(document.querySelectorAll(".next-btn"));
        nextButtons.forEach((button) => {
            button.addEventListener("click", () => {
                const currentStepInputs = Array.from(steps[currentStep].querySelectorAll("input, textarea"));
                const isStepValid = currentStepInputs.every((input) => input.checkValidity());

                if (isStepValid) {
                    showStep(currentStep + 1);
                    if (currentStep === steps.length - 1) {
                        updateFormSummary();
                    }
                } else {
                    alert("Please fill out all required fields.");
                }
            });
        });
    };

    handleNextButton(); // Initialize event listeners
});
