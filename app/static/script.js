document.getElementById("form").addEventListener("submit", async function (e) {
  e.preventDefault();
  
  const formData = new FormData(this);
  const data = {};

  formData.forEach((value, key) => {
    data[key] = Number(value);
  });

  const response = await fetch("http://127.0.0.1:9000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  const result = await response.json();

  const resultDiv = document.getElementById("result");
  resultDiv.style.display = "block";
  resultDiv.innerHTML = `<strong>Result:</strong> ${result.result}<br><strong>Confidence:</strong> ${result.confidence}`;
});