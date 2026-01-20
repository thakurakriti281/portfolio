<head>
  <title>Chatbot</title>

  <!-- JS written in head -->
  <script>
    function openChat() {
      document.getElementById("chatModal").style.display = "block";
    }

    function closeChat() {
      document.getElementById("chatModal").style.display = "none";
    }

    async function sendChat() {
      const input = document.getElementById("chatInput");
      const chatBody = document.getElementById("chatBody");

      const msg = input.value.trim();
      if (!msg) return;

      chatBody.innerHTML += `<div class="message user">${msg}</div>`;

      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
      });

      const data = await res.json();
      chatBody.innerHTML += `<div class="message bot">${data.reply}</div>`;

      input.value = "";
      chatBody.scrollTop = chatBody.scrollHeight;
    }
  </script>

</head>
