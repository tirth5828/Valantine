setInterval(() => {
    let heart = document.createElement("div");
    heart.innerHTML = "❤️";
    heart.style.position = "absolute";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animation = "float 5s linear";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 5000);
}, 500);
