function checkPassword() {
    let password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/check-password", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        let message = `Strength: ${data.strength}`;
        if (data.pwned) message += " ⚠️ (This password has been leaked)";
        document.getElementById("result").innerText = message;
    })
    .catch(error => console.error("Error:", error));
}
