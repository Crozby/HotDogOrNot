document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#link").oninput = () => {
        document.querySelector("#btn_send").disabled = document.querySelector("#link").value === '';
    };

    document.querySelector("#link").oncontextmenu = () => {
        document.querySelector("#link").value = '';
        document.querySelector("#btn_send").disabled = true;
        event.preventDefault();
    };

    document.querySelector("#btn_send").onclick = () => {
        const request = new XMLHttpRequest();
        request.open("POST", "/get_answer");
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data["error"]) {
                document.querySelector("#warning").style.display = "block";
                return;
            } else {
                document.querySelector("#warning").style.display = "none";
            }
            document.querySelector("#answer").innerHTML = data["answer"];
            document.querySelector("#image").src = data["image"];
            document.querySelector("#image").style.display = "block";
        };

        const data = new FormData();
        data.append("path", document.querySelector("#link").value);
        data.append("token", "12w1y2h3u12heu289HU2dsa&8789sak2ed")
        request.send(data);
    }
});
